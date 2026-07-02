from fastapi import FastAPI
from models.chat import ChatRequest, ChatResponse,Recommendation
from fastapi.middleware.cors import CORSMiddleware
from service.catalog_service import search_catalog
from dotenv import load_dotenv
from service.ai_service import (
    generate_response,
    extract_search_query,
    compare_assessments
)


load_dotenv()
conversation_state = {
    "last_query": "",
    "last_matches": []
}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {"message":"Welcome to SHL AI BACKEND"}

@app.get("/health")
def health():
    return {"status":"okay"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    latest_message = request.messages[-1].content

    matches = []

    greetings = {
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    }

    

    if latest_message.lower() in greetings:
        return ChatResponse(
            reply=(
                "Hello! I'm your SHL AI Assessment Assistant.\n\n"
                "Tell me the role you're hiring for.\n\n"
                "Examples:\n"
                "• Java Backend Developer\n"
                "• Python Data Scientist\n"
                "• Sales Manager"
            ),
            recommendations=[],
            end_of_conversation=False
        )
    
    compare_words = [
        "compare",
        "difference",
        "vs",
        "versus",
        "better"
    ]

    is_compare = any(
        word in latest_message.lower()
        for word in compare_words
    )


    if is_compare:

        search_query = extract_search_query(latest_message)

        keywords = [
            keyword.strip()
            for keyword in search_query.split(",")
        ]

        matches = search_catalog(keywords)

        if len(matches) < 2:
            return ChatResponse(
                reply="I couldn't find two assessments to compare.",
                recommendations=[],
                end_of_conversation=False
            )

        reply = compare_assessments(
            matches[0],
            matches[1]
        )

        recommendations = [
            Recommendation(
                name=matches[0]["name"],
                url=matches[0]["link"],
                test_type=", ".join(matches[0]["keys"])
            ),
            Recommendation(
                name=matches[1]["name"],
                url=matches[1]["link"],
                test_type=", ".join(matches[1]["keys"])
            )
        ]

        return ChatResponse(
            reply=reply,
            recommendations=recommendations,
            end_of_conversation=False
        )
    
    

    

    refinement_words = [
        "only",
        "remote",
        "adaptive"
    ]

    if (
        conversation_state["last_matches"]
        and any(word in latest_message.lower() for word in refinement_words)
    ):

        matches = conversation_state["last_matches"]

        # Filter remote assessments
        if "remote" in latest_message.lower():
            matches = [
                m for m in matches
                if m.get("remote", "").lower() == "yes"
            ]

            print("\n===== Remote Filter Applied =====")
            for m in matches:
                print(m["name"], "-", m.get("remote"))

        # Filter adaptive assessments
        if "adaptive" in latest_message.lower():
            matches = [
                m for m in matches
                if m.get("adaptive", "").lower() == "yes"
            ]

            print("\n===== Adaptive Filter Applied =====")
            for m in matches:
                print(m["name"], "-", m.get("adaptive"))



    else:

        search_query = extract_search_query(latest_message)

        keywords = [
            keyword.strip()
            for keyword in search_query.split(",")
        ]

        matches = search_catalog(keywords)[:7]

        conversation_state["last_query"] = latest_message
        conversation_state["last_matches"] = matches

    if not matches:
        return ChatResponse(
            reply="I couldn't find any matching SHL assessments.",
            recommendations=[],
            end_of_conversation=False
        )

    recommendations = []

    for assessment in matches:
        recommendations.append(
            Recommendation(
                name=assessment["name"],
                url=assessment["link"],
                test_type=", ".join(assessment["keys"])
            )
        )

    try:
        reply = generate_response(latest_message, matches)
    except Exception as e:
        print("Gemini Error:", e)
        reply = "Here are the best matching SHL assessments."

    return ChatResponse(
        reply=reply,
        recommendations=recommendations,
        end_of_conversation=False
    )

   
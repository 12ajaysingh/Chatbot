from fastapi import FastAPI
from models.chat import ChatRequest, ChatResponse,Recommendation
from fastapi.middleware.cors import CORSMiddleware
from service.catalog_service import search_catalog
from dotenv import load_dotenv
from service.ai_service import generate_response,extract_search_query

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
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
            "Tell me the role you're hiring for, the required skills, or the experience level, "
            "and I'll recommend the best SHL assessments.\n\n"
            "Examples:\n"
            "• Java Backend Developer\n"
            "• Python Data Scientist\n"
            "• Sales Manager\n"
            "• Graduate Software Engineer"
        ),
        recommendations=[],
        end_of_conversation=False
    )

    print("User Query:", latest_message)

    search_query = extract_search_query(latest_message)

    print("Extracted Keywords:", search_query)

    keywords = [
        keyword.strip()
        for keyword in search_query.split(",")
    ]

    print("Keyword List:", keywords)

    matches = search_catalog(keywords)[:7]
    if not matches:
        return ChatResponse(
        reply=(
            "I couldn't find any matching SHL assessments.\n\n"
            "Could you tell me:\n"
            "• The job role\n"
            "• Required skills\n"
            "• Experience level"
        ),
        recommendations=[],
        end_of_conversation=False
    )

    print("Matches Found:", len(matches))

    recommendations = []

    for assessment in matches:

        print(assessment["name"])

        recommendations.append(
            Recommendation(
                name=assessment["name"],
                url=assessment["link"],
                test_type=", ".join(assessment["keys"])
            )
        )

    try:
        reply = generate_response(
        latest_message,
        matches
    )
    except Exception as e:
        print("Gemini Error:", e)

        reply = (
            "I found the following SHL assessments for your request. "
            "The AI explanation is temporarily unavailable because the Gemini API quota has been exceeded."
    )

    return ChatResponse(
        reply=reply,
        recommendations=recommendations,
        end_of_conversation=False
    )
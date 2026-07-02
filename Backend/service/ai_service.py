import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API Key Loaded:", api_key is not None)

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def test_gemini():
    response = model.generate_content("Say Hello")
    return response.text

def generate_response(user_query, assessments):

    catalog_text = ""

    for i, assessment in enumerate(assessments, start=1):
        catalog_text += f"""
Assessment {i}

Name: {assessment['name']}

Description: {assessment['description']}

URL: {assessment['link']}

Categories: {', '.join(assessment['keys'])}

------------------------
"""

    prompt = f"""
You are an SHL Assessment Recommendation Assistant.

User request:
{user_query}

Matching SHL assessments:
{catalog_text}

Rules:

- Recommend EXACTLY the THREE best assessments.
- Use ONLY the assessments provided above.
- Never invent assessment names.
- Explain why each assessment matches the user's requirement.
- Mention the SHL URL for every recommendation.
- Be concise and professional.
- Do not recommend assessments outside the provided list.
"""

    response = model.generate_content(prompt)

    return response.text

def extract_search_query(user_query):

    prompt = f"""
Extract only the important skills, technologies and roles.

Return ONLY comma-separated keywords.

User:
{user_query}
"""

    try:
        response = model.generate_content(prompt)

        if (
            response.candidates
            and response.candidates[0].content.parts
        ):
            return response.candidates[0].content.parts[0].text.strip()

    except Exception as e:
        print(e)

    return user_query

    
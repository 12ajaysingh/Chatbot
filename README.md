# 🤖 SHL AI Assessment Recommendation System

An AI-powered chatbot that recommends the most relevant SHL assessments based on a hiring requirement or job description.

The application uses **React**, **FastAPI**, **Google Gemini**, and a locally indexed SHL assessment catalog to provide intelligent assessment recommendations.

---

# Features

- AI-powered hiring assistant
- SHL assessment recommendations
- Natural language query support
- Keyword extraction using Gemini
- Intelligent catalog search
- FastAPI REST API
- React-based chat interface
- Responsive UI
- Recommendation cards with direct SHL links
- Graceful fallback if AI is unavailable

---

# Tech Stack

## Frontend

- React
- Vite
- JavaScript
- CSS

## Backend

- FastAPI
- Python
- Google Gemini API
- Pydantic

---

# Project Structure

```
Chat-bot
│
├── Backend
│   ├── data
│   ├── models
│   ├── service
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── Frontend
│   ├── src
│   ├── public
│   └── package.json
│
└── README.md
```

---

# Installation

## Clone the repository

```bash
git clone <your-github-repository>
```

---

## Backend Setup

Navigate to the backend folder

```bash
cd Backend
```

Create virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Run the server

```bash
uvicorn main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

Navigate to frontend

```bash
cd Frontend
```

Install dependencies

```bash
npm install
```

Create a `.env`

```env
VITE_API_URL=http://127.0.0.1:8000
```

Run

```bash
npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# Example Queries

- Java Backend Developer
- Python Data Scientist
- Sales Manager
- Graduate Software Engineer
- React Developer
- Need a Java developer with Spring Boot experience
- Looking for a Data Analyst

---

# System Workflow

```
User Query
      │
      ▼
Gemini extracts keywords
      │
      ▼
SHL Catalog Search
      │
      ▼
Top Matching Assessments
      │
      ▼
Gemini generates explanation
      │
      ▼
Frontend displays recommendations
```

---

# 📡 API

## POST `/chat`

Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Java Backend Developer"
    }
  ]
}
```

Response

```json
{
  "reply": "Recommended assessments...",
  "recommendations": [
    {
      "name": "Core Java (Advanced)",
      "url": "...",
      "test_type": "Knowledge & Skills"
    }
  ],
  "end_of_conversation": false
}
```

---

# Screenshots

Add screenshots of:

- Home Page
- Chat Interface
- Assessment Recommendations
- Swagger API

---

# Future Improvements

- Conversation memory
- Better semantic search
- Vector database integration
- Multi-turn conversations
- Authentication
- Cloud deployment
- Assessment filtering by duration and job level

---

# Author

**Ajay Singh**

GitHub:
https://github.com/12ajaysingh

---

# License

This project is developed for learning and assessment purposes.
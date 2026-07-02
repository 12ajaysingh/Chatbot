# SHL AI Assessment Recommendation System - Evaluation

## Evaluation Method

The system was evaluated using representative hiring queries covering different job roles, technologies, and comparison requests.

Each response was evaluated on the following metrics:

- Retrieval Quality
- Recommendation Relevance
- Groundedness
- Response Accuracy
- Conversation Handling

## Test Cases

| User Query | Expected Behaviour | Result |
|------------|--------------------|--------|
| Java Backend Developer | Recommend Java-related SHL assessments | ✅ Passed |
| Python Data Scientist | Recommend Python-related assessments | ✅ Passed |
| Sales Manager | Recommend sales assessments | ✅ Passed |
| Compare Automata Front End and Automata Fix | Compare two assessments | ✅ Passed |
| Hello | Display greeting | ✅ Passed |
| Unknown Role | Ask clarifying questions | ✅ Passed |

## Retrieval Quality

The system extracts important keywords from the user's query using Gemini.

These keywords are matched against the SHL catalog using:

- Assessment Name
- Description
- Categories

The highest-scoring assessments are returned.

## Recommendation Relevance

Recommendations are generated only from assessments retrieved from the SHL catalog.

Gemini explains why each assessment matches the user's hiring requirements.

No assessments outside the catalog are recommended.

## Groundedness

The LLM receives only the retrieved SHL catalog entries as context.

Responses are generated exclusively from this retrieved information.

The prompt explicitly instructs Gemini not to invent assessment names or details.

## Response Accuracy

The generated recommendations were manually verified using multiple job-role queries.

Responses were checked to ensure:

- Relevant assessments were recommended.
- Assessment names existed in the SHL catalog.
- URLs matched the official SHL product pages.
- Explanations were consistent with the catalog descriptions.


## Limitations

- Recommendation quality depends on keyword extraction.
- Free Gemini API quotas may temporarily disable AI-generated explanations.
- Conversation memory is maintained only during the current backend session.

## Conclusion

The evaluation demonstrates that the system successfully retrieves relevant SHL assessments, generates grounded recommendations, supports assessment comparison, and handles common recruitment scenarios effectively.
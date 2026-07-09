import json
from services.gemini_service import model


def evaluate_reply(email, generated_reply):
    prompt = f"""
You are an expert AI evaluator.

Your task is to evaluate how well the generated email reply responds to the original email.

Original Email:
{email}

Generated Reply:
{generated_reply}

Evaluate the reply using the following criteria:

1. Accuracy (0-100)
- Does the reply correctly answer the sender's request?
- Does it avoid incorrect information?
- Scoring Guide:
  - 90-100 = Excellent
  - 80-89 = Good
  - 60-79 = Fair
  - Below 60 = Poor

2. Tone
Describe the tone in one sentence.

3. Completeness
State whether the reply addresses all important points.

4. Reason
Explain why you assigned the score.

5. Suggestions
Suggest improvements if necessary.

Return ONLY valid JSON in the following format:

{{
    "accuracy": 95,
    "tone": "Professional",
    "completeness": "Complete",
    "reason": "The reply fully addresses the user's request.",
    "suggestions": "No major improvements needed."
}}
"""

    try:
        response = model.generate_content(prompt)

        cleaned_response = (
            response.text.replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(cleaned_response)

    except Exception as e:
        return {
            "accuracy": 0,
            "tone": "Error",
            "completeness": "Error",
            "reason": str(e),
            "suggestions": "Try again."
        }

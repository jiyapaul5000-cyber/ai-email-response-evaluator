import json
from services.gemini_service import model


def evaluate_reply(email, generated_reply):
    prompt = f"""
You are an AI evaluator.

Evaluate the generated email reply.

Original Email:
{email}

Generated Reply:
{generated_reply}

Return ONLY valid JSON.

Format:

{{
    "accuracy": 0,
    "tone": "",
    "completeness": "",
    "reason": "",
    "suggestions": ""
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
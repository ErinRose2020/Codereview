import anthropic
import json

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

def analyze_with_ai(code: str) -> list[dict]:
    prompt = f"""You are a code reviewer. Analyze the following Python code and return ONLY a JSON array of issues.
Each issue must have: "type" (bug/style/security/performance), "severity" (low/medium/high), and "message".
Return an empty array if there are no issues. Do not include any text outside the JSON.

Code:
{code}
"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.content[0].text.strip()
    raw = raw.removeprefix("```json").removeprefix("```").removesuffix("```").strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return [{"type": "meta", "severity": "low", "message": "AI review failed to parse response"}]
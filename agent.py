import requests
from email_tool import check_emails

OLLAMA_URL = "http://localhost:11434/api/generate"

def run_agent():
    emails = check_emails()

    if not emails:
        print("No new emails")
        return

    prompt = f"""
You are a smart assistant.

Emails:
{emails}

Tasks:
1. Summarize
2. Mark important emails
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "qwen3.5:4b",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"]

    print("\n=== AI RESPONSE ===")
    print(result)
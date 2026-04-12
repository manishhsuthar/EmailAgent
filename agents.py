from langchain.llms import Ollama
from email_tool import check_emails
import os

llm = Ollama(model="qwen3.5:4b")


def notify(msg):
    os.system(f'notify-send "AI Agent" "{msg}"')

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

    response = llm.invoke(prompt)

    print("\n=== AI RESPONSE ===")
    print(response)
import schedule
import time
from agent import run_agent

def safe_run_agent():
    try:
        run_agent()
    except Exception as e:
        # Keep the service alive even if email/LLM/network is temporarily unavailable.
        print(f"Agent run failed: {e}")

schedule.every(10).minutes.do(safe_run_agent)

print("AI Agent Started...")

safe_run_agent()

while True:
    schedule.run_pending()
    time.sleep(1)

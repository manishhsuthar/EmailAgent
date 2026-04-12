import schedule
import time
from agent import run_agent

schedule.every(10).minutes.do(run_agent)

print("AI Agent Started...")

run_agent()  # Run immediately on start

while True:
    schedule.run_pending()
    time.sleep(1)
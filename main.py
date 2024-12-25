from core.agent import Agent
from utils.logger import Logger

if __name__ == "__main__":
    Logger.log("Initializing Arxen AI...")
    agent = Agent(name="Arxen")
    agent.perform_task()
    Logger.log("Arxen AI execution complete.")

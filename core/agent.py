from core.behavior import Behavior

class Agent:
    def __init__(self, name):
        self.name = name
        self.behavior = Behavior()

    def perform_task(self):
        print(f"{self.name} is analyzing the environment...")
        self.behavior.adapt_behavior()

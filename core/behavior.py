class Behavior:
    def __init__(self):
        self.state = "Idle"

    def adapt_behavior(self):
        print("Adapting behavior based on environment...")
        self.state = "Active"
        print(f"Current state: {self.state}")

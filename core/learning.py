class Learning:
    def __init__(self):
        self.knowledge = []

    def reinforce(self, data):
        print(f"Learning from data: {data}")
        self.knowledge.append(data)
        print(f"Updated knowledge base: {self.knowledge}")

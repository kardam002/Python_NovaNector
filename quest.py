# quest.py
class Quest:
    def __init__(self, name, description, reward):
        self.name = name
        self.description = description
        self.reward = reward

    def __str__(self):
        return f"Quest: {self.name}, Reward: {self.reward}"

# Define more methods for quest actions

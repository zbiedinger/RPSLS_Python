import Gesture


class Paper(Gesture):
    def __init__(self, name, weakness):
        self.name = "paper"
        self.weakness = ["scissors", "lizard"]

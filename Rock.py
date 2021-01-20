import Gesture


class Rock(Gesture):
    def __init__(self, name, weakness):
        self.name = "rock"
        self.weakness = ["paper", "spock"]

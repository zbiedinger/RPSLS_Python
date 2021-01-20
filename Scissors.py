import Gesture


class Scissors(Gesture):
    def __init__(self, name, weakness):
        self.name = "scissors"
        self.weakness = ["rock", "spock"]

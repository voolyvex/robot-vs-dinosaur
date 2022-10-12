
from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()

    def run_game(self):
        pass

    def display_welcome(self):
        print("Welcome to the battlefield")

    def battle_phase(self):
        pass

    def display_winner(self):
        print("The winner is ______")

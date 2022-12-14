
from dinosaur import Dinosaur
from robot import Robot
from slow_print import slow_print as s


class Battlefield:
    def __init__(self):
        self.robot = Robot("Robbie", 90)
        self.dinosaur = Dinosaur("Pterodactyl", 20)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()

    def display_welcome(self):
        s("\nWelcome to the battlefield of Robot vs Dinosaur!\nPrepare for battle")

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health <= 0:
                s(f"{self.dinosaur.name} is dead")
            else:
                s(f"Health of {self.dinosaur.name} is now {self.dinosaur.health}")
                print()
            if self.robot.health > 0 and self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)
                if self.robot.health < 0:
                    s(f"{self.robot.name} is dead")
                else:
                    s(f"Health of {self.robot.name} is now {self.robot.health}")
                    print()
        self.display_winner()

    def display_winner(self):
        s("Victory acheived!")
        if self.robot.health <= 0:
            s(f"The winner is dinosaur {self.dinosaur.name}!\n")
        else:
            s(f"The winner is robot {self.robot.name}!\n")

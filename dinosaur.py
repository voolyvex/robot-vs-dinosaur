from robot import Robot

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        print(f"\nDinosaur {self.name} attacks!")
        robot.health -= self.attack_power
        print(f"Robot {robot.name} is damaged by {self.attack_power} points")
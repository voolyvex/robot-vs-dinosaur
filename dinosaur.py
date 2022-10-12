from robot import Robot


class Dinosaur:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.attack_power = 0

    def attack(self):
        Robot.health -= self.attack_power
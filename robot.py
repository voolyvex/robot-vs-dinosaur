from weapon import Weapon
from slow_print import slow_print as s


class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.active_weapon = Weapon("Laser", 22)

    def attack(self, dinosaur):
        s(f"\nRobot {self.name} attacks with {self.active_weapon.name}!")
        dinosaur.health -= self.active_weapon.attack_power
        s(f"Dinosaur {dinosaur.name} is damaged by {self.active_weapon.attack_power} points")

  
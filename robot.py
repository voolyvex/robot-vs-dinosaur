from weapon import Weapon


class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.active_weapon = Weapon("Laser", 22)

    def attack(self, dinosaur):
        print(f"\nRobot {self.name} attacks with {self.active_weapon.name}!")
        dinosaur.health -= self.active_weapon.attack_power
        print(f"Dinosaur {dinosaur.name} is damaged -{self.active_weapon.attack_power} points")

  
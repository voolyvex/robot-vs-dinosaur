from weapon import Weapon

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.active_weapon = Weapon("Laser", 15)

    def attack(self, dinosaur):
        pass

  
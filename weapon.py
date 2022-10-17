import random
class Weapon:
    def __init__(self, name, base_attack_power):
        self.name = name
        self.attack_power = base_attack_power

    # def attack_variance(self, base_attack_power):
    #     variance = random.randint(-10, 10)
    #     base_attack_power += variance
    #     return base_attack_power
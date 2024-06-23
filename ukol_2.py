import random


class Fighter:

    def __init__(self, name, health, attack_min, attack_max, defense):
        self.name = name
        self.health = health
        self.attack_min = attack_min
        self.attack_max = attack_max
        self.defense = defense
        """base definition"""

    def attack_to(self, target):
        attack_range = random.randint(self.attack_min, self.attack_max)
        """add range of attack"""

        crit_attack = random.random() < 0.05
        if crit_attack:
            attack_range *= 3
            print(f"{self.name} dealt crtitical damage")
            """add random critical attack - 5% chance to tripple damage"""

        caused_damage = attack_range - target.defense
        caused_damage = max(caused_damage, 0)
        target.receive_attack(caused_damage)
        """defines damage caused
        sets damage > 0
        attacking the target"""

    def receive_attack(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        """decreases health by damage amount"""

    def alive(self):
        return self.health > 0
        """Fighter is alive"""

    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Attack: {self.attack_min} - {self.attack_max}, Defense: {self.defense}"
        """return stats of fighter"""


# make fighters
fighter1 = Fighter("První", 100, 10, 15, 5)
fighter2 = Fighter("Druhý", 100, 7, 20, 6)

round_number = 1

while fighter1.alive() and fighter2.alive():
    print(f"Round {round_number}:")
    print(fighter1)
    print(fighter2)
    """round number anr printing fighters stats"""
    fighter1.attack_to(fighter2)
    if fighter2.alive():
        fighter2.attack_to(fighter1)
    """fighters attacking"""
    round_number += 1
    """next round number adder"""

print("Final stats:")
print(fighter1)
print(fighter2)

if fighter1.alive():
    print(f"{fighter1.name} wins!")
elif fighter2.alive():
    print(f"{fighter2.name} wins!")
else:
    print("DRAW!")


class Fighter:

    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        """base definition"""

    def attack_to(self, target):
        caused_damage = self.attack - target.defense
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
        return f"Name: {self.name}, Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}"
        """return stats of fighter"""


# make fighters
fighter1 = Fighter("První", 100, 20, 15)
fighter2 = Fighter("Druhý", 100, 25, 10)


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


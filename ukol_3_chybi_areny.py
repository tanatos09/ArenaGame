import random


class Fighter:
    # BASDE DEFINITION
    def __init__(self, name, health, attack_min, attack_max, defense):
        self.name = name
        self.health = health
        self.attack_min = attack_min
        self.attack_max = attack_max
        self.defense = defense

    # ADD RANGE OF ATTACK AND CRITICAL ATTACK
    def attack_to(self, target, crit_chance=0.05):
        attack_range = random.randint(self.attack_min, self.attack_max)

        crit_attack = random.random() < crit_chance
        if crit_attack:
            attack_range *= 3
            print(f"{self.name} dealt crtitical damage")

        # DEFINES CAUSED DAMAGE, SET DEMAGE > 0, AND ATTACKING THE TARGET
        caused_damage = attack_range - target.defense
        caused_damage = max(caused_damage, 0)
        target.receive_attack(caused_damage)

    # DECREASE HEALTH BY DAMAGE AMOUNT
    def receive_attack(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    # HEALING
    def heal(self, amount):
        self.healh += amount

    # FIGHTER IS ALIVE - CHECKING
    def alive(self):
        return self.health > 0

    # FIGHTER STATS
    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Attack: {self.attack_min} - {self.attack_max}, Defense: {self.defense}"


class Arena:
    # BASE DEFINITION
    def __init__(self, name):
        self.name = name

    # ARENA EFFECT
    def arena_effects(self, fighters):
        for fighter in fighters:
            if random.random() < 0.1:  # 10% chance for trap
                print(f"{fighter.name} step into the trap!")
                return fighter  # return trapped fighter back to fight
        return None  # nobody step to the trap


# MAKEING FIGHTERS
fighter1 = Fighter("Guardian", 100, 10, 15, 5)
fighter2 = Fighter("Champion", 100, 7, 20, 6)

# MAKING ARENA
arena = Arena("None")

round_number = 1
while fighter1.alive() and fighter2.alive():
    print(f"Round {round_number}:")
    if round_number == 1:
        print(fighter1)
        print(fighter2)
    # printing stats on start fight
    else:
        print(f"{fighter1.name}, {fighter1.health} HP")
        print(f"{fighter2.name}, {fighter2.health} HP")
    # printing name and HP during fight

    skipped_fighter = arena.arena_effects([fighter1, fighter2])
    # arena effects aplication

    if skipped_fighter != fighter1:
        fighter1.attack_to(fighter2)
    if skipped_fighter != fighter2 and fighter2.alive():
        fighter2.attack_to(fighter1)
    # fight

    round_number += 1
    # next round number adder

print("Final stats:")
print(fighter1)
print(fighter2)
# printing final stats

if fighter1.alive():
    print(f"{fighter1.name} wins!")
elif fighter2.alive():
    print(f"{fighter2.name} wins!")
else:
    print("DRAW!")
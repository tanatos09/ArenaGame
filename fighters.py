import random
class Fighter:
    # BASDE DEFINITION
    def __init__(self, name, health, attack_min, attack_max, defense):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_min = attack_min
        self.attack_max = attack_max
        self.defense = defense

    # ADD RANGE OF ATTACK AND CRITICAL ATTACK
    def attack_to(self, target, crit_chance=0.05):
        attack_range = random.randint(self.attack_min, self.attack_max)

        crit_attack = random.random() < crit_chance
        if crit_attack:
            attack_range *= 3
            print(f"{self.name} dealt crtitical damage!")

        # DEFINES CAUSED DAMAGE, SET DEMAGE > 0, AND ATTACKING THE TARGET
        caused_damage = attack_range - target.defense
        caused_damage = max(caused_damage, 0)
        target.receive_attack(caused_damage)

    # DECREASE HEALTH BY DAMAGE AMOUNT
    def receive_attack(self, damage):
        self.health -= damage
        self.health = max(self.health, 0)
    # HEALING
    def heal(self, amount):
        self.health += amount
        self.health = min(self.health, self.max_health)

    # FIGHTER IS ALIVE - CHECKING
    def alive(self):
        return self.health > 0

    # FIGHTER STATS
    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Attack: {self.attack_min} - {self.attack_max}, Defense: {self.defense}"

class Healer(Fighter):
    def __init__(self, name):
        super().__init__(name, 70, 6, 10, 5)
        self.healing_self = 5 #healing self every round

    def heal(self):
        if random.random() <0.1: # 10% to heal self
            self.health = self.max_health
            print(f"{self.name} is fully healed!")

    def heal_self(self):
        self.health += self.healing_self

class Rager(Fighter):
    def __init__(self, name):
        super().__init__(name, 100, 15, 20, 3)

    def attack_to(self, target, crit_chance=0.15):
        attack_range = random.randint(self.attack_min, self.attack_max)
       #TODO ################################################dokončit postavu RAGER - crit 15%, při critu se sníží obrana a zdraví####################################



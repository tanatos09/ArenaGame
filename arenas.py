import random
class Arena:
    # BASE DEFINITION
    def __init__(self, name):
        self.name = name
        self.sandstorm = False #sandstorm no activated
        self.overheated = None #overheating no activated

    # ARENA EFFECT
    def arena_effects(self, fighters):
        for fighter in fighters:
            if random.random() < 0.1:  # 10% chance for trap
                print(f"{fighter.name} stepped into the trap!")
                return fighter  # return trapped fighter back to fight
        return None  # nobody step to the trap

class Forest(Arena):
    def arena_effects(self, fighters):
        for fighter in fighters:
            if random.random() < 0.15: #15% chance to heal
                print(f"{fighter.name} was healed by magic of the forest")
                fighter.heal(20)
        return None

class Desert(Arena):
    def arena_effects(self, fighters):
        if not self.sandstorm and random.random() < 0.05: #5% chance for sandstorm
            print("SANDSTORM!")
            self.sandstorm = True #
            for fighter in fighters:
                fighter.defense = 0 #set defense 0 for all fighters

        for fighter in fighters:
            if fighter == self.overheated:
                self.apply_overheating(fighter)
                break #stop checking overgeating

            elif self.overheated is None and random.random() < 0.1:
                print(f"{fighter.name} is overheated!")
                self.overheated = fighter #fighter is now overheated
                self.apply_overheating(fighter)
                break

    def apply_overheating(self, fighter):
        fighter.health -= 5 #reduce health -5 when fighter is overheated
        print(f"{fighter.name} is overheated! Health reduced to {fighter.health}")
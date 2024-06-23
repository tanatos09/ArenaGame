import random
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




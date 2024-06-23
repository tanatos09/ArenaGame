from arenas import Arena
from fighters import Fighter

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
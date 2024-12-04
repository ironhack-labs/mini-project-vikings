from vikingsClasses import Viking, Saxon, War
import random

def create_viking_team(names, count):
    """Create a list of Viking warriors with random health and strength."""
    vikings = []
    for _ in range(count):
        name = random.choice(names)
        health = random.randint(100, 200)
        strength = random.randint(30, 50)
        vikings.append(Viking(name, health, strength))
    return vikings

def create_saxon_team(count):
    """Create a list of Saxon warriors with random health and strength."""
    saxons = []
    for _ in range(count):
        health = random.randint(80, 150)
        strength = random.randint(25, 40)
        saxons.append(Saxon(health, strength))
    return saxons

def run_battle(war):
    """Run the battle between Vikings and Saxons."""
    round_number = 1
    while war.vikingArmy and war.saxonArmy:
        print(f"--- Round {round_number} ---")
        if random.choice([True, False]):
            result = war.vikingAttack()
            print(f"Viking attacks: {result}")
        else:
            result = war.saxonAttack()
            print(f"Saxon attacks: {result}")

        round_number += 1

        if round_number % 3 == 0:
            print(war.showStatus())

    print("\n--- Final Status ---")
    print(war.showStatus())

def main():
    print("Welcome to the Viking vs. Saxon Battle Simulator!")

    # Step 1: Create the teams
    viking_names = ["Wasif", "Larry", "Cindy", "Ignacio", "Montassar"]
    viking_count = int(input("Enter the number of Vikings: "))
    saxon_count = int(input("Enter the number of Saxons: "))

    vikings = create_viking_team(viking_names, viking_count)
    saxons = create_saxon_team(saxon_count)

    # Step 2: Set up the war
    war = War()
    for viking in vikings:
        war.addViking(viking)
    for saxon in saxons:
        war.addSaxon(saxon)

    print("\nThe armies are ready!")
    print(f"Viking army: {len(war.vikingArmy)} warriors")
    print(f"Saxon army: {len(war.saxonArmy)} warriors\n")

    # Step 3: Run the battle
    run_battle(war)

if __name__ == "__main__":
    main()

import random

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

# Example usage:
# Create a Soldier instance
soldier1 = Soldier(100, 20)

# Call the attack method
print(soldier1.attack())  # Output: 20

# Call the receiveDamage method
soldier1.receiveDamage(10)
print(soldier1.health)  # Output: 90



class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)  # Call the super class (Soldier) constructor
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Example usage:
# Create a Viking instance
viking1 = Viking("Ragnar", 100, 30)

# Call the attack method (inherited from Soldier)
print(viking1.attack())  # Output: 30

# Call the receiveDamage method
print(viking1.receiveDamage(20))  # Output: Ragnar has received 20 points of damage

# Call the battleCry method
print(viking1.battleCry())  # Output: Odin Owns You All!



class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)  # Call the super class (Soldier) constructor

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# Example usage:
# Create a Saxon instance
saxon1 = Saxon(80, 25)

# Call the attack method (inherited from Soldier)
print(saxon1.attack())  # Output: 25

# Call the receiveDamage method
print(saxon1.receiveDamage(30))  # Output: A Saxon has received 30 points of damage





class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        if self.saxonArmy:
            random_saxon = random.choice(self.saxonArmy)
            random_viking = random.choice(self.vikingArmy)
            result = random_saxon.receiveDamage(random_viking.strength)
            if random_saxon.health <= 0:
                self.saxonArmy.remove(random_saxon)
            return result

    def saxonAttack(self):
        if self.vikingArmy:
            random_viking = random.choice(self.vikingArmy)
            random_saxon = random.choice(self.saxonArmy)
            result = random_viking.receiveDamage(random_saxon.strength)
            if random_viking.health <= 0:
                self.vikingArmy.remove(random_viking)
            return result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

# Example usage:
# Create a War instance and add soldiers
war = War()
war.addViking(Viking("Ragnar", 100, 30))
war.addSaxon(Saxon(80, 25))

# Perform attacks and display the status
print(war.vikingAttack())  # Attack a Saxon
print(war.saxonAttack())  # Attack a Viking
print(war.showStatus())  # Output the current status of the war





# game.py

from vikingsClasses import Soldier, Viking, Saxon, War
import random

def create_teams(num_vikings, num_saxons):
    """Create Viking and Saxon teams with random names"""
    viking_names = ["Erik", "Leif", "Bjorn", "Ingrid", "Freja"]
    saxon_names = ["Osgar", "Eadric", "Baldwin", "Aelfric", "Lufa"]

    viking_team = [Viking(random.choice(viking_names), random.randint(80, 120), random.randint(15, 25)) for _ in range(num_vikings)]
    saxon_team = [Saxon(random.choice(saxon_names), random.randint(80, 120), random.randint(15, 25)) for _ in range(num_saxons)]

    return viking_team, saxon_team

def run_battle(viking_team, saxon_team):
    """Run the battle simulation"""
    war = War()
    for viking in viking_team:
        war.addViking(viking)
    for saxon in saxon_team:
        war.addSaxon(saxon)

    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        if random.choice([True, False]):  # Randomly selecting the attacker
            print(war.vikingAttack())
        else:
            print(war.saxonAttack())

    print(war.showStatus())

def main():
    viking_team, saxon_team = create_teams(5, 5)  # Create teams with 5 Vikings and 5 Saxons
    run_battle(viking_team, saxon_team)

if __name__ == "__main__":
    main()
import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength



    def receiveDamage(self, damage):
        self.health -= damage
        
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name


    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = saxon.receiveDamage(viking.attack())
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result
    
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = viking.receiveDamage(saxon.attack())
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


def main():
    print("Welcome to the Viking vs. Saxon Battle Simulator!")

    # Step 1: Create the teams
    viking_names = ["Ragnar", "Lagertha", "Bjorn", "Floki", "Ivar"]
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

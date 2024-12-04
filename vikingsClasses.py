import random

# Soldier class definition
class Soldier:
    def __init__(self, health, strength):
        # Constructor to initialize health and strength of the soldier
        self.health = health
        self.strength = strength

    def attack(self):
        # Method to return the soldier's attack strength
        return self.strength

    def receiveDamage(self, damage):
        # Method to reduce the soldier's health by the given damage
        self.health -= damage
        # No need to return anything, implicitly returns None

# Saxon class definition, inherits from Soldier
class Saxon(Soldier):
    def __init__(self, health, strength):
        # Constructor to initialize health and strength for Saxon
        super().__init__(health, strength)  # Call the parent constructor to initialize health and strength

    def receiveDamage(self, damage):
        # Saxon-specific method to receive damage
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# Viking class definition, inherits from Soldier
class Viking(Soldier):
    def __init__(self, name, health, strength):
        # Constructor to initialize health and strength for Viking
        super().__init__(health, strength)
        self.name = name  # Vikings have a name

    def receiveDamage(self, damage):
        # Viking-specific method to receive damage
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"

# War class definition
class War:
    def __init__(self):
        self.vikingArmy = []  # Array to store Viking soldiers
        self.saxonArmy = []   # Array to store Saxon soldiers

    def addViking(self, viking):
        # Adds a Viking to the vikingArmy
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        # Adds a Saxon to the saxonArmy
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        # Viking attack: randomly selects a Viking and a Saxon
        if self.saxonArmy:
            viking = random.choice(self.vikingArmy)
            saxon = random.choice(self.saxonArmy)
            result = saxon.receiveDamage(viking.attack())
            # Remove dead Saxon from the army
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)
            return result

    def saxonAttack(self):
        # Saxon attack: randomly selects a Saxon and a Viking
        if self.vikingArmy:
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
            result = viking.receiveDamage(saxon.attack())
            # Remove dead Viking from the army
            if viking.health <= 0:
                self.vikingArmy.remove(viking)
            return result

    def showStatus(self):
        # Displays the status of the war
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

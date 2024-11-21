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
            return f"A Saxon has died in combat"

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
        if not self.saxonArmy:
            return None
        saxon_left = random.randint(0, len(self.saxonArmy) - 1)
        saxon = self.saxonArmy[saxon_left]
        damage = random.choice([viking.strength for viking in self.vikingArmy])
        result = saxon.receiveDamage(damage)
        self.saxonArmy = [sax for sax in self.saxonArmy if sax.health > 0]
        return result
    
    def saxonAttack(self):
        if not self.vikingArmy:
            return None
        viking_index = random.randint(0, len(self.vikingArmy) - 1)
        viking = self.vikingArmy[viking_index]
        damage = random.choice([saxon.strength for saxon in self.saxonArmy])
        result = viking.receiveDamage(damage)
        self.vikingArmy = [vik for vik in self.vikingArmy if vik.health > 0]
        return result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        


    pass



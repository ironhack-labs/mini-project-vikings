import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength
    
    def attack(self):
        # your code here
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage

        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


# War

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy  = []

    def addViking(self, viking : Viking):
        # your code here
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon : Saxon):
        # your code here
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        # your code here
        if(len(self.vikingArmy)>0):
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
            result = saxon.receiveDamage(viking.strength)

            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)

            return result
        return "No vikings left to attack the Saxons."
    
    def saxonAttack(self):
        # your code here
        if(len(self.saxonArmy)>0):
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
            result = viking.receiveDamage(saxon.strength)

            if viking.health <= 0:
                self.vikingArmy.remove(viking)

            return result
        return  "No Saxons left to attack the vikings."

    def showStatus(self):
        # your code here
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        
        else: #if (len(self.saxonArmy) >= 1) and (len(self.vikingArmy) >= 1):
            return "Vikings and Saxons are still in the thick of battle."

import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
        # your code here
    
    def attack(self):
        # your code here
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        self.health-=damage
        

    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength)
        self.name=name

    def battleCry(self):
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        self.health-=damage
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
        self.health-=damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        # your code here
        attacking_viking=random.choice(self.vikingArmy)
        defending_saxon=random.choice(self.saxonArmy)

        fight=defending_saxon.receiveDamage(attacking_viking.strength)

        if defending_saxon.health <= 0:
            self.saxonArmy.remove(defending_saxon)

        return fight
    
    def saxonAttack(self):
        # your code here
        attacking_saxon=random.choice(self.saxonArmy)
        defending_viking=random.choice(self.vikingArmy)

        fight=defending_viking.receiveDamage(attacking_saxon.strength)

        if defending_viking.health <= 0:
            self.vikingArmy.remove(defending_viking)

        return fight

    def showStatus(self):
        # your code here
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    pass



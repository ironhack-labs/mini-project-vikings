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
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
       self.health -= damage

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        
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
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        damage_result = saxon.receiveDamage(viking.strength)

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        
        return damage_result
 
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)

        damage_result = viking.receiveDamage(saxon.strength)

        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        
        return damage_result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
        return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
        return "Saxons have fought for their lives and survive another day..."
        else:
        return "Vikings and Saxons are still in the thick of battle."

    pass



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
        self.name = name
        self.health = health
        self.strength = strength


    def battleCry(self):
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage

        if (self.health > 0):
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage

        if (self.health > 0):
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# Davicente
'''
vikingAttack
should make a Saxon receiveDamage() equal to the strength of a Viking
should remove dead saxons from the army
should return result of calling receiveDamage() of a Saxon with the strength of a Viking

saxonAttck
should make a Viking receiveDamage() equal to the strength of a Saxon
should remove dead vikings from the army
should return result of calling receiveDamage() of a Viking with the strength of a Saxon
'''
class War():
    def __init__(self):
        # your code here
        self.saxonArmy = []
        self.vikingArmy = []

    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        # your code here
        message = self.saxonArmy[0].receiveDamage(self.vikingArmy[0].strength)
        
        if(message == f"A Saxon has died in combat"):
            self.saxonArmy.pop(0)
            
        return message
    
    def saxonAttack(self):
        # your code here
        message = self.vikingArmy[0].receiveDamage(self.saxonArmy[0].strength)
        
        if(message == f"{self.vikingArmy[0].name} has died in act of combat"):
            self.vikingArmy.pop(0)
            
        return message

    def showStatus(self):
        # your code here
        if(bool(self.saxonArmy) and (self.vikingArmy)):
            return "Vikings and Saxons are still in the thick of battle."
        elif(bool(self.saxonArmy)):
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings have won the war of the century!"
            
    pass


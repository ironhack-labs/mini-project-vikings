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
        diff = self.health - damage
        self.health = diff
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        # your code here
        battle_cry = "Odin Owns You All!"
        return battle_cry
    
    def __str__(self):
        return self.name

    def receiveDamage(self, damage):
        # your code here
        diff = self.health - damage
        self.health = diff
        
        if self.health > 0:
            alive = f"{self.name} has received {damage} points of damage"
            return alive
        else:
            dead = f"{self.name} has died in act of combat"
            return dead

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        # your code here
        diff = self.health - damage
        self.health = diff
        if self.health > 0:
            alive = f"A Saxon has received {damage} points of damage"
            return alive
        else:
            dead = f"A Saxon has died in combat"
            return dead

# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        # your code here
        attacker = random.choice(self.vikingArmy)
        defender = random.choice(self.saxonArmy)
        
        result = defender.receiveDamage(attacker.attack())
        
        if defender.health <= 0:
            self.saxonArmy.remove(defender)    
        
        return result
        
    def saxonAttack(self):
        # your code here
        attacker = random.choice(self.saxonArmy)
        defender = random.choice(self.vikingArmy)
        
        result = defender.receiveDamage(attacker.attack())
        
        if defender.health <= 0:
            self.vikingArmy.remove(defender)
        
        return result
            

    def showStatus(self):
        # your code here
        if not self.saxonArmy:
            vikingWin = "Vikings have won the war of the century!"
            return vikingWin
        elif not self.vikingArmy:
            saxonWin = "Saxons have fought for their lives and survive another day..."
            return saxonWin
        else:
            unresolved = "Vikings and Saxons are still in the thick of battle."
            return unresolved
    pass



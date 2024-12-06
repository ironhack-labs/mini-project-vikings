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
        self.health = health
        self.strength = strength
        
    def battleCry(self):        
        return"Odin Owns You All!"
        # your code here
        

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        if self.health <= 0 :
            return f"{self.name} has died in act of combat"
        
        
      
  
  # your code here

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        # your code here
        
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        if self.health <= 0:
            return"A Saxon has died in combat"
        
        # your code here



class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)

        damage = random_viking.strength
        result = random_saxon.receiveDamage(damage)

        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)

        return result

    def saxonAttack(self):
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)

        damage = random_saxon.strength
        result = random_viking.receiveDamage(damage)

        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)

        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."




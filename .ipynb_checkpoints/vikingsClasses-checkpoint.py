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
        self.health = self.health - damage
    

# Viking

class Viking(Soldier):
    
    def __init__(self, name, health, strength):

        #Viking is a child of Soldier Class
        super().__init__(health, strength)
        self.name = name


    def battleCry(self):
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        
        self.health = self.health - damage
        
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name,damage)
        else:
            return "{} has died in act of combat".format(self.name)
            


        

# Saxon

class Saxon(Soldier):
    
    def __init__(self, health, strength):
        #Saxon is also child of Soldier Class
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        # your code here
        self.health = self.health - damage
        
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"
        

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

        if (len(self.saxonArmy) == 0) or (len(self.vikingArmy) == 0):
            
            return "War is Over"
            
        else:
        
            # Calling one saxon and one viking
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
    
            #Damage received by Saxon equal to the strength of the Viking
            result = saxon.receiveDamage(viking.strength)
    
            #Removing dead saxons
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)
    
            return result

    
        
        
    
    def saxonAttack(self):

        if (len(self.saxonArmy) == 0) or (len(self.vikingArmy) == 0):
            
            return "War is Over"
        
        else:

            # Calling one saxon and one viking
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
    
            #Damage received by Viking equal to the strength of the Saxon
            result = viking.receiveDamage(saxon.strength)
    
            #Removing dead vikings
            if viking.health <= 0:
                self.vikingArmy.remove(viking)
    
            return result

    def showStatus(self):
        
        # your code here
        
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."
    pass



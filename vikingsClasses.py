import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here0
        self.health = health # attribute health 
        self.strength = strength # attribute strength 
        
    def attack(self):
        # your code here
        return self.strength
                
    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health < 0:
            self.health = 0
        
    
# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength)
        self.name = name
           
    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
            return(f"{self.name} has received {damage} points of damage")
        else:
            return(f"{self.name} has died in act of combat")
     
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)
        
    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
            return(f"A Saxon has received {damage} points of damage")
        else:
            return(f"A Saxon has died in combat")  
      
# Davicente

class War():
    def __init__(self):
        # your code here
        self.VikingArmy = []
        self.SaxonArmy = []

        
    def addViking(self, viking):
        # your code here
        self.VikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        # your code here
        self.SaxonArmy.append(saxon)
    
    def vikingAttack(self):
        # your code here
        r_saxon = random.choice(self.SaxonArmy)
        r_viking = random.choice(self.VikingArmy)
        result_v_attack = r_saxon.receiveDamage(r_viking.attack())
        if r_saxon.health <= 0:
            self.SaxonArmy.remove(r_saxon)
        return result_v_attack
  
    def saxonAttack(self):
        # your code here
        r_saxon = random.choice(self.SaxonArmy)
        r_viking = random.choice(self.VikingArmy)
        result_s_attack = r_viking.receiveDamage(r_saxon.attack())
        if r_viking.health <= 0:
            self.VikingArmy.remove(r_viking)
        return result_s_attack
 

    def showStatus(self):
        # your code here
        if len(self.SaxonArmy) ==0:   
            return "Vikings have won the war of the century!"
        elif len(self.VikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


    pass




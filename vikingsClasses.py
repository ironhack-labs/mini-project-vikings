import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health,strength)
        self.name = name

    def battleCry(self):
        return 'Odin Owns You All!'

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return self.name + ' has died in act of combat'
        else:
            return self.name + ' has received' + damage + ' points of damage'


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return 'A Saxon has received ' + damage + ' points of damage'
        else:
            return 'A Saxon has died in combat'

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
        selectedViking = random.randrange(len(self.vikingArmy))
        selectedSaxon = random.randrange(len(self.saxonArmy))

        result = self.saxonArmy[selectedSaxon].receiveDamage(self.vikingArmy[selectedViking].attack())

        if result == 'A Saxon has died in combat':
            self.saxonArmy.pop(selectedSaxon)

        return result
        
    
    def saxonAttack(self):
        selectedViking = random.randrange(len(self.vikingArmy))
        selectedSaxon = random.randrange(len(self.saxonArmy))

        result = self.vikingArmy[selectedViking].receiveDamage(self.saxonArmy[selectedSaxon].attack())

        if 'has died in act of combat' in result:
            self.vikingArmy.pop(selectedViking)
            
        return result

    def showStatus(self):
        if len(self.saxonArmy) < 1:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) < 1:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
 



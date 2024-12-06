import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength    
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health-=damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name=name
    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0:
            return f'{self.name} has recieved {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0:
            return f'A Saxon has recieved {damage} points of damage'
        else:
            return 'A Saxon has died in act of combat'

# Davicente

class War():
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        randomsax=random.choice(self.saxonArmy)
        randomvik=random.choice(self.vikingArmy)
        dmg=randomvik.attack()
        self.randomsax.recieveDamage(dmg)
        if self.randomsax()<=0:
            self.saxonArmy.remove(randomsax)
            return f'{randomsax} has fallen'
        return dmg

    def saxonAttack(self):
        randomsax=random.choice(self.saxonArmy)
        randomvik=random.choice(self.vikingArmy)
        dmg=randomsax.attack()
        if self.randomvik()<=0:
            self.vikingArmy.remove(randomvik)
            return f'{randomvik} has fallen'
        return dmg

    def showStatus(self):
        if len(self.saxonArmy)==0:
            return 'Vikings have won the war of the century'
        elif len(self.vikingArmy)==0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle'

    pass



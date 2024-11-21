import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strenght = strength
    
    def attack(self):
        return self.strenght

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []

    def addViking(self, viking):
        self.viking_army.append(viking)
    
    def addSaxon(self, saxon):
        self.saxon_army.append(saxon)
    
    def vikingAttack(self):
        if not self.saxon_army:
            return None
        saxon_left = random.randint(0, len(self.saxon_army) - 1)
    saxon = self.saxon_army[saxon_left]
    damage = random.choice([viking.strength for viking in self.viking_army])
    result = saxon.receive_damage(damage)
    self.saxon_army = [sax for sax in self.saxon_army if sax.health > 0]
    return result
    
    def saxonAttack(self):
        if not self.viking_army:
            return None
        viking_index = random.randint(0, len(self.viking_army) - 1)
        viking = self.viking_army[viking_index]
        damage = random.choice([saxon.strength for saxon in self.saxon_army])
        result = viking.receive_damage(damage)
        self.viking_army = [vik for vvik in self.viking_army if vik.health > 0]
        return result

    def showStatus(self):
        if not self.saxon_army:
            return "Vikings have won the war of the century!"
        elif not self.viking_army:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        
        

    pass



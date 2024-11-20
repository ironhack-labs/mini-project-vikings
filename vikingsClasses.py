import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength

    def attack(self):
        # do an amount of damage = to strength
        # should receive 0 arguments
        # should return the strength property of the Soldier
        return self.strength

    def receiveDamage(self, damage):
        # decrease health by a given interger
        # should receive 1 argument (the damage)
        #   should remove the received damage from the health property
        #  shouldn't return anything
        self.health -= damage


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):

          self.name = name
          self.health = health
          self.strength = strength
        

    def battleCry(self):
      return 'Odin Owns You All!'


    def receiveDamage(self, damage):
        self.health -= damage

        if self.health <= 0:
          return f'{self.name} has died in act of combat'
        elif self.health >= 0:
          return f'{self.name} has received {damage} points of damage'



# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # # your code here
        self.health = health
        self.strength = strength

        # super().__init__(health, strength)

    def receiveDamage(self, damage):
        # your code here
        # should receive 1 argument (the damage)
        # should remove the received damage from the health property
        # if the Saxon is still alive, it should return "A Saxon has received DAMAGE points of damage"
        # if the Saxon dies, it should return "A Saxon has died in combat"
        self.health -= damage

        if  self.health <= 0:
            return "A Saxon has died in combat"
        else:
            return f"A Saxon has received {damage} points of damage"

# Davicente

class War():
    def __init__(self):
        # your code here
        # should assign an empty array to the vikingArmy property
        # should assign an empty array to the saxonArmy property
        self.vikingArmy=[]
        self.saxonArmy=[]



    def addViking(self, viking):
        # your code here

        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        # your code here
        # should receive 1 argument (a Saxon object)
        # should add the received Saxon to the army
        # shouldn't return anything

        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        # your code here
      # A Saxon (chosen at random) has their receiveDamage() method called with
      # the damage equal to the strength of a Viking (also chosen at random).
      # This should only perform a single attack and the Saxon doesn't get to
      # attack back.
    
      
        viking_soldier = random.choice(self.vikingArmy)
        saxon_soldier = random.choice(self.saxonArmy)
        result = saxon_soldier.receiveDamage(viking_soldier.strength)
        if saxon_soldier.health <= 0:
            self.saxonArmy.remove(saxon_soldier)
        return result


    def saxonAttack(self):
        # your code here
        viking_soldier = random.choice(self.vikingArmy)
        saxon_soldier = random.choice(self.saxonArmy)
        result = viking_soldier.receiveDamage(saxon_soldier.strength)
        if viking_soldier.health <= 0:
            self.vikingArmy.remove(viking_soldier)
        return result       


    def showStatus(self):
        # your code here
        # if the Saxon array is empty, should return "Vikings have won the war of the century!"
        # if the Viking array is empty, should return "Saxons have fought for their lives and survive another day..."
        # if there are at least 1 Viking and 1 Saxon, should return "Vikings and Saxons are still in the thick of battle."
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        
        else:
            return "Vikings and Saxons are still in the thick of battle."





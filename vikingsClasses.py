import random

# Soldier


class Soldier:# Soldier class: Represents a soldier with health and strength
    def __init__(self, health, strength):
        # your code here
        self.health = health# Initialize soldier's health
        self.strength = strength# Initialize soldier's strength
            
    
    def attack(self):
        # your code here
        return self.strength# Return the soldier's strength for attacking

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage# Decrease the soldier's health by the received damage
    

# Viking

class Viking(Soldier):# Viking class: Inherits from Soldier and adds a name and battle cry
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength)# Initialize parent (Soldier) class
        self.name = name# Initialize Viking's name

    def battleCry(self):
        # your code here
        return f"Odin Owns You All!"# Return Viking's battle cry

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage # Decrease Viking's health by received damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"# Return message if Viking is still alive
        else:
            return f"{self.name} has died in act of combat"# Return message if Viking dies
                

# Saxon

class Saxon(Soldier):# Saxon class: Inherits from Soldier and represents a Saxon with no additional properties
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)# Initialize parent (Soldier) class

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage# Decrease Saxon's health by received damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage" # Return message if Saxon is still alive
        else:
            return f"A Saxon has died in combat"# Return message if Saxon dies

# Davicente

class War():# War class: Controls the war between Vikings and Saxons
    def __init__(self):
        # your code here
        self.vikingArmy = []# Initialize empty Viking army
        self.saxonArmy = []# Initialize empty Saxon army

    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)# Add a Viking to the Viking army
    
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)# Add a Saxon to the Saxon army
    
    def vikingAttack(self):
        # your code here

        # Check if there are any Vikings and Saxons to attack/defend
        if not self.vikingArmy:
            return "No Vikings left to attack."
        if not self.saxonArmy:
            return "No Saxons left to defend."

        viking = random.choice(self.vikingArmy)# Select a random Viking
        saxon = random.choice(self.saxonArmy)# Select a random Saxon
        damage_hit = saxon.receiveDamage(viking.strength) # Saxon receives damage from Viking

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)# Remove the Saxon from the army if they die

        return damage_hit
    
    def saxonAttack(self):
        # your code here

        # Check if there are any Saxons and Vikings to attack/defend
        if not self.saxonArmy:
            return "No Saxons left to attack."
        if not self.vikingArmy:
            return "No Vikings left to defend."
    
        viking = random.choice(self.vikingArmy)# Select a random Viking
        saxon = random.choice(self.saxonArmy)# Select a random Saxon
        damage_hit = viking.receiveDamage(saxon.strength) # Viking receives damage from Saxon

        if viking.health <= 0:
            self.vikingArmy.remove(viking)# Remove the Viking from the army if they die

        return damage_hit

    def showStatus(self):# Check the current status of the war
        # your code here
        if not self.saxonArmy: # Vikings win if Saxons are all dead
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy: # Saxons win if Vikings are all dead
            return "Saxons have fought for their lives and survive another day..."
        else: # Continue if both armies are still alive
            return "Vikings and Saxons are still in the thick of battle."
    pass



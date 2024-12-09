import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
       """
       Initializes a soldier instance with health and strength.

       Parameters:
           health (int): The health of the soldier.
           strength (int): The strength of the soldier.
        """

       self.health = health
       self.strength = strength
               
    def attack(self):
        """
        Returns the strength of the soldier, with 0 arguments.
        """
        return self.strength
         

    def receiveDamage(self, damage):
        """
        Receives the damage as an argument, and reduces the health of the soldier..

        Parameter:
            damage (int): damage to be subtracted from health.
        """
        self.health -= damage


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

        
    def receiveDamage(self, damage):
        """
        Subtracts damage received from the health of the individual.
        
        Parameters:
            damage(int): damage to be subtracted from health.
        
        Returns:
            str: message about the Viking based on their remaining health.
        """
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        

    def battleCry(self):
        """
        Returns the vikings battle cry.
        
        Returns:
            str: the Vikings battle cry.
        """
        return "Odin Owns You All!"
        
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        """
        Initializes a Saxon instance, inheriting from Soldier, with two arguments, health and strength.
        """
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        """
        Reduces health based on the damage received and returns a message regarding the health of the Saxon.

        Parameters:
            damage (int): damage to be substracted from the health of the Saxon.

        Returns:
            str: message regarding the health of the Saxon.
        """
        self.health -= damage
        
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War

class War():
    def __init__(self):
        """
        """
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking):
        """
        Adds a viking to the viking army.

        Parameters:
            viking (Viking): a Viking instance.
        """
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        """
        Adds a Saxon to the Saxon army.

        Parameters:
            saxon (Saxon): Saxon instance.
        """
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        """
        Simulates a Viking-Saxon attack.

        Returns:
            str: message with the result of the attack.
        """
        if not self.saxonArmy:
            return "No Saxons are left to continue."

        attacking_viking = random.choice(self.vikingArmy)
        
        defending_saxon = random.choice(self.saxonArmy)
        
        result = defending_saxon.receiveDamage(attacking_viking.attack())
        
        if defending_saxon.health <= 0:
            self.saxonArmy.remove(defending_saxon)
        
        return result
    
    def saxonAttack(self):
        """
        Simulates a Saxon attacking a Viking.

        Returns:
            str: message with the result of the attack.
        """
        if not self.vikingArmy:
            return "There are no Vikings left to continue."
            
        attacking_saxon = random.choice(self.saxonArmy)
        
        defending_viking = random.choice(self.vikingArmy)
        
        result = defending_viking.receiveDamage(attacking_saxon.attack())

        if defending_viking.health <= 0:
            self.vikingArmy.remove(defending_viking)

        return result
    
    def showStatus(self):
        """
        Returns the status of the war based on the remaining armies.

        Returns:
            str: a message indicating the current status of the war.
        """
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
     


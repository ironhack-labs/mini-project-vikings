import random

# Soldier
class Soldier:
    def __init__(self, health, strength):
        """
        Initialize Soldier properties.
        Args:
            healt (int): soldier health
            strength (int): soldier strength
        """                    
        self.health = health
        self.strength = strength
        
    def attack(self):
        """
        Returns the Soldier's Strength.
        Args:
            no arguments
        """            
        return self.strength

    def receiveDamage(self, damage):
        """
        Set Soldier received damage.
        Args:
            damage (int): receive damage by the soldier
        """          
        self.health -= damage
    

# Viking Class - inheritance from Soldier
class Viking(Soldier):
    def __init__(self, name, health, strength):
        """
        Initialize the viking soldier properties.
        Args:
            name (str): viking name        
            healt (int): soldier health
            strength (int): soldier strength        
        """                
        super().__init__(health, strength) #taking the things from PARENT class        
        self.name = name

    def battleCry(self):
        """
        Return the Viking Yahl Message.
        Args:
            no arguments
        Return:
            string
        """             
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        """
        Return the Viking Yahl Message.
        Args:
            damage (int): damage received by the viking
        Return:
            string message
        """             
        super().receiveDamage( damage )
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon Class - inheritance from Soldier
class Saxon(Soldier):
    def __init__(self, health, strength):
        """
        Initialize the saxon soldier properties.
        Args:
            healt (int): soldier health
            strength (int): soldier strength        
        """            
        super().__init__(health, strength) #taking the things from PARENT class

    def receiveDamage(self, damage):
        """
        Return the Saxon battle message.
        Args:
            damage (int): damage received by the viking
        Return:
            string message
        """           
        super().receiveDamage( damage )
        if self.health  > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# Davicente
class War():
    def __init__(self):
        """
        Initialize the War armies
            vikingArmy (Viking): list of Vikings
            saxonArmy (Saxon): list of Saxons
        Args:
            no arguments
        """          
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        """
        Add Vikings to Viking Army List
        Args:
            viking (object): viking object (name, health, strength)
        """         
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        """
        Add Saxon to Saxon Army List
        Args:
            saxon (object): saxon object (health, strength)
        """                 
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        """
        Realize a Viking Attack
        Args:
            no arguments
        Returns:
            string (str): Saxon Army status and/or Saxon soldier damage status (Viking or Saxon)
        """
        if not self.saxonArmy:
            return self.showStatus()
        elif not self.vikingArmy:
            return "Viking Army not have soldiers!"  # Optional: for testing 
        else:
            # Randon selection for the Saxon and the Viking 
            # saxon = random.randrange(len(self.saxonArmy)) # random.choice(
            # viking = random.randrange(len(self.vikingArmy))
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)

            # attack the Saxon 
            # attack_result_msg = self.saxonArmy[saxon].receiveDamage( self.vikingArmy[viking].attack())
            attack_result_msg = saxon.receiveDamage( viking.attack() )

            # Remove the Saxon from the Saxon Army if die
            if saxon.health <= 0:            
                self.saxonArmy.remove(saxon)
            return attack_result_msg
    
    def saxonAttack(self):
        """
        Realize a Saxon Attack
        Args:
            no arguments
        Returns:
            string (str): Viking Army status and/or Viking soldier damage status (Viking or Saxon)
        """        
        if not self.vikingArmy:
            return self.showStatus() # No more vikings         
        elif not self.saxonArmy:
            return "Saxon Army not have soldiers!" # Optional: for testing
        else:
            # Randon selection for the Saxon and the Viking 
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
    
            # attack the Viking 
            attack_result_msg = viking.receiveDamage(saxon.attack())
    
            # Remove the Viking from the Viking Army if die
            if viking.health <= 0:
                self.vikingArmy.remove(viking)
            return attack_result_msg

    def showStatus(self):
        """
        Return the Army Status
        Args:
            no arguments
        Returns:
            string (str):  Army status (Viking or Saxon)
        """          
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        elif self.vikingArmy and self.saxonArmy:
            return "Vikings and Saxons are still in the thick of battle."
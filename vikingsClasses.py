
import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        """
        Initializes the Soldier with health and strength.
        :param health: Integer, representing the Soldier's health points.
        :param strength: Integer, representing the Soldier's strength points.
        """
        self.health = health  # Assign health to the Soldier
        self.strength = strength  # Assign strength to the soldier 
   
    
    def attack(self):
        # your code here
        """
        Returns the Soldier's strength.
        :return: Integer, the Soldier's strength.
        """
        return self.strength # Return the soldier's strength as attack power
        
    def receiveDamage(self, damage):
        # your code here
        """
        Reduces the Soldier's health by the damage received.
        :param damage: Integer, the amount of damage inflicted on the Soldier.
        """
        self.health -= damage # Decrease health by the damage amount


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        """
        Initializes a Viking with name, health, and strength.
        :param name: String, the name of the Viking.
        :param health: Integer, the Viking's health points.
        :param strength: Integer, the Viking's strength points.
        """
        super().__init__(health, strength)  # Call the Soldier constructor
        self.name = name  # Initialize the name for the Viking

    def battleCry(self):
        # your code here
        """
        Returns the Viking's signature battle cry.
        :return: String, the battle cry.
        """
        return "Odin Owns You All!"  # Return the Viking's battle cry

    def receiveDamage(self, damage):
        # your code here
        """
        Reduces the Viking's health by the damage received.
        If the Viking dies, returns a death message.
        Otherwise, returns the damage message.
        :param damage: Integer, the amount of damage inflicted on the Viking.
        :return: String, describing the result of the damage.
        """
        self.health -= damage  # Reduce health by the damage
        if self.health <= 0:
            return f"{self.name} has died in act of combat"
        else:
            return f"{self.name} has received {damage} points of damage"

# Saxon

class Saxon(Soldier):
    
    def __init__(self, health, strength):
        # your code here
        """
        Initializes a Saxon with health and strength.
        :param health: Integer, the Saxon's health points.
        :param strength: Integer, the Saxon's strength points.
        """
        super().__init__(health, strength)  # Call the Soldier constructor

    
    def receiveDamage(self, damage):
        # your code here
        """
        Reduces the Saxon's health by the damage received.
        If the Saxon dies, returns a death message.
        Otherwise, returns the damage message.
        :param damage: Integer, the amount of damage inflicted on the Saxon.
        :return: String, describing the result of the damage.
        """
        self.health -= damage  # Reduce health by the damage
        if self.health <= 0:
            return "A Saxon has died in combat"  # Death message
        else:
            return f"A Saxon has received {damage} points of damage"  # Damage received message

# Davicente

class War:
    def __init__(self):
        # your code here
        # Initialize the war with empty armies
        self.vikingArmy = []  # List to store Vikings
        self.saxonArmy = []  # List to store Saxons

    def addViking(self, viking):
        # your code here
        # Adds a Viking to the vikingArmy
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        # your code here
        # Adds a Saxon to the saxonArmy
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        # your code here
        # Randomly select a Viking and a Saxon
        viking = random.choice(self.vikingArmy)  # Random Viking
        saxon = random.choice(self.saxonArmy)  # Random Saxon
        
        # The Saxon receives damage equal to the Viking's strength
        result = saxon.receiveDamage(viking.strength)
        
        # Remove dead Saxons from the army
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        
        return result

    def saxonAttack(self):
        # your code here
        # Randomly select a Saxon and a Viking
        saxon = random.choice(self.saxonArmy)  # Random Saxon
        viking = random.choice(self.vikingArmy)  # Random Viking
        
        # The Viking receives damage equal to the Saxon's strength
        result = viking.receiveDamage(saxon.strength)
        
        # Remove dead Vikings from the army
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        
        return result

    def showStatus(self):
        # your code here
        # Display the current status of the war
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

import random

# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

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
            return "A Saxon has died in combat"
# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        import random
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result

    def saxonAttack(self):
        import random
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

import unittest
from vikingsClasses import Viking
from inspect import signature


class TestViking(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.name = 'Harald'
        cls.strength = 150
        cls.health = 300
        cls.viking = Viking(cls.name, cls.health, cls.strength)
        
    def testShouldReciveThreeParams(self):
        self.assertEqual(len(signature(Viking).parameters), 3)
        
    def testName(self):
        self.assertEqual(self.viking.name, self.name)

    def testHealth(self):
        self.assertEqual(self.viking.health, self.health)

    def testStrenght(self):
        self.assertEqual(self.viking.strength, self.strength)

    def testAttackShouldBeFunction(self):
        self.assertEqual(callable(self.viking.attack), True)

    def testAttackReciveNoParameters(self):
        self.assertEqual(len(signature(self.viking.attack).parameters), 0)

    def testAttackShouldReturnStrength(self):
        self.assertEqual(self.viking.attack(), self.strength)

    def testReceiveDamageIsFunction(self):
        self.assertEqual(callable(self.viking.receiveDamage), True)

    def testReceiveDamageReciveOneParam(self):
        self.assertEqual(
            len(signature(self.viking.receiveDamage).parameters), 1)

    def testReciveDamageShouldRestHealth(self):
        self.viking.receiveDamage(50)
        self.assertEqual(self.viking.health, self.health - 50)

    def testReciveDamageShouldReturnString50(self):
        self.assertEqual(self.viking.receiveDamage(50), self.name +
                         ' has received 50 points of damage')

    def testReciveDamageShouldReturnString70(self):
        self.assertEqual(self.viking.receiveDamage(70), self.name +
                         ' has received 70 points of damage')

    def testReceiveDamageShouldReturnStringDeath(self):
        self.assertEqual(self.viking.receiveDamage(self.health),
                         self.name + ' has died in act of combat')

    def testBattleCry(self):
        self.assertEqual(callable(self.viking.battleCry), True)

    def testBattleCryReturnString(self):
        self.assertEqual(self.viking.battleCry(), 'Odin Owns You All!')
        
        if __name__ == '__main__':
            unittest.main()   

import unittest
from vikingsClasses import Saxon
from inspect import signature


class TestSaxon(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.health = 60
        cls.strength = 25
        cls.saxon = Saxon(cls.health, cls.strength)

    def testSaxonShouldReceiveTwoParams(self):
        self.assertEqual(len(signature(Saxon).parameters), 2)

    def testHealth(self):
        self.assertEqual(self.saxon.health, self.health)

    def testStrength(self):
        self.assertEqual(self.saxon.strength, self.strength)

    def testAttack(self):
        self.assertEqual(callable(self.saxon.attack), True)

    def testAttackShouldReceiveNoParams(self):
        self.assertEqual(len(signature(self.saxon.attack).parameters), 0)

    def testAttackREturnStrength(self):
        self.assertEqual(self.saxon.attack(), self.strength)

    def testReceiveDamageIsFunction(self):
        self.assertEqual(callable(self.saxon.receiveDamage), True)

    def testReceiveDamageShouldReceiveOneParam(self):
        self.assertEqual(
            len(signature(self.saxon.receiveDamage).parameters), 1)

    def testReceiveDamage(self):
        self.saxon.receiveDamage(1)
        self.assertEqual(self.saxon.health, self.health - 1)

    def testReceiveDamageString45(self):
        self.assertEqual(self.saxon.receiveDamage(
            45), 'A Saxon has received 45 points of damage')

    def testReceiveDamageString10(self):
        self.assertEqual(self.saxon.receiveDamage(
            10), 'A Saxon has received 10 points of damage')

    def testReceiveDamageStringDied(self):
        self.assertEqual(self.saxon.receiveDamage(self.health),
                         'A Saxon has died in combat')


if __name__ == '__main__':
    unittest.main()  
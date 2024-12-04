import unittest
from vikingsClasses import Saxon
from inspect import signature

class TestSaxon(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # Setup test values for Saxon
        cls.health = 60
        cls.strength = 25
        cls.saxon = Saxon(cls.health, cls.strength)

    def testSaxonShouldReceiveTwoParams(self):
        # Test to ensure Saxon constructor receives 2 parameters
        self.assertEqual(len(signature(Saxon).parameters), 2)

    def testHealth(self):
        # Test if Saxon's health is set correctly
        self.assertEqual(self.saxon.health, self.health)

    def testStrength(self):
        # Test if Saxon's strength is set correctly
        self.assertEqual(self.saxon.strength, self.strength)

    def testAttack(self):
        # Test if Saxon's attack method is callable
        self.assertEqual(callable(self.saxon.attack), True)

    def testAttackShouldReceiveNoParams(self):
        # Test if Saxon's attack method takes no parameters
        self.assertEqual(len(signature(self.saxon.attack).parameters), 0)

    def testAttackReturnStrength(self):
        # Test if Saxon's attack method returns the strength
        self.assertEqual(self.saxon.attack(), self.strength)

    def testReceiveDamageIsFunction(self):
        # Test if Saxon's receiveDamage method is callable
        self.assertEqual(callable(self.saxon.receiveDamage), True)

    def testReceiveDamageShouldReceiveOneParam(self):
        # Test if Saxon's receiveDamage method takes 1 parameter (damage)
        self.assertEqual(len(signature(self.saxon.receiveDamage).parameters), 1)

    def testReceiveDamage(self):
        # Test if Saxon's health decreases correctly after receiving damage
        self.saxon.receiveDamage(1)
        self.assertEqual(self.saxon.health, self.health - 1)

    def testReceiveDamageString45(self):
        # Test the string returned by Saxon's receiveDamage method when receiving 45 damage
        self.assertEqual(self.saxon.receiveDamage(45), 'A Saxon has received 45 points of damage')

    def testReceiveDamageString10(self):
        # Test the string returned by Saxon's receiveDamage method when receiving 10 damage
        self.assertEqual(self.saxon.receiveDamage(10), 'A Saxon has received 10 points of damage')

    def testReceiveDamageStringDied(self):
        # Test the string returned when Saxon dies after receiving full health damage
        self.assertEqual(self.saxon.receiveDamage(self.health), 'A Saxon has died in combat')

if __name__ == '__main__':
    unittest.main()

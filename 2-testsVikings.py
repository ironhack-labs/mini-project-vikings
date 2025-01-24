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

    class Viking:
        def __init__(self, name, health, strength):
            self.name = name
        self.health = health
        self.strength = strength

    def attack(self):
        # Returns the Viking's strength
        return self.strength

    def receiveDamage(self, damage):
        # Reduces the Viking's health by the damage amount
        self.health -= damage
        # Returns appropriate message based on health
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        # Returns the battle cry
        return "Odin Owns You All!"

if __name__ == '__main__':
    unittest.main()

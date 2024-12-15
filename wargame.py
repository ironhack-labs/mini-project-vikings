from vikingsClasses import Soldier, Viking, Saxon, War
import random

soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]
great_war = War()

# Crear 5 Vikings con nombres aleatorios
for _ in range(5):
    name = random.choice(soldier_names)
    health = 100
    strength = random.randint(50, 100)
    great_war.addViking(Viking(name, health, strength))

# Crear 5 Saxons con atributos aleatorios
for _ in range(5):
    health = 100
    strength = random.randint(50, 100)
    great_war.addSaxon(Saxon(health, strength))

# Simular la guerra
round = 0
while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    # Realizar ataques
    great_war.vikingAttack()
    great_war.saxonAttack()
    
    # Mostrar el estado de cada ronda
    print(f"round: {round} // Viking army: {len(great_war.vikingArmy)} warriors",
          f"and Saxon army: {len(great_war.saxonArmy)} warriors")
    print(great_war.showStatus())
    
    round += 1

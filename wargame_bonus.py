# With a correction already implemented: dont forget to initialize an instance of Class "War"

from vikingsClasses import Viking, Saxon, War
import random
import time

# Nombres más elaborados y características de vikingos
VIKING_NAMES = [
    "Ragnar Lothbrok", "Bjorn Ironside", "Ivar the Boneless", 
    "Lagertha", "Floki", "Rollo", "Ubbe", "Sigurd", "Hvitserk", "Aslaug"
]

SAXON_NAMES = [
    "Aethelred", "Alfred", "Edmund", "Harold", "Edward", 
    "Ethelred", "Cnut", "Edgar", "Oswald", "Eadric"
]

BATTLE_CRIES = [
    "¡Skål!", "¡Valhalla nos espera!", "¡Por Odín!", 
    "¡A la victoria!", "¡Por la gloria de Asgard!"
]

class NamedSaxon(Saxon):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in combat"

def create_viking_army(size):
    vikings = []
    for _ in range(size):
        name = random.choice(VIKING_NAMES)
        health = random.randint(80, 120)
        strength = random.randint(20, 40)
        vikings.append(Viking(name, health, strength))
    return vikings

def create_saxon_army(size):
    saxons = []
    for _ in range(size):
        name = random.choice(SAXON_NAMES)
        health = random.randint(70, 100)
        strength = random.randint(15, 35)
        saxons.append(NamedSaxon(name, health, strength))
    return saxons

def display_armies_status(war):
    print("\n=== ESTADO DE LOS EJÉRCITOS ===")
    print(f"Vikings: {len(war.vikingArmy)} guerreros")
    for viking in war.vikingArmy:
        print(f"  - {viking.name}: ❤️ {viking.health} 💪 {viking.strength}")
    
    print(f"\nSaxons: {len(war.saxonArmy)} guerreros")
    for saxon in war.saxonArmy:
        print(f"  - {saxon.name}: ❤️ {saxon.health} 💪 {saxon.strength}")
    print("============================\n")

def battle_round(war, round_number):
    print(f"\n🗡️  RONDA {round_number} 🗡️")
    
    # Ataque vikingo
    viking_result = war.vikingAttack()
    if viking_result:
        print(f"⚔️  {viking_result}")
        print(random.choice(BATTLE_CRIES))
    
    # Ataque sajón
    saxon_result = war.saxonAttack()
    if saxon_result:
        print(f"⚔️  {saxon_result}")
    
    time.sleep(1)  # Pausa dramática
    display_armies_status(war)

def main():
    print("🏰 GUERRA DE VIKINGOS VS SAJONES 🏰")
    
    # Configuración inicial
    army_size = int(input("Ingresa el tamaño de cada ejército (1-10): "))
    army_size = max(1, min(10, army_size))  # Limitar entre 1 y 10
    
    # Crear guerra y ejércitos
    war = War()
    
    print("\n⚔️ Creando ejército vikingo...")
    for viking in create_viking_army(army_size):
        war.addViking(viking)
    
    print("⚔️ Creando ejército sajón...")
    for saxon in create_saxon_army(army_size):
        war.addSaxon(saxon)
    
    display_armies_status(war)
    
    # Loop principal de batalla
    round_number = 1
    input("Presiona Enter para comenzar la batalla...")
    
    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        battle_round(war, round_number)
        round_number += 1
        
        if round_number > 1:
            continue_battle = input("Presiona Enter para continuar (o 'q' para salir): ")
            if continue_battle.lower() == 'q':
                break
    
    # Resultado final
    print("\n🏆 RESULTADO FINAL 🏆")
    print(war.showStatus())

if __name__ == "__main__":
    main()
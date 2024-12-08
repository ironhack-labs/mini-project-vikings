from vikingsClasses import War, Viking, Saxon
import random

def create_viking_team(num_vikings):
    viking_names = ['Andres', 'Brandon','Dara','Javier','Luis','Natalia']
    vikings = []

    for x in range(num_vikings):
        name = random.choice(viking_names)
        health = random.randint(100, 150)
        strength = random.randint(30, 50)
        vikings.append(Viking(name, health, strength))
    
    return vikings
    
def create_saxon_team(num_saxons):
    saxons = []

    for x in range(num_saxons):
        health =  random.randint(80, 120)
        strength = random.randint(20, 40)
        saxons.append(Saxon(health, strength))
    
    return saxons

def run_game(vikings, saxons):
    war = War()

    for viking in vikings:
        war.addViking(viking)
    for saxon in saxons:
        war.addSaxon(saxon)

    while len(war.vikingArmy) > 0 and len(war.saxonArmy) > 0:
        
        if random.choice([True, False]):
            result = war.vikingAttack()
            print(result, '\n', war.showStatus())
        else:
            result = war.saxonAttack()
            print(result, '\n', war.showStatus())
    
    print('\nGame Over!')
    

if __name__ == "__main__":

    vikings = create_viking_team(random.randint(5,10))
    saxons = create_saxon_team(random.randint(5,10))

    print("Starting the Viking vs Saxon War Simulation!")
    run_game(vikings, saxons)

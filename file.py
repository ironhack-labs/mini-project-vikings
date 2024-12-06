# With a correction already implemented: dont forget to initialize an instance of Class "War"


from vikingsClasses import Soldier, Viking, Saxon, War
import random


valhalla_war = War()

#Create Vikings Army
def create_vikings_army(vikings):
    """
    Initialize the Saxon Army List.
    Args:
        vikings (str list): a list of possible vikings names.
    """    
    for viking in vikings:
        valhalla_war.addViking( Viking(viking, 100, random.randint(0,100)) )

#Create Saxons Army
def create_saxons_army(army_size):
    """
    Initialize the Saxon Army List.
    Args:
        army_size (int): the Saxon Army size, same as Vinkings Army size
    """    
    for i in range(0, army_size):
        valhalla_war.addSaxon( Saxon( 100,random.randint(0,100) ) )

def setup_game():
    """
    Initialize the Vinking's and Saxon's Armies
    Args:
        no arguments
    """
    vikings_names = ["Ragnar","Olaf","Bjorn","Ivar the Boneless", "Gerard","Lagertha","Torvi","Floki"]
    random.shuffle(vikings_names) # shuffle the vinkings names
    
    army_size = len(vikings_names)

    create_vikings_army(vikings_names)
    create_saxons_army(army_size)

def start_war():
    """
    Run all necessary functions for the war.
    Args:
        no arguments
    """
    battle_round = 0
    while valhalla_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        valhalla_war.vikingAttack()
        valhalla_war.saxonAttack()
        print(f"Round {battle_round}: Viking army: {len(valhalla_war.vikingArmy)} warriors",end=' ')
        print(f"and Saxon army: {len(valhalla_war.saxonArmy)} warriors")
        print(f"  {valhalla_war.showStatus()}")
        battle_round += 1
        
def main():
    """
    The main function or caller for the program.
    Args:
        no arguments
    """        
    setup_game() # setup all variables and list
    print("\n¡Let's The War Begin!")
    start_war() # game simulation AI
    
# Call the Main Funtion
if __name__ == "__main__":
    main()
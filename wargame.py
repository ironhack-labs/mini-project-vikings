"""
Define functions to create the workflow of the game:
i.e. functions to create teams (maybe you can create random teams with your classmates' names), run the game, etc.
"""

from vikingsClasses import Soldier, Viking, Saxon, War
import random

name_list = ["Blanca","Javi","Jorge","Pablo","Ester","Maria","Fran","Mamen"]

def create_team(name_list, members):
    return [random.choice(name_list) for _ in range(0, members)]

team_members = 10
team_members_var = 3

vikings_team_a = create_team(name_list, team_members + random.randint(0, team_members_var))
vikings_team_b = create_team(name_list, team_members + random.randint(0, team_members_var))
saxons_team = create_team(name_list, team_members + random.randint(0, team_members_var))

min_health = 10
max_health = 100

min_strength = 1
max_strength = 10

war = War()

def fill_team(team, is_viking):
    if is_viking:
        for member in team:
            war.addViking(
                Viking(
                    member,
                    random.randint(min_health, max_health),
                    random.randint(min_strength, max_strength)))
    else:
        for member in team:
            war.addSaxon(
                Saxon(
                    random.randint(min_health, max_health),
                    random.randint(min_strength, max_strength)))

fill_team(vikings_team_a, True)
#fill_team(vikings_team_b, True)
fill_team(saxons_team, False)

print(f"Viking Team: {len(war.vikingArmy)}")
print(f"Saxon Team: {len(war.saxonArmy)}")

while (len(war.vikingArmy) > 0 and len(war.saxonArmy) > 0):
    print(war.vikingAttack())
    if len(war.saxonArmy) > 0:
        print(war.saxonAttack())
print("\n" + war.showStatus() + "\n")
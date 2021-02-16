import random
from hero import Hero
from ability import Ability

class Team():
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        
        if not foundHero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
    
    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
    
    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does) -
            our_team_hero = random.choice(living_heroes)
            other_team_hero = random.choice(living_opponents)
            
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            our_team_hero.fight(other_team_hero)
            
            # 3) update the list of living_heroes and living_opponents
            if our_team_hero.is_alive():
                living_heroes.remove(our_team_hero) 
            else:
                living_opponents.remove(other_team_hero)
            
            # to reflect the result of the fight
            if len(living_heroes) > 0 and len(living_opponents) == 0:
                return "Our heroes win"
            elif len(living_heroes) == 0 and len(living_opponents) > 0:
                return "Opponent heroes win"
            else:
                pass
            

   

if __name__ == "__main__":
    # Teams
    team_1 = Team("team-1")
    team_2 = Team("team-2")

    ### BUILDING HEROES ###
    # Hero 1
    spider_man = Hero("Spider Man")
    spider_man.add_ability( Ability("Webshot", 15) )
    
    # Hero 2
    iron_man = Hero("Iron Man")
    iron_man.add_ability( Ability("Hand Cannon",25) )
    
    # Hero 3
    hulk = Hero("Hulk")
    hulk.add_ability( Ability("Hulk Smash", 40) )

    # Hero 4
    black_widow = Hero("Black WIdow")
    black_widow.add_ability( Ability("Punch", 5) )

    # Create team
    team_1.add_hero( spider_man )
    team_1.add_hero( iron_man )
    team_2.add_hero( hulk )
    team_2.add_hero( black_widow )

    # Fight
    team_1.attack(team_2)
import random
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero():
    def __init__(self, name, starting_health = 100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        pass

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def deffend(self, incoming_damage):
        total_block = 0

        if len(self.armors) == 0 or self.current_health <= 0:
            return total_block
        else:
            for armor in self.armors:
                total_block += armor.block()
            return total_block

    def take_damage(self, damage):
        defend = self.deffend(damage)
        damage_dealt = damage - defend
        self.current_health -= damage_dealt

    def add_kill(self, num_kills=1):
        self.kills += num_kills
    
    def add_deaths(self, num_deaths=1):
        self.deaths += num_deaths

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        self.opponent = opponent

        # ends in draw
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("draw")
            return "Draw"

        # ends in hero 1 winning
        elif len(self.abilities) > 0 and len(opponent.abilities) == 0:
            print(f"{self.name} wins!")
            self.add_kill()
            opponent.add_deaths()
            return f"{self.name} wins!"

        # ends in hero 2 winning
        elif len(self.abilities) == 0 and len(opponent.abilities) > 0:
            print(f"{opponent.name} wins!")
            self.add_deaths()
            opponent.add_kill()
            return f"{opponent.name} wins!"

        # the real fight
        else:
            print("we have a fight")

            while self.is_alive() == True or opponent.is_alive() == True:
                self.take_damage( opponent.attack() )
                opponent.take_damage( self.attack() )

                # print(f"{self.name}'s health:       {self.current_health}")
                # print(f"{opponent.name}'s health:    {opponent.current_health}")
                
                if self.is_alive() == True and opponent.is_alive() == False:
                    print(f"\n{self.name} wins!")
                    self.add_kill()
                    opponent.add_deaths()
                    return f"{self.name} wins!"
                
                if self.is_alive() == False and opponent.is_alive() == True:
                    print(f"\n{opponent.name} wins!")
                    self.add_deaths()
                    opponent.add_kill()
                    return f"{opponent.name} wins!"
                
                if self.is_alive() == False and opponent.is_alive() == False:
                    print(f"\nDouble KO")
                    self.add_deaths()
                    opponent.add_deaths()
                    return f"Double KO"



if __name__ == "__main__":
    
    # HERO 1
    hero_1 = Hero("Spider Man", 250)

    hero_1.add_ability( Ability("Web Shot", 50) )
    hero_1.add_ability( Ability("Web Spray", 30) )
    hero_1.add_armor( Armor("shield", 40) )


    # HERO 2 
    hero_2 = Hero("Miles Morales", 200)

    hero_2.add_ability( Ability("Web Strike", 65) )
    hero_2.add_ability( Ability("Web Throw", 20) )
    hero_2.add_armor( Armor("shield", 50) )


    # FIGHT!
    hero_1.fight(hero_2)


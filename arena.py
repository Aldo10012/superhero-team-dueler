from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team
import random


class Arena:
    def __init__(self):
        self.team_one = None #Team("Team Iron Man")
        self.team_two = None #Team("Team Captain America")
    
    def create_ability(self):
        name = input("What is the ability name?  ")
        max_damage = input("What is the max damage of the ability?  ")
        return Ability(name, max_damage)
    
    def create_weapon(self):
        name = input("What is the name of your weapon?   ")
        max_damage = input("What is the max damage of the weapon?  ")

        return Weapon(name, int(max_damage))
    
    def create_armor(self):
        name = input("What is the name of your armor?   ")
        max_block = input("What is the max block power of the armor?  ")
        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               ability = self.create_ability()
               hero.add_ability(ability)

           elif add_item == "2":
               weapon = self.create_weapon()
               hero.add_weapon(weapon)
               
           elif add_item == "3":
               armor = self.create_armor()
               hero.add_armor(armor)
               
        return hero

    def build_team_one(self):
        team_name = input("What's your team name?   ")
        self.team_one = Team(team_name)

        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        team_name = input("What's your team name?   ")
        self.team_two = Team(team_name)

        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    # ERROR:  TypeError: can only concatenate str (not "int") to str   
    def team_battle(self):
        self.team_one.attack(self.team_two)


arena = Arena()
arena.build_team_one()
arena.build_team_two()
arena.team_battle()

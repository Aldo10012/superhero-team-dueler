from ability import Ability
import random

class Weapon(Ability):
    def __init__(self, name, max_damage):
        super().__init__(name, max_damage)
        self.weapon_damage = random.randint( int(self.max_damage/2) , self.max_damage )  
    
    def attack(self):
        return self.weapon_damage

         
            
if __name__ == "__main__":        
    weapon = Weapon("sward", 10)
    print(weapon)
    print(f"""
    name:        {weapon.name}
    max damage:  {weapon.max_damage}
    damage done: {weapon.attack()}
    """)

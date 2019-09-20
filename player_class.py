#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
from bag_class import Inventory, Item

class Player:
    def __init__(self, name:str = "", hp:int = 100, stamina:int = 100, attack: int = 100, sp_attack:int = 100): #Sets up player stats 
        self.name = name
        self.hp = hp
        self.stamina = stamina
        self.attack = attack
        self.sp_attack = sp_attack
        self.inventory = Inventory()

    def restore_hp(self, amount: int = 10) -> None:
        '''Restores player hp by the amount specified'''
        while self.hp < 100 and amount > 0:
            self.hp += 1
            amount -= 1

    def restore_stamina(self, amount: int = 5) -> None:
        '''Restores player stamina by the amount specified'''
        while self.stamina < 20 and amount > 0:
            self.stamina += 1
            amount -= 1

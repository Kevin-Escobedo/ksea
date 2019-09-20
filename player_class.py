#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com

class Player:
    def __init__(self, name:str = "", hp:int = 100, stamina:int = 20): #Sets up player stats 
        self.name = name
        self.hp = hp
        self.stamina = stamina

    def restore_hp(self, amount: int = 10):
        '''Restores player hp by the amount specified'''
        while self.hp < 100 and amount > 0:
            self.hp += 1
            amount -= 1

    def restore_stamina(self, amount: int = 5):
        '''Restores player stamina by the amount specified'''
        while self.stamina < 20 and amount > 0:
            self.stamina += 1
            amount -= 1

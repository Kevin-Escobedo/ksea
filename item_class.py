#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com

#TODO:
#Add item effects
#Decrement item use when used

class Item:
    def __init__(self, name:str = "", uses:int = 0):
        self.name = name
        self.uses = uses
        self.broken = False

    def check_broken(self) -> bool:
        '''Checks if the item can still be used'''
        if self.uses <= 0:
            self.broken = True
        return not self.broken

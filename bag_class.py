#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
from item_class import Item

class Inventory:
    def __init__(self):
        self.bag = dict()

    def add(self, item:Item) -> None:
        '''Adds item into the bag'''
        if item in self.bag:
            self.bag[item] += 1
        else:
            self.bag[item] = 1

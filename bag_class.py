#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
from item_class import Item

class Inventory:
    def __init__(self):
        self.bag = [] #Change later?

    def add(self, item:Item) -> None:
        '''Adds item into the bag'''
        self.bag.append(item)

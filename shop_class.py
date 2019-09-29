#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com

from item_class import Item

class Shop:
    def __init__(self):
        self.stock = self.get_items()

    def get_items(self):
        file = open("Resources/items.txt")

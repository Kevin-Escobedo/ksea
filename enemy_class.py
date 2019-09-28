#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com

from npc_class import NPC
import random

class Enemy(NPC):
    def __init__(self, name:str, race:str, life:float):
        NPC.__init__(self, name, race, life)

    def attack(self):
        #Maybe include different attacks based on race?
        return random.randrange(5,16) #Change later


#Authors: u/gonano4, Kevin C. Escobedo

#TODO:
#Should we make race into a class?
#And make each different race have their own characteristics?

class NPC:
    def __init__(self, name: str = "", race:str = "", life:float = 0.0):
        self.name = name
        self.race = race
        self.life = life

    def speak(self, dialogue:str):
        '''Returns dialogue for NPC to say'''
        return dialogue

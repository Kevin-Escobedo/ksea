from player_class import Player, Inventory, Item
import time
import pickle
#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com

class Gameplay:
    def __init__(self):
        try:
            file = open("save_file.sav", "rb")
            self.player = pickle.load(file)
            file.close()
            print("Loaded Player {}".format(self.player.name))
        except FileNotFoundError:
            self.player = self.start_tutorial()

    def start_tutorial(self):
        '''Plays if there is no save file'''
        player_name = self.get_name()
        time.sleep(2)
        player_type = self.get_type()

        if player_type == "Special":
            player = Player(name = player_name, attack = 25, sp_attack = 50)
            print("Valder: Great! You can have this Spellbook, it's about flames")
            player.inventory.add(Item("Flame Spellbook", 50, 50))
        else:
            player = Player(name = player_name, attack = 50, sp_attack = 25)
            print("Valder: Then have this Iron Sword, it will keep you safe")
            player.inventory.add(Item("Iron Sword", 50, 50))

        file = open("save_file.sav", "wb")
        pickle.dump(player, file)
        file.close()

        return player

    def get_name(self) -> None:
        name = input("Unknown: Hello, welcome to the fantastic world of Ksea!\nPlease tell me your name: ")
        print("{}, a great name for and adventurer!\nI am Valder, The Master of the fire".format(name))
        return name

    def get_type(self) -> None:
        player_type = input("Valder: As you are new to Ksea, I'll ask you a question\nValder: Are you familiar with magic, yes or no? ")
        if player_type.lower() in ["yes", "y", "1"]:
            return "Special"
        else:
            return "Physical"
        


if __name__ == "__main__":
    g = Gameplay()

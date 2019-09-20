print("Unknown:Hello, welcome to the fantastic world of Ksea,what is your name?")
name=input()
print(name+",","a great name for and adventurer,i am Valder, The Master of the fire")
import time
time.sleep(2)
print("Valder:as you are new to Ksea i´ll ask you a question")
time.sleep(2)
print("Valder:Are you familiar with magic, yes or no?")
var=input()
time.sleep(.5)
if var == "yes":
    print("Valder:great so you can have this spellbook, it´s about flames")
else:
    print("Valder:then have this iron sword, it will keep you safe")
time.sleep(1)
print("Valder:folow me")
time.sleep(5)
print("||Valder and",name,"enter on a pine forest||")  
time.sleep(3)
print("||the forest isstrange at all but bot of them keep going||")
print("||suddenly an orc comes out of the woods with a battle axe and an assassin look||")
time.sleep(1)
found=False
if var =="yes":
    while(found == False):
        print("*what do you use?*")
        var99=input()
        src_str = var99
 
        sub_index = src_str.find('flames')
 
        if sub_index > -1 :
            print("the flames were efective and the orc is now ash")
            found = True
        else:
            found = False
            print("try again")
if var =="no":
    while(found == False):
        print("*what do you use?*")
        var100=input()
        src_str = var100
 
        sub_index = src_str.find('sword')
 
        if sub_index > -1 :
            print("the sword was effective and the orc lies beheaded on the ground")
            found = True
        else:
            foud = False
            print("try again")
if found==True:
    time.sleep(5)
    print("Valder:well done, not all the pople can say they killed an orc")
    time.sleep(2)
    print("Valder:come on, we have a long journey until the next village")
    time.sleep(4)
    import os
    os.system("cls")
    print("||travelling...||")
    time.sleep(15)
    print("||you arrive at Sanctur||")
    time.sleep(2)
    os.system("cls")
    print("Valder:here you have 100 coins for saving me today choose wisely where to spend them")
    coins = 100
    time.sleep(2)
    
if var == "yes":
    print("||you get into a library, you can buy a)sparks spell, b)freeze spell, or c)wolf spell, what do you buy?||")
    var3=input()

else:
    print("||You arrive at the blacksmith, can buy a) better sword, b)mace or c)axe, what do you buy?||")
    var4=input()

    
        
if var3 == "a":
    print("Mage:congrats! sparks is an awsome spell")
if var3 == "b":
    print("Mage:congrats! freeze is an awsome spell")
if var3 == "c":
    print("Mage:congrats! invocated wolf is an awsome spell")
time.sleep(2)
print("you have 25 coins left")

if var4 == "a":
    print("Mage:congrats! you purchased a steel sword")
if var4 == "b":
    print("Mage:congrats! you purchased a steel axe")
if var4 == "c":
    print("Mage:congrats! you purchased steel mace")
time.sleep(2)

coins = coins-75
print("you have",coins, "coins left")
time.sleep(5)
print("Valder:lets go to sleep")
os.system("cls")
print("||sleeping...||")
time.sleep(15)
print("You awake full recovered")

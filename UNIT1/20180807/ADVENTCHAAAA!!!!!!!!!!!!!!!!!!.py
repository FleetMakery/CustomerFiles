import random

hp=5
exp=0
v90=("gold block")
x95=("bread and cheese")
name=input("Type in your adventurers name")
print("Welcome",name,"to the...")
print("""
The floor of the cave is now mostly submerged
beneath inky black water. Your shoes give up the battle to keep the water out and you walk with a steady squelch.
""")

from time import sleep
sleep(3.0)
print("You spot a fierce rat in the center of the tunnel")
event1 = input("Press s to sneak by. Press t to throw stone at it")
if event1 == ("s"):
    print("Carefully you edge past")
else:
    print("You throw a stone at the rat and it runs off")


sleep(2.0)

print("The rat turns its head towards you")

if event1 == ("s"):
    print("Carefully you edge past")
    exp=exp+2
else:
    print("You throw a stone at the rat")
    print("It attacks you")
sleep(5.0)
print("After a struggle it runs off")
exp=exp+1    
hp=hp-1

print("You have",exp,"point")
print("You have",hp,"hit points left")

print("Your rucksack contains:")
playerrucksack = ["gold coin","rope","cheese roll"]
chest1 = ["ruby","emerald","Wand of Doom"]
playerrucksack = playerrucksack +chest1
print(playerrucksack)


choice3 = input("Type a to attack, b to back away or c to creep past.") 
if choice3 == "a":
     print("You attack with your terrible sword")
elif choice3 == "b":
     print("You back away quietly")
else:
     print("Carefully you sneak past")
     random.choice(["a","b","c"])
     import sys
if hp <= 0:
    print("Your hero is dead")
    sys.exit(0)
else:
    print("You won!!!")
    




from time import sleep
hp=5
exp=0

def death_test():
    if hp==0:
        print ("Your hero is dead")
        exit()
    
name=input("Type in your adventurers name: ")
print("Welcome",name,"to Russia")
print ("""
The wooden floor gives out from under your feet as the steady fire attacks the floor
and engulfs the cave with fire and the blackness surrounds you as you fall down...
down... down... and land on a piano and its a soft landing because theres a fat guy on it.
You hear his groans fill your surroundings. You a lose a hp but you gain an ep.
""")
sleep(20.0)
hp=hp-1
exp=exp+1
print("You have",exp,"point")
print("You have",hp,"hit points left")
death_test()
print("He tries to attack you.")
event1=input("Press f to fight back. Press r to run away.")
if event1 == ("f"):
       print("You fight back and win. You gain exp.")
       exp=exp+1
else:
       print ("You run away.")
death_test()
print("You have",exp,"point")
print("You have",hp,"hit points left")
print("""
You see a magical sword on the ground. You check your rucksack and see what is in there.There is:
""",rucksack)
sleep(10.0)
rucksack = ("Picture","Potion","Dead rat","galculator","compass","food item")
sword = input("Would you like to replace an item in your rucksack with a sword?": )
if sword == ("yes" or "Yes"):
    pictureremove = input ("would you like to remove the picture?: ")
    if pictureremove = ("yes" or "Yes")
    else:
        potionremove = input ("would you like to remove the potion: ")

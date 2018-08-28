from time import sleep
import sys
hp=3
exp=0
name=input("Type in your adventurers name")
print("Welcome",name,"to the.....")
print("""
You spot man-eating spider in the centre of the cave
""")
event1 = input("Press a to sneak past.Press s to throw a stick at it")
if event1 ==("a"):
    print("Carefully you edge past")
    exp=exp+2
else:
    print("You throw a stick at the man-eating spider")
    print("It attacks you")
    sleep(5.0)
    print("After a struggle it scurries off")
    exp=exp+1
    hp=hp-2
    print("You have",exp,"point")
    print("You have",hp,"hit points left")

    backpack = ["gold coin","rope","tuna sandwich"]
print(backpack)
print("""
You find a bow and arrow on the floor
""")
event2 = input("Press a to pick up.")
if event2 ==("a"):
    print("Bow and arrow added to your backpack")
backpack.append("bow and arrow")
print(backpack)
print("""
You find a chest behind a tree
""")
event3 = input("Press a to open")
if event3 ==("a"):
    print("Contents of the chest are added to yor backpack")
    chest1 = ["ruby","emerald","sniper rifle"]
backpack = backpack +chest1

print(backpack)
print("""
You spot a fierce mutant rat
""")
choice1 = input("Type a to atttack,b to back away or c to sneak past.")
if choice1 ==("a"):
    print("You attack with your bow and arrow")
    sleep(5.0)
    print("It attacks you")
    print("You hit it and it gets knocked out")
    exp=exp+1
    hp=hp-1
    
    print("You have",exp,"point")
    print("You have",hp,"hit points left")
    

elif choice1 ==("b"):
    print("You back away quietly")
    exp=exp+1
    print("You have",exp,"points")
    print("You have",hp,"hit points left")
else:
    print("Carefully you creep past")
    exp=exp+2
    print("You have",exp,"points")
    print("You have",hp,"hit points left")


if hp <= 0:
    print("Your hero is dead")
    sys.exit(0)
    
    
    
    


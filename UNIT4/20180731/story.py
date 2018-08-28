import time
hp=5
exp=0
name=input("Type in your adventurers name: ")
print("Welcome",name,"to the toilet gang")

print("""
you need to find the magic stone to win
""")




print("you will be shot, you need to either move or stay still")
event1 = input('Press m to move press s to stay still: ')
if event1 == ("m"):
    print('The shooter anticipated this, you are shot, but its okay')
else:
    print('you didnt move, the shooter thought you would so you are safe')

print("You see a gold coin and a fish, you can only carry one object")
event1 = input('Press g to take the gold coin press f to take the fish: ')
print ('Both objects ran away so you cant get them')


print ('someone tries to attack them')
ans = input('press p to punch back, press d to dodge')
if ans == 'p':
    print('you both punch each other, you are both hurt')
    hp = hp - 1
else :
    print('you didnt get punched and the attacked dies and vanished')
    



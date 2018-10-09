import random
from time import sleep
class Place():
    def __init__(self, name=None, pos=None):
        self.name = name
        self.pos = pos
        self.routes = []

    def __str__(self):
        return 'place is {} your possible routes are:\n\t{}'.format(self.name, '\n\t'.join([str(x) for x in self.routes]) )
        
#for each place



class Route():
    def __init__(self, start=None,end=None, distance=0):
        self.start = start
        self.end = end
        self.distance = distance

    def __str__(self):
        return "The start is {} and the end is {} and the distance is {}".format(self.start.name,self.end.name,self.distance)

    #'the start is '+self.start+' and the end is '+self.end+' and the distance is '+str(self.distance)


#routes

hook = Place(name='Hook',pos=[1,2])
fleet = Place(name='Fleet',pos=[2,1])
basingstoke = Place(name='Basingstoke',pos=[0,1])
guildford = Place(name='Guildford',pos =[1,0])
reading = Place(name='Reading', pos=[2,3])
woking = Place(name='Woking',pos=[2,-1])
#each place

hooktofleet = Route(start=hook,end=fleet,distance=2)
fleettohook = Route(start=fleet,end=hook,distance=2)
hooktobasingstoke = Route(start=hook,end=basingstoke,distance=1)
basingstoketohook = Route(start=basingstoke,end=hook,distance=1)
basingstoketoguildford = Route(start=basingstoke,end=guildford,distance=1)
guildfordtobasingstoke = Route(start=guildford,end=basingstoke,distance=1)
guildfordtofleet = Route(start=guildford,end=fleet,distance=3)
fleettoguildford = Route(start=fleet,end=guildford,distance=3)
guildfordtowoking = Route(start=guildford,end=woking,distance=1)
wokingtoguildford = Route(start=woking,end=guildford,distance=1)
fleettowoking = Route(start=fleet,end=woking,distance=3)
wokingtofleet = Route(start=woking,end=fleet,distance=3)
fleettoreading = Route(start=fleet,end=reading,distance=4)
readingtofleet = Route(start=reading,end=fleet,distance=4)
hooktoreading = Route(start=hook,end=reading,distance=2)
readingtohook = Route(start=reading,end=hook,distance=2)
#each route
hook.routes = [hooktofleet, hooktobasingstoke, hooktoreading]
fleet.routes = [fleettohook, fleettoguildford, fleettoreading, fleettowoking]
guildford.routes = [guildfordtobasingstoke, guildfordtofleet, guildfordtowoking]
basingstoke.routes  = [basingstoketoguildford, basingstoketohook]
woking.routes = [wokingtoguildford, wokingtofleet]
reading.routes = [readingtofleet, readingtohook]

def can_i_get_there_from_here(start_place, dest_place):
    for item in start_place.routes:
        #print(item.end.name)
        if item.end.name == dest_place.name:
            return True
    return False


def take_me_to_my_desired_destination_randomly(start_location, desired_destination, maxlimit=20):
    current_location = start_location
    temproute = None
    totaldistance = 0
    while current_location.name != desired_destination.name:
        temproute=random.choice(current_location.routes)
        totaldistance = totaldistance+temproute.distance
        print(current_location,totaldistance,temproute)
        current_location=temproute.end
        sleep(1)
        if totaldistance > maxlimit:
            break
    if current_location == desired_destination:
        print('you have reached your destination')
    else:
        print('you keeled over, exhausted')
    
def take_me_to_my_desired_destination(start_location, desired_destination, maxlimit=20):
    current_location = start_location
    temproute = None
    totaldistance = 0
    while current_location.name != desired_destination.name:
        direction_to_dest = current_location.pos[1] - desired_destination.pos[1]
        for route in current_location.routes:
            route_direction = route.start.pos[1] - route.end.pos[1]
        totaldistance = totaldistance+temproute.distance
        #print(current_location,totaldistance,temproute)
        current_location=temproute.end
        #sleep(1)
        if totaldistance > maxlimit:
            break
    if current_location == desired_destination:
        print('you have reached your destination')
    else:
        print('you keeled over, exhausted')
















#import random
class Place():
    def __init__(self, name=None):
        self.name = name
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

hook = Place(name='Hook')
fleet = Place(name='Fleet')
basingstoke = Place(name='Basingstoke')
guildford = Place(name='Guildford')
#each place

hooktofleet = Route(start=hook,end=fleet,distance=2)
fleettohook = Route(start=fleet,end=hook,distance=2)
hooktobasingstoke = Route(start=hook,end=basingstoke,distance=1)
basingstoketohook = Route(start=basingstoke,end=hook,distance=1)
basingstoketoguildford = Route(start=basingstoke,end=guildford,distance=1)
guildfordtobasingstoke = Route(start=guildford,end=basingstoke,distance=1)
guildfordtofleet = Route(start=guildford,end=fleet,distance=3)
fleettoguildford = Route(start=fleet,end=guildford,distance=3)
#each route
hook.routes = [hooktofleet, hooktobasingstoke]
fleet.routes = [fleettohook, fleettoguildford]
guildford.routes = [guildfordtobasingstoke, guildfordtofleet]
basingstoke.routes  = [basingstoketoguildford, basingstoketohook]


def can_i_get_there_from_here(start_place, dest_place):
    for item in start_place.routes:
        #print(item.end.name)
        if item.end.name == dest_place.name:
            return True
    return False


# def take_me_to_my_desired_destination(current_location, desired_destination)
#     dest=random.choice(current_location.end.name)
#     if dest == desired_destination  

































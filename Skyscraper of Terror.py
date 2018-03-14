from Inventory import Flashlight


class Room():
    def __init__(self, name, description, id):
        self.name = name
        self.description = description
        self.id = id
        self.items = []
        self.connectors = []
        self.rooms = {}

    def add_item(self, item):
        self.items.append(item)

    def add_room(self, direction, room):
        self.rooms[direction] = room

    def add_connection(self, room, connector, actions):
        for direction in actions:
            self.rooms[direction] = room
        self.connectors.append((connector, actions[0]))

    def enter_room(self):
        print self.name
        print
        print self.description
        print
        if len(self.connectors) > 0:
            for connector in self.connectors:
                print "There is a " + connector[0] + \
                      " that goes " + connector[1]

    def get_name(self):
        return self.name

    def is_valid_direction(self, direction):
        return direction in self.rooms.keys()

    def next_room(self,direction):
        return self.rooms[direction]



kitchen = Room('kitchen', 'You are in the kitchen.', 'k')
dining = Room('dining room','You are in the dining room', 'd')
hallway = Room('hallway', 'You are in the hallway', 'h')
hallway2 = Room('upstairs Hallway', 'You are in the hallway', 'uh')
bedroom1 = Room('bedroom', 'You are in a bedroom', 'b1')
bedroom2 = Room('bedroom', 'You are in a bedroom', 'b2')
bedroom3 = Room('bedroom', 'You are in a bedroom', 'b3')
living = Room('living Room', 'You are in the living room', 'lr')

kitchen.add_connection(dining, "passage", ["east", "e"])
dining.add_connection(kitchen, "passage", ["west", "w"])



#kitchen.add_room('n', dining)
#dining.add_room('s', kitchen)
#dining.add_room('n', hallway)
#hallway.add_room('s', dining)
#hallway.add_room('u', hallway2)
#hallway.add_room('e', living)
#living.add_room('w', hallway)
#hallway2.add_room('d', hallway)
#hallway2.add_room('n', bedroom1)
#hallway2.add_room('e', bedroom2)
#hallway2.add_room('w', bedroom3)
#bedroom1.add_room('s', hallway2)
#bedroom2.add_room('w', hallway2)
#bedroom3.add_room('e', hallway2)




current_room = kitchen
current_room.enter_room()

while True:
    direction = raw_input("What direction do you want to go?")
    if direction == 'x':
        break
    elif current_room.is_valid_direction(direction):
        current_room = current_room.next_room(direction)
        current_room.enter_room()
    else:
        print "Ouch! You ran into a wall."














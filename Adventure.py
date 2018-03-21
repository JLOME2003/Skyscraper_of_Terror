from room import Room
from Inventory import Inventory, Flashlight, DarkRoom, LightSource

helipad = Room('You have parachuted from a helicopter on a special mission to save the president inside of the Empire State Building from ZOMBIES', 'You are on the Empire State Building helipad and start to look around for a way to enter the building', 'h')
staircase = Room('You open the door that leads to the staircase and you proceed to go down','After fending off 15 zombies you are now inside the building', 'd')
hallway = Room('You start to walk down the hallway until you are ambushed by a herd of zombies and you pull out your pistol and shoot at them in an attempt to fight them off', 'After facing off with an enormous herd of zombies you are now exhausted but ready to continue on with your mission', 'h')
lobby = Room('In order to avoid another encounter with zombies you crouch down and start to apply your cloaking device to avoid detection. You start to carefully deploy explosives in various areas of the lobby. After deploying the explosives, you walk back a safe distance from the explosives and proceed to detonate them. ', 'Now that you have successfully eliminated all the zombies in the you stand in the middle of the blood ridden lobby, thinking about all the choices you made that led you to this point in life', 'uh')
kitchen = Room('After contemplating life you look around for another way to get deeper into the building and you spot a door that leads into the kitchen', 'After many attempts at forcefully pushing the door open, you are finally inside the kitchen and there still seems to be no sign of the president', 'b1')
ceo_office = Room('You continue to venture deeper into the kitchen and you stumble upon the CEO office', 'The door of the office was wide open so you walked in but as soon as you entered the office you were attacked by a zombie that came out from behind the office door but fortunately the zombie had no legs so you stomped it out', 'b2')
trapdoor = Room('You start to look at the dark oak table in the center of the office and you notice a small metal hatch under the desk', 'You opened the hatch and you fell into what seemed like an underground tunnel and you proceed to walk forward because that is the only way you can go', 'b3')
living = Room('living Room', 'You are in the living room', 'lr')

helipad.add_connection(staircase, "staircase", ["east", "e"])
staircase.add_connection(hallway, "dark and quiet hallway", ["west", "w"])
hallway.add_connection(lobby, "lobby entirely full of zombies", ["north", "n"])
lobby.add_connection(kitchen, "large metal kitchen door that seems to be blocked off from the other side", ["south", "s"])
kitchen.add_connection(ceo_office, "office that belongs to the CEO of the building", ["west", "w"])
ceo_office.add_connection(trapdoor, "You teleport back to the helipad", ["east", "e"])
trapdoor.add_connection(helipad, "")

current_room = helipad
inventory = Inventory()


inventory = Inventory()
current_room = helipad

kitchen.add_item(Flashlight())


while True:
    current_room.enter_room(inventory)
    command = raw_input("What would you like to do? ")
    if command in ["exit", "x", "quit", "q"]:
        break

    result = current_room.process_command(command, inventory)
    if isinstance(result, Room):
        current_room = result
        result.enter_room(inventory)
        continue
    elif isinstance(result, str):
        print result
        continue
    else:
        print "I don't know what you mean"






























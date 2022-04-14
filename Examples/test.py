class Room():
    def __init__(self,
                 description: str = " ",
                 north: str = "north",
                 east: str = "east",
                 south: str = "south",
                 west: str = "west"):
        self.description: str = " "
        self.north: str = north
        self.east: str = east
        self.south: str = south
        self.west: str = west

def main():
    room_list = Room()

    room_list.description = "You are currently in the second bedroom. There is a door to the north."
    room_list.north = None
    room_list.east = 1
    room_list.south = None
    room_list.west = None
    room_list.append = 0

    current_room = 0

    print(room_list.description)

    room_list.description = " You are in the south hall"
    room_list.north = 4
    room_list.east = 2
    room_list.south = None
    room_list.west = 0
    room_list.append = 1

    room_list.description = "This is the dining room"
    room_list.north = None
    room_list.east = None
    room_list.south = None
    room_list.west = 1
    room_list.append = 2

    room_list.description = "This is the second bedroom in the house"
    room_list.north = None
    room_list.east = 4
    room_list.south = None
    room_list.west = None
    room_list.append = 3

    room_list.description = "You are in the north hall"
    room_list.north = 6
    room_list.east = 5
    room_list.south = 1
    room_list.west = 3
    room_list.append = 4

    room_list.description = "You are in an empty kitchen"
    room_list.north = None
    room_list.east = None
    room_list.south = None
    room_list.west = 1
    room_list.append = 5

    room_list.description = "You are outside standing on the balcony"
    room_list.north = None
    room_list.east = None
    room_list.south = 4
    room_list.west = None
    room_list.append = 6


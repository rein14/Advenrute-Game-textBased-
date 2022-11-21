"""
    Create a room described "description". Initially, it has
    no exits. The 'description' is something like 'kitchen' or
    'an open court yard'.
"""
from player import Player
import random
class Room:

    def __init__(self, description, lock= False):
        """
            Constructor method.
        :param description: Text description for this room
        """
        self.description = description
        self.exits = {}  # Dictionary
        self.room_items = []
        self.player = Player()
        key = self.player.key
        self.lock = True
        
    # def unlock(self, key):
    #     self.lock = False 
    def set_exit(self, direction, neighbour):
        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room).
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour
    
    def get_short_description(self):
        """
            Fetch a short text description.
        :return: text description
        """
        return self.description

    def get_long_description(self):
        """
            Fetch a longer description including available exits.
        :return: text description
        """
        return f'Location: {self.description}, Exits: {self.get_exits()}.\n with ITEMS: {self.player.bagpack} in your bagpack'
    
    
    def get_exits(self):
        """
            Fetch all available exits as a list.
        :return: list of all available exits
        """
        all_exits = list(self.exits.keys())
        return all_exits

    
    def get_exit(self, direction):
        """
            Fetch an exit in a specified direction.
        :param direction: The direction that the player wishes to travel
        :return: Room object that this direction leads to, None if one does not exist
        """
        if direction in self.exits:
            if direction == self.get_exits()[-1]:
                if self.room_items:
                    item = random.choice(self.room_items)
                    item = self.player.pick_item(item, self.room_items)
                    print("**********************************")
                    print(f"You picked up {item} as sourvenir")
                    print(self.player.get_picked_items())
                else:
                    print("no sourvenir found")
            else:
                print("sourvenir is not in this locatiion")
            return self.exits[direction]

    def set_item(self, item):
        """
        Add a new item to the list of room items
        :return: None
        """
        self.room_items.append(item)
    
    def set_room_key(self):
        self.room_key = True
        key = self.room_key
        return key
    
    def get_room_key(self):
        pass
        # if self.lock is True:

             # return self.room_key
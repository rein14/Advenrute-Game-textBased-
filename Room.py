"""
    Create a room described "description". Initially, it has
    no exits. The 'description' is something like 'kitchen' or
    'an open court yard'.
"""

from dataclasses import dataclass
import random


@dataclass
class User:
    """
    Initialize user properties
    """
    key = bool
    LIMIT = 5
    bagpack = []


class Room:

    def __init__(self, description, lock= False):
        """
            Constructor method.
        :param description: Text description for this room
        """
        self.description = description
        self.exits = {}  # Dictionary
        self.room_items = []
        self.user = User()
        key = self.user.key
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
        return f'Location: {self.description}, Exits: {self.get_exits()}.\n with ITEMS: {self.user.bagpack} in your bagpack'
    
    
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
                    item = self.pick_item(item)
                    print("**********************************")
                    print(f"You picked up {item} as sourvenir")
                    print(self.user.bagpack)
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
    

    def pick_item(self, item):
        """
        Add an item to bagpack.
        :param item: Item to be added to bagpack
        :return: None
        """

        if len(self.user.bagpack) < self.user.LIMIT:
            if item in self.room_items:
                self.user.bagpack.append(item)
        else:
            self.user.bagpack.pop(0)
            self.user.bagpack.append(item)

        return item




    def get_item(self, item):  
        """
        Fetch an item from bagpack 
        :param item: Item to retrieve
        :return: item
        """ 
        if item in self.user.bagpack:
                return self.user.bagpack[item]

    def get_picked_items(self):

       """
       Fetch what you have picked up in your bagpack
       :return: list   
       """
       return self.user.bagpack
    
    def set_room_key(self):
        self.room_key = True
        key = self.room_key
        return key
    
    def get_room_key(self):
        pass
        # if self.lock is True:
            
        # return self.room_key
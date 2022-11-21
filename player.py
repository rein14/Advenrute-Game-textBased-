from dataclasses import dataclass


@dataclass
class Player:
    """
    Initialize user properties
    """
    key = bool
    LIMIT = 5
    bagpack = []

    
    def pick_item(self, item, room_items):
        """
        Add an item to bagpack.
        :param item: Item to be added to bagpack
        :return: None
        """

        if len(self.bagpack) < self.LIMIT:
            if item in room_items:
                self.bagpack.append(item)
        else:
            self.bagpack.pop(0)
            self.bagpack.append(item)

        return item


    def get_picked_items(self):

       """
       Fetch what you have picked up in your bagpack
       :return: list   
       """
       return self.bagpack
    


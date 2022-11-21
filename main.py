from room import Room
from textUI import TextUI
from abc import abstractclassmethod, ABC


class Game:

    def __init__(self):
        """
        Initialises the game.
        """
        self.create_rooms()
        self.current_room = self.outside
        self.textUI = TextUI()

        
    def create_rooms(self):
        """
            Sets up all room assets.
        :return: None
        """
        self.outside = Room("You are outside")
        self.lobby = Room("in the lobby", lock=True)
        self.corridor = Room("in a corridor")
        self.lab = Room("in a computing lab")
        self.office = Room("in the computing admin office")
        self.first_floor = Room("Going upstairs")
        self.restroom = Room("In the restroom")
        self.garage = Room("In the garage")
        self.storeroom = Room("In the storeroom")
        self.warroom = Room("In the warroom")

        self.outside.set_exit("east", self.lobby)
        self.outside.set_exit("south", self.lab)
        self.outside.set_exit("west", self.corridor)
        self.lobby.set_exit("west", self.outside)
        self.corridor.set_exit("east", self.outside)
        self.lab.set_exit("north", self.outside)
        self.lab.set_exit("east", self.office)
        self.office.set_exit("west", self.lab)
        self.office.set_exit("upstairs", self.first_floor)
        self.first_floor.set_exit("upstairs", self.restroom )
        self.restroom.set_exit("west", self.garage)
        self.storeroom.set_exit("north", self.warroom)
        self.warroom.set_exit("south", self.outside)
        self.garage.set_exit("east", self.outside)
        self.outside.set_item("key")
        self.outside.set_item("pen")
        self.office.set_item("stapeler")
        self.first_floor.set_item("key")
        self.first_floor.set_item("pencil")
       



    def do_go_command(self, second_word):
        """
            Performs the GO command.
        :param second_word: the direction the player wishes to travel in
        :return: None
        """
        if second_word == None:
            # Missing second word...
            self.textUI.print_to_textUI("Go where?")
            return

        next_room = self.current_room.get_exit(second_word)
        # pick_item = self.current_room.pick_item("weapon")
        if next_room == None:
            self.textUI.print_to_textUI("There is no door!")
        else:
            self.current_room = next_room
            self.textUI.print_to_textUI(self.current_room.get_long_description())


class GameOptions:

    def __init__(self):
        """
        Initialises Game options and properties
        """
        self.textUI = TextUI()
        self.game = Game().do_go_command
  
    def play(self):
        """
            The main play loop.
        :return: None
        """
        self.print_welcome()
        finished = False
        while not finished:  # while (finished == False):
            command = self.textUI.get_command()  # Returns a 2-tuple
            finished = self.process_command(command)
        print("Thank you for playing!")

    def print_welcome(self):
        """
        Displays a welcome message.
        :return:
        """
        self.textUI.print_to_textUI(f"\nYou are lost. You are alone. You wander around the deserted complex \
                                        \nYour command words are: {self.show_command_words()}.'")
   
    def show_command_words(self):
        """
            Show a list of available commands.
        :return: None
        """
        return ['help', 'go', 'quit']

    def process_command(self, command):
        """
        Process a command from the TextUI.
        :param command: a 2-tuple of the form (command_word, second_word)
        :return: True if the game has been quit, False otherwise
        """
        command_word, second_word = command
        if command_word is not None:
            command_word = command_word.upper()

        want_to_quit = False
        if command_word == "HELP":
            self.print_help()
        elif command_word == "GO":
            self.game(second_word)
        elif command_word == "QUIT":
            want_to_quit = True
        else:
            # Unknown command...
            self.textUI.print_to_textUI("Don't know what you mean.")

        return want_to_quit

    def print_help(self):
        """
            Display some useful help text.
        :return: None
        """
        self.textUI.print_to_textUI(f"\nYou are lost. You are alone. You wander around the deserted complex \
                                        \nYour command words are: {self.show_command_words()}.'")


def main():
    game = GameOptions()
    game.play()

if __name__ == "__main__":
    main()









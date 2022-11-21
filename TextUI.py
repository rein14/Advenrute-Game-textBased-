"""
    A simple text based User Interface (UI) for the Adventure World game.
"""

class TextUI:

    def __init__(self):
        # Nothing to do...
        pass

    def get_command(self):
        """
            Fetches a command from the console.
        :return: a 2-tuple of the form (command_word, second_word)
        """
        word1 = None
        word2 = None
        print('> ', end='')
        input_line = input()
        if input_line != "":
            all_words = input_line.split()
            word1 = all_words[0]
            if len(all_words) > 1:
                word2 = all_words[1]
            else:
                word2 = None
            # Just ignore any other words
        return(word1, word2)

    def print_to_textUI(self, text):
        """
            Displays text to the console.
        :param text: Text to be displayed
        :return: None
        """
        print(text)


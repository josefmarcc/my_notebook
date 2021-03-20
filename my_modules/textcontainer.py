str_to_test = "test this string"


class TextContainer():
    """A TextContainer consists of a list of text."""

    def __init__(self, txt):
        """Initialize the TextContainer with text."""
        self.txt = txt

    def word_count(self):
        """Print the amount of words in the txt."""
        return print(len(self.txt.split()))

    def char_count(self):
        """Print the amount of chars in the txt."""
        return print(len([char for char in self.txt]))


TextContainer(str_to_test).word_count()

TextContainer(str_to_test).char_count()

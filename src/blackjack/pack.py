# pack.py

class Pack:
    def __init__(self):
        self.__size = 52

    @property
    def size(self):
        return self.__size

    def get_card(self):
        return Card()

class Card:
    pass

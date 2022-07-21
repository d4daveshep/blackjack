import enum


class Suits(enum.Enum):
    Hearts = "Hearts"
    Clubs = "Clubs"
    Diamonds = "Diamonds"
    Spades = "Spades"

class Card:
    def __init__(self, suit):
        if isinstance(suit, Suits):
            self.__suit = suit
        else:
            raise TypeError(f"\'{suit}\' is not a valid suit")


    @property
    def suit(self):
        return self.__suit

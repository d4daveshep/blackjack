import enum

class Card_Names(enum.Enum):
    Ace = "Ace"
    Two = "2"
    Three = "3"
    Four = "4"
    Five = "5"
    Six = "6"
    Seven = "7"
    Eight = "8"
    Nine = "9"
    Ten = "10"
    Jack = "Jack"
    Queen = "Queen"
    King = "King"

class Suits(enum.Enum):
    Hearts = "Hearts"
    Clubs = "Clubs"
    Diamonds = "Diamonds"
    Spades = "Spades"

class Card:
    def __init__(self, name, suit):
        if isinstance(name, Card_Names):
            self.__name = name
        else:
            raise TypeError(f"\'{name}\' is not a valid card name")
        if isinstance(suit, Suits):
            self.__suit = suit
        else:
            raise TypeError(f"\'{suit}\' is not a valid suit")

    @property
    def name(self):
        return self.__name

    @property
    def suit(self):
        return self.__suit



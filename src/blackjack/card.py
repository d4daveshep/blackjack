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
    __card_values = {Card_Names.Ace: 11, Card_Names.Two: 2, Card_Names.Three: 3, Card_Names.Four: 4, Card_Names.Five: 5,
                     Card_Names.Six: 6, Card_Names.Seven: 7, Card_Names.Eight: 8, Card_Names.Nine: 9,
                     Card_Names.Ten: 10, Card_Names.Jack: 10, Card_Names.Queen: 10, Card_Names.King: 10}

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

    @property
    def value(self):
        return self.__card_values[self.name]

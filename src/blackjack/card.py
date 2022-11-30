import enum
from collections import namedtuple
from typing import NamedTuple


class Name(enum.Enum):
    ACE = "Ace"
    TWO = "Two"
    THREE = "Three"
    FOUR = "Four"
    FIVE = "Five"
    SIX = "Six"
    SEVEN = "Seven"
    EIGHT = "Eight"
    NINE = "Nine"
    TEN = "Ten"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"


class Suit(enum.Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"


class CardFactory:
    def __init__(self):
        self.__cards = {}

    def get_card(self, name: Name, suit: Suit):
        key = (name, suit)
        card = self.__cards.get(key)
        if not card:
            card = self.__Card(name, suit)
            self.__cards[key] = card

        return card


    class __Card(NamedTuple):
        name: Name
        suit: Suit

        def is_ace(self):
            return self.name == Name.ACE





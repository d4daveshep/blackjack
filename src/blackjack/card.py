import enum
from typing import NamedTuple


class Name(enum.Enum):
    ACE = ("Ace", 1)
    TWO = ("Two", 2)
    THREE = ("Three", 3)
    FOUR = ("Four", 4)
    FIVE = ("Five", 5)
    SIX = ("Six", 6)
    SEVEN = ("Seven", 7)
    EIGHT = ("Eight", 8)
    NINE = ("Nine", 9)
    TEN = ("Ten", 10)
    JACK = ("Jack", 10)
    QUEEN = ("Queen", 10)
    KING = ("King", 10)


class Suit(enum.Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"


class Face(enum.Enum):
    UP = 1
    DOWN = 2


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

        @property
        def value(self) -> int:
            pass
            return self.name.value[1]

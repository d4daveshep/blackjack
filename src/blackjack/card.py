import enum
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

# class CardNames(enum.Enum):
#     Ace = "Ace"
#     Two = "2"
#     Three = "3"
#     Four = "4"
#     Five = "5"
#     Six = "6"
#     Seven = "7"
#     Eight = "8"
#     Nine = "9"
#     Ten = "10"
#     Jack = "Jack"
#     Queen = "Queen"
#     King = "King"


# class Suits(enum.Enum):
#     Hearts = "Hearts"
#     Clubs = "Clubs"
#     Diamonds = "Diamonds"
#     Spades = "Spades"


class Card(NamedTuple):
    name: Name
    suit: Suit

# class Card:
#     __card_values = {CardNames.Ace: 1, CardNames.Two: 2, CardNames.Three: 3, CardNames.Four: 4, CardNames.Five: 5,
#                      CardNames.Six: 6, CardNames.Seven: 7, CardNames.Eight: 8, CardNames.Nine: 9,
#                      CardNames.Ten: 10, CardNames.Jack: 10, CardNames.Queen: 10, CardNames.King: 10}
#
#     def __init__(self, name, suit):
#         if isinstance(name, CardNames):
#             self.__name = name
#         else:
#             raise TypeError(f"\'{name}\' is not a valid card name")
#         if isinstance(suit, Suits):
#             self.__suit = suit
#         else:
#             raise TypeError(f"\'{suit}\' is not a valid suit")
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def suit(self):
#         return self.__suit
#
#     @property
#     def value(self):
#         return self.__card_values[self.name]
#
#     def is_ace(self):
#         return self.__name == CardNames.Ace
#

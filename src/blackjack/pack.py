# pack.py


# Suits = ("Hearts", "Clubs", "Diamonds", "Spades")
# Names = ("A", "1", "2", "3", "4", "5", "6", "7"}
from blackjack.card import Card, Suits


class Pack:
    def __init__(self):
        self.__size = 52
        self.__cards = [Card(suit) for suit in Suits] * 13

    @property
    def size(self):
        return self.__size

    def get_cards(self, n=-1):
        if n == -1:
            return self.__cards
        elif 0 < n and n <= self.__size:
            return self.__cards[0:n]
        else:
            raise ValueError(f"Can't get {n} cards")



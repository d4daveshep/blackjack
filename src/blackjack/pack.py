# pack.py


# Suits = ("Hearts", "Clubs", "Diamonds", "Spades")
# Names = ("A", "1", "2", "3", "4", "5", "6", "7"}
from blackjack.card import Card, Suits, Card_Names


class Pack:
    def __init__(self):
        self.__cards = []
        for suit in Suits:
            for name in Card_Names:
                self.__cards.append(Card(name, suit))
        self.__size = len(self.__cards)

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



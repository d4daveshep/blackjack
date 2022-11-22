# pack.py

import random

from card import Card, Suit, Name


class Pack:
    def __init__(self):
        self.__cards = []
        for suit in Suit:
            for name in Name:
                self.__cards.append(Card(name, suit))
        self.__size = len(self.__cards)

    @property
    def size(self) -> int:
        return self.__size

    def show_cards(self, n: int = -1) -> list:
        if n == -1:
            return self.__cards
        elif 0 < n <= self.__size:
            return self.__cards[0:n]
        else:
            raise ValueError(f"Can't get {n} cards")

    def count_cards_left(self) -> int:
        return len(self.__cards)

    def deal_cards(self, n: int) -> list:
        dealt_cards = self.show_cards(n)
        del self.__cards[0:n]
        return dealt_cards

    def shuffle(self) -> None:
        random.shuffle(self.__cards)

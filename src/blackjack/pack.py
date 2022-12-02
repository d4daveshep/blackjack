# pack.py

import random

from blackjack.card import Suit, Name, CardFactory


class Pack:
    def __init__(self):
        self.__card_factory = CardFactory()
        self.__cards = []
        for suit in Suit:
            for name in Name:
                self.__cards.append(self.__card_factory.get_card(name, suit))
        self.__size = len(self.__cards)

    @property
    def size(self) -> int:
        return self.__size

    def show_cards(self, number_of_cards: int = -1) -> list:
        """
        Show the next cards in the pack without removing them
        :param number_of_cards:
        :return: list of cards
        """
        if number_of_cards == -1:
            return self.__cards
        elif 0 < number_of_cards <= self.__size:
            return self.__cards[0:number_of_cards]
        else:
            raise ValueError(f"Can't get {number_of_cards} cards")

    def count_cards_left(self) -> int:
        return len(self.__cards)

    def deal_cards(self, number_of_cards: int) -> list:
        """
        Deal a number of cards from the pack.  Cards dealt are removed from the pack
        :param number_of_cards:
        :return: list of cards
        """
        dealt_cards = self.show_cards(number_of_cards)
        del self.__cards[0:number_of_cards]
        return dealt_cards

    def shuffle(self) -> None:
        random.shuffle(self.__cards)

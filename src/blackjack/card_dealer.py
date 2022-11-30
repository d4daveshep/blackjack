from blackjack.card import CardFactory
from blackjack.pack import Pack


class CardDealer:

    def __init__(self, packs: int = 1):
        self.__number_of_packs = packs
        self.__pack = Pack()


    @property
    def number_of_packs(self):
        return self.__number_of_packs

    def number_of_cards_left(self):
        return self.__pack.count_cards_left()

    def deal_cards(self, number_of_cards: int) -> list:
        return self.__pack.deal_cards(number_of_cards)





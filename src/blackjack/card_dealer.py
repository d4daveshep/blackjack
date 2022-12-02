from blackjack.pack import Pack


class CardDealer:

    def __init__(self, number_of_packs: int = 1):
        self.__number_of_packs = number_of_packs
        self.__cards = self.__create_cards(self.__number_of_packs)
        # self.__pack = Pack()

    @property
    def number_of_packs(self):
        return self.__number_of_packs

    def number_of_cards_left(self):
        return len(self.__cards)

    def deal_cards(self, number_of_cards: int) -> list:
        """
        Deal a number of cards from the pack.  Cards dealt are removed from the pack
        :param number_of_cards:
        :return: list of cards
        """
        dealt_cards = self._show_cards(number_of_cards)
        del self.__cards[0:number_of_cards]
        return dealt_cards

    def _show_cards(self, number_of_cards: int = -1) -> list:
        """
        Show the next cards in the pack without removing them
        :param number_of_cards:
        :return: list of cards
        """
        if number_of_cards == -1:
            return self.__cards
        elif 0 < number_of_cards <= self.number_of_cards_left():
            return self.__cards[0:number_of_cards]
        else:
            raise ValueError(f"Can't get {number_of_cards} cards")

    def deal_card(self):
        return self.deal_cards(1)

    def __create_cards(self, number_of_packs: int) -> list:
        all_cards = []
        for _ in range(number_of_packs):
            pack = Pack()
            all_cards += pack.show_cards(-1)
        return all_cards

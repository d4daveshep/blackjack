
class CardDealer:

    def __init__(self, packs: int = 1):
        self.__packs = packs

    @property
    def packs(self):
        return self.__packs

    def number_of_cards_left(self):
        return self.__packs * 52

    def deal_cards(self, number_of_cards: int) -> list:
        return [i for i in range(number_of_cards)]





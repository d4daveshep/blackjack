from blackjack.card import Name, Suit


class Hand:
    def __init__(self):
        self.__cards = []

    def __len__(self):
        return len(self.__cards)

    def add(self, card) -> None:
        try:
            if not isinstance(card.name, Name):
                raise ValueError("card has no name")
            if not isinstance(card.suit, Suit):
                raise ValueError("card has no suit")
        except AttributeError as err_info:
            raise ValueError(f"{card} is not a card ")

        self.__cards.append(card)

    def aces(self) -> list:
        return list(filter(lambda card: card.is_ace(), self.__cards))

    def is_soft(self) -> bool:
        return bool(self.aces())

    def is_hard(self) -> bool:
        return not bool(self.aces())

    def is_blackjack(self) -> bool:
        """
        Blackjack hands contain 2 cards, an Ace and a 10 or picture card
        """
        if len(self) == 2 and len(self.aces()) == 1:  # and self.hard_value() == 21:
            return True
        else:
            return False

    @property
    def value(self) -> int:
        total = 0
        for card in self.__cards:
            total += card.value

        # if total > 21 and self.aces():
        #     for i in self.aces():
        #         total -= 10
        #         if total <= 21:
        #             break

        return total

    def hard_value(self) -> int:
        value = self.value
        for _ in self.aces():
            value += 10
            if value > 11:
                break
        return value

    def soft_value(self) -> int:
        return self.value

    def max_value(self) -> int:
        return self.value + len(self.aces()) * 10

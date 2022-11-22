import enum

from blackjack.card import Card


class Hand:
    def __init__(self, cards: list):
        self.__cards = cards

    def __len__(self):
        return len(self.__cards)

    def add(self, card: Card) -> None:
        assert isinstance(card, Card)
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
        if len(self) == 2 and len(self.aces()) == 1 and self.hard_value() == 21:
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


class Move(enum.Enum):
    Hit = "Hit"
    Stand = "Stand"
    Bust = "Bust"


class Strategy:
    @classmethod
    def decide_move(cls, hand: Hand) -> Move:
        if hand.value < 17:
            return Move.Hit
        elif hand.value <= 21:
            return Move.Stand
        else:
            return Move.Bust

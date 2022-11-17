from typing import NamedTuple

import pytest

from src.blackjack import card
from src.blackjack.card import CardNames, Suits


# Card = namedtuple("Card", "name suit")
class Card(NamedTuple):
    name: card.Name
    suit: card.Suit


def test_cards_are_immutable():
    nine_hearts = Card(card.Name.NINE, card.Suit.HEARTS)

    two_spades = Card("Two", "Spades")
    # assert two_spades.suit == Suits.Spades

    with pytest.raises(AttributeError) as err_info:
        nine_hearts.name = card.Name.TWO

    with pytest.raises(AttributeError) as err_info:
        nine_hearts.suit = card.Suit.CLUBS

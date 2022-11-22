import sys
from typing import NamedTuple

import pytest
sys.path.append("../")

# from blackjack import card
# from blackjack.card import CardNames, Suits


# Card = namedtuple("Card", "name suit")
from src.blackjack.card import Card, Name, Suit


def test_cards_are_immutable():
    nine_hearts = Card(Name.NINE, Suit.HEARTS)

    two_spades = Card("Two", "Spades")
    # assert two_spades.suit == Suits.Spades

    with pytest.raises(AttributeError) as err_info:
        nine_hearts.name = Name.TWO

    with pytest.raises(AttributeError) as err_info:
        nine_hearts.suit = Suit.CLUBS

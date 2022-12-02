from typing import NamedTuple

import pytest

from blackjack.card import Name, Suit, CardFactory


def test_create_card_by_factory():
    factory = CardFactory()
    nine_hearts = factory.get_card(Name.NINE, Suit.HEARTS)

    assert nine_hearts.name == Name.NINE
    assert nine_hearts.suit == Suit.HEARTS


def test_cant_create_card_without_factory():
    with pytest.raises(AttributeError) as err_info:
        illegal_card = CardFactory.__Card(Name.NINE, Suit.HEARTS)
        assert False, "Shouldn't be able to create card outside of factory"


def test_cards_are_immutable():
    factory = CardFactory()
    nine_hearts = factory.get_card(Name.NINE, Suit.HEARTS)

    with pytest.raises(AttributeError) as err_info:
        nine_hearts.name = Name.ACE

    with pytest.raises(AttributeError) as err_info:
        nine_hearts.suit = Suit.SPADES


def test_cards_are_singletons():
    factory = CardFactory()
    nine_hearts_1 = factory.get_card(Name.NINE, Suit.HEARTS)
    nine_hearts_2 = factory.get_card(Name.NINE, Suit.HEARTS)

    assert nine_hearts_1 is nine_hearts_2, "Cards are not singletons"





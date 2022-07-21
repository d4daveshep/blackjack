# test_pack_of_cards.py
import sys
import pytest

sys.path.append("../")

from blackjack.pack import Pack
from blackjack.card import Card, Suits


@pytest.fixture()
def pack():
    return Pack()

def test_should_create_pack_with_default_size(pack):
    assert pack.size == 52


def test_should_get_card_from_pack(pack):
    card = pack.get_cards(1)[0]
    assert card is not None
    assert isinstance(card, Card)


def test_should_get_all_cards_from_pack(pack):
    cards = pack.get_cards()
    assert len(cards) == pack.size


def test_card_should_have_valid_suit():
    card = Card
    with pytest.raises(TypeError) as error:
        card = Card("bogus")
    assert error.value.args[0] == "\'bogus\' is not a valid suit"

def test_should_get_full_pack_of_cards(pack):

    suits = {}

    for card in pack.get_cards():
        if card.suit not in suits:
            suits[card.suit] = 1
        else:
            suits[card.suit] += 1

    assert len(suits) == 4
    assert Suits.Hearts in suits
    assert Suits.Clubs in suits
    assert Suits.Diamonds in suits
    assert Suits.Spades in suits

    for suit in suits:
        assert suits[suit] == 13




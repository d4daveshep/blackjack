# test_pack_of_cards.py
import sys
import pytest

sys.path.append("../")

from blackjack.pack import Pack
from blackjack.card import Card, Suits, Card_Names


@pytest.fixture()
def pack():
    return Pack()

def test_should_create_pack_with_default_size(pack):
    assert pack.size == 52


def test_should_get_card_from_pack(pack):
    card = pack.show_cards(1)[0]
    assert card is not None
    assert isinstance(card, Card)


def test_should_get_all_cards_from_pack(pack):
    cards = pack.show_cards()
    assert len(cards) == pack.size


def test_card_should_have_valid_suit():
    card = Card(name=Card_Names.Ace, suit=Suits.Spades)
    assert card.suit == Suits.Spades

    with pytest.raises(TypeError) as error:
        card = Card(name=Card_Names.Ace, suit="bogus")
    assert error.value.args[0] == "\'bogus\' is not a valid suit"

def test_card_should_have_valid_name():
    card = Card(name=Card_Names.Ace, suit=Suits.Spades)
    assert card.name == Card_Names.Ace

    with pytest.raises(TypeError) as error:
        card = Card(name="bogus", suit=Suits.Spades)
    assert error.value.args[0] == "\'bogus\' is not a valid card name"

def test_should_show_full_pack_of_cards(pack):

    # build dictionaries of suits and names found.  value is the count of each
    found_suits = {}
    found_names = {}

    for card in pack.show_cards():
        if card.suit not in found_suits:
            found_suits[card.suit] = 1
        else:
            found_suits[card.suit] += 1

        if card.name not in found_names:
            found_names[card.name] = 1
        else:
            found_names[card.name] += 1

    # check the dictionaries contain the expected counted values
    assert len(found_suits) == 4  # should have found 4 suits
    for suit in Suits:
        assert suit in found_suits

    for suit in found_suits:
        assert found_suits[suit] == 13  # should be 14 of each suit

    assert len(found_names) == 13  # should have found 13 different card names
    for name in Card_Names:
        assert name in found_names

    for name in found_names:
        assert found_names[name] == 4  # should have found 4 of each card name

def test_should_deal_cards_from_pack(pack):
    assert pack.count_cards_left() == pack.size

    hand = pack.deal_cards(5)
    assert len(hand) == 5

    assert pack.count_cards_left() == (pack.size - 5)

def test_should_add_card_values(pack):

    hand = pack.deal_cards(5)
    expected_total = 11+2+3+4+5
    hand_total = 0

    for card in hand:
        hand_total += card.value

    assert hand_total == expected_total



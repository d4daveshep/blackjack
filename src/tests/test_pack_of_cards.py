# test_pack_of_cards.py
import sys

import pytest

from blackjack.card import CardFactory, Suit, Name
from fixtures import pack, cards



def test_should_create_pack_with_default_size(pack):
    assert pack.size == 52


def test_should_get_card_from_pack(pack):
    card_list = pack.show_cards(1)
    card_0 = card_list[0]
    assert card_0
    assert card_0.name
    assert card_0.suit


def test_should_get_all_cards_from_pack(pack):
    cards = pack.show_cards()
    assert len(cards) == pack.size


def test_card_should_have_valid_suit(cards):
    assert cards[Name.TWO].suit == Suit.HEARTS


def test_card_should_have_valid_name(cards):
    card = cards[Name.ACE]
    assert card.name == Name.ACE

def test_should_show_full_pack_of_cards(pack):

    # build dictionaries of Suit and names found.  value is the count of each
    found_Suit = {}
    found_names = {}

    for card in pack.show_cards():
        if card.suit not in found_Suit:
            found_Suit[card.suit] = 1
        else:
            found_Suit[card.suit] += 1

        if card.name not in found_names:
            found_names[card.name] = 1
        else:
            found_names[card.name] += 1

    # check the dictionaries contain the expected counted values
    assert len(found_Suit) == 4  # should have found 4 Suit
    for suit in Suit:
        assert suit in found_Suit

    for suit in found_Suit:
        assert found_Suit[suit] == 13  # should be 14 of each suit

    assert len(found_names) == 13  # should have found 13 different card names
    for name in Name:
        assert name in found_names

    for name in found_names:
        assert found_names[name] == 4  # should have found 4 of each card name

def test_should_deal_cards_from_pack(pack):
    assert pack.count_cards_left() == pack.size

    hand = pack.deal_cards(5)
    assert len(hand) == 5

    assert pack.count_cards_left() == (pack.size - 5)



def test_card_is_ace(cards):
    assert cards[Name.ACE].is_ace()

def test_card_is_not_ace(cards):
    assert not cards[Name.TEN].is_ace()
    assert not cards[Name.KING].is_ace()
    assert not cards[Name.SIX].is_ace()

def test_card_values(cards):
    assert cards[Name.ACE].value == 1
    assert cards[Name.TWO].value == 2
    assert cards[Name.THREE].value == 3
    assert cards[Name.FOUR].value == 4
    assert cards[Name.FIVE].value == 5
    assert cards[Name.SIX].value == 6
    assert cards[Name.SEVEN].value == 7
    assert cards[Name.EIGHT].value == 8
    assert cards[Name.NINE].value == 9
    assert cards[Name.TEN].value == 10
    assert cards[Name.JACK].value == 10
    assert cards[Name.QUEEN].value == 10
    assert cards[Name.KING].value == 10



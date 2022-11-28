import pytest

from blackjack.card_dealer import CardDealer


def test_card_dealer_has_pack_of_cards():

    dealer = CardDealer(packs=1)
    assert dealer.packs == 1
    assert dealer.number_of_cards_left() == 52



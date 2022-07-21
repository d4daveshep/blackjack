# test_pack_of_cards.py
import sys
import pytest
sys.path.append("../")

from blackjack.pack import Pack, Card

def test_should_create_pack_with_default_size():

    pack = Pack()
    assert pack.size == 52




def test_should_get_card_from_pack():
    pack = Pack()

    card = pack.get_card()
    assert card is not None
    assert isinstance(card, Card)




import sys
import pytest

sys.path.append("../")
from blackjack.game import Hand, Strategy, Move
from blackjack.pack import Pack


@pytest.fixture()
def shuffled_pack() -> Pack:
    pack = Pack()
    pack.shuffle()
    return pack



def test_hand_should_draw_two_cards_and_decide_next_move(shuffled_pack):
    hand = Hand(shuffled_pack.deal_cards(2))

    assert len(hand) == 2
    move = Strategy.decide_move(hand)
    if hand.value < 17:
        assert move == Move.Hit
    elif hand.value <= 21:
        assert move == Move.Sit
    else:
        assert move == Move.Bust




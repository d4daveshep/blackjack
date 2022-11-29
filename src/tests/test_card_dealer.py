from blackjack.card import Name, Suit
from blackjack.card_dealer import CardDealer


def test_card_dealer_has_pack_of_cards():
    dealer = CardDealer(packs=1)
    assert dealer.packs == 1
    assert dealer.number_of_cards_left() == 52


def test_card_dealer_can_deal_cards():
    dealer = CardDealer(packs=1)
    hand = dealer.deal_cards(5)
    assert len(hand) == 5
    assert hand[0].name == Name.ACE
    assert hand[0].suit == Suit.HEARTS
    assert hand[1].name == Name.TWO
    assert hand[1].suit == Suit.HEARTS
    assert hand[2].name == Name.THREE
    assert hand[2].suit == Suit.HEARTS
    assert hand[3].name == Name.FOUR
    assert hand[3].suit == Suit.HEARTS
    assert hand[4].name == Name.FIVE
    assert hand[4].suit == Suit.HEARTS

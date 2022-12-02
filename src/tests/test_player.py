from blackjack.player import Player


def test_create_player():
    player = Player(name="David", inital_balance=100.00)
    assert player
    assert player.name == "David"
    assert player.balance == 100.00

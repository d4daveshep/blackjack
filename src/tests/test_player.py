from blackjack.player import Player


def test_create_player():
    player = Player(name="Test", inital_balance=100.00)
    assert player
    assert player.name == "Test"
    assert player.balance == 100.00


def test_player_has_hand():
    player = Player(name="Test", inital_balance=100.00)
    assert player.hand

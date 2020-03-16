import pytest
from blackjack.cards import Card, Deck
from blackjack.characters import Character


@pytest.fixture
def player():
    return Character()


def test_check_card_count(player):
    cards = [Card("Hearts", x) for x in ["2", "3", "4"]]
    player.hand = cards
    assert player.card_count == 9


def test_check_card_count_ace_under_21(player):
    cards = [Card("Hearts", x) for x in ["A", "3", "4"]]
    player.hand = cards
    assert player.card_count == 18


def test_check_card_count_ace_over_21(player):
    cards = [Card("Hearts", x) for x in ["A", "10", "4"]]
    player.hand = cards
    assert player.card_count == 15


def test_hand_string(player):
    cards = [Card("Hearts", x) for x in ["A", "10", "4"]]
    player.hand = cards
    expected = "A.Hearts 10.Hearts 4.Hearts"
    assert expected == player.str_hand()

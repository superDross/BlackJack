from cards import Card, Deck
from characters import Character


class TestCharacter:
    def setup(self):
        self.player = Character()

    def test_check_card_count(self):
        cards = [Card("Hearts", x) for x in ["2", "3", "4"]]
        self.player.hand = cards
        assert self.player.card_count == 9

    def test_check_card_count_ace_under_21(self):
        cards = [Card("Hearts", x) for x in ["A", "3", "4"]]
        self.player.hand = cards
        assert self.player.card_count == 18

    def test_check_card_count_ace_over_21(self):
        cards = [Card("Hearts", x) for x in ["A", "10", "4"]]
        self.player.hand = cards
        assert self.player.card_count == 15

    def test_hand_string(self):
        cards = [Card("Hearts", x) for x in ["A", "10", "4"]]
        self.player.hand = cards
        expected = 'A.Hearts 10.Hearts 4.Hearts'
        assert expected == self.player.str_hand()

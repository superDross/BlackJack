from cards import Deck


class TestDeck:
    def setup(self):
        self.deck = Deck()

    def test_generate_cards(self):
        assert len(self.deck) == 52

    def test_take_card(self):
        card = self.deck.take_card()
        assert card not in self.deck

    def test_deck_regeneration_when_less_than_5_cards_in_deck(self):
        num_take = len(self.deck) - 5
        for _ in range(num_take):
            self.deck.pop()
        self.deck.take_card()
        assert len(self.deck) == 51

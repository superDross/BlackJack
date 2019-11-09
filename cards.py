import itertools
import random
from dataclasses import dataclass


@dataclass
class Card:
    suit: str
    number: str


class Deck(list):
    """
    Generates and contains all 52 Cards.
    """

    def __init__(self) -> None:
        super().__init__()
        self._generate_cards()

    def _generate_cards(self) -> None:
        """
        Generates all 52 cards
        """
        suits = ["Hearts", "Spades", "Clovers", "Diamonds"]
        numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        all_card_combos = list(itertools.product(numbers, suits))
        for number, suit in all_card_combos:
            card = Card(suit, number)
            self.append(card)
        random.shuffle(self)

    def take_card(self) -> Card:
        """
        Returns a card and removes it from the deck
        """
        self._check_card_count()
        card = random.choice(self)
        self.remove(card)
        return card

    def _check_card_count(self) -> None:
        """
        Regenerate deck if there are not enough cards for a game
        """
        if len(self) > 5:
            return
        else:
            self.clear()
            self._generate_cards()

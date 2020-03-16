from typing import List, Tuple, Union

from cards import Card, Deck


class Character:
    """
    Base class for the dealer and player
    """

    def __init__(self, money: Union[int, float] = 1000) -> None:
        self.hand: List[Card] = []
        self.money = money

    @property
    def card_count(self) -> int:
        """
        Counts total value of all card numbers and returns the
        best possible value from character hand
        """
        counter1 = 0
        # counter 2 for alternative ace
        counter2 = 0
        for card in self.hand:
            num = self._card2int(card)
            counter1 += num[0]
            counter2 += num[1]
        # filter only for values under 21
        under_21 = [x for x in (counter1, counter2) if x <= 21]
        if under_21:
            return max(under_21)
        # if all avlues are over 21 then return the largest
        else:
            return max(x for x in (counter1, counter2))

    def _card2int(self, card: Card) -> Tuple[int, int]:
        """ Counts the value of the given card number.

        Returns:
            A tuple of integers where the first
            element is the card int if the ace = 1
            and the second element is the card int
            if the ace = 11
        """

        if card.number in ["K", "Q", "J"]:
            return (10, 10)
        elif card.number == "A":
            return (1, 11)
        else:
            return (int(card.number), int(card.number))

    def str_hand(self) -> str:
        """
        Returns a string representation of all cards in hand
        """
        hand = ["{}.{}".format(card.number, card.suit) for card in self.hand]
        return " ".join(hand)


class Dealer(Character):
    """
    Card dealer
    """

    def __init__(self) -> None:
        self.deck: Deck = Deck()
        Character.__init__(self, 1000000)

    def deal(self, player: Character) -> None:
        """
        Take a card from the deck and place it to the given players hand attribute
        """
        player.hand.append(self.deck.take_card())

    def str_hand(self, show_hidden: bool = False) -> str:
        """
        Returns a string representation of all cards in hand except the face-down card
        """
        index = 0 if show_hidden else 1
        hand = ["{}.{}".format(card.number, card.suit) for card in self.hand[index:]]
        return " ".join(hand)

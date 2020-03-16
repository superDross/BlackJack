#!/usr/bin/python3

import sys

from characters import Character, Dealer
from menus import ActionMenu
from utils import clear, flush_input, sleep


class BlackJack:
    """
    BlackJack game
    """

    def __init__(self) -> None:
        self.player = Character()
        self.dealer = Dealer()
        self.menu = ActionMenu(self.dealer)
        self.minimum = 10
        self.maximum = int(self.minimum * 1.5)
        self.bet = 0

    def __call__(self) -> None:
        self.execute()

    def execute(self) -> None:
        """
        Starts the game
        """
        while self.player.money > self.minimum:
            try:
                self._make_bet()
                self._first_deal()
                self._construct_screen()
                if self._natural_21():
                    continue
                choice = self.menu.handle_options()
                self._perform_move(choice)
                self._show_cards(show_hidden=True)
                self._determine_winner()
                self._update_min_max()
                self._clear_hands()
            except KeyboardInterrupt:
                clear()
                print("\nThanks for playing!\n")
                sleep()
                clear()
                sys.exit(0)
        self._game_over()

    def _game_over(self) -> None:
        """
        Game over messages
        """
        msg = "You do not have enough money for the minimum bet of ${}"
        print(msg.format(self.minimum))
        print("\nGAME OVER")

    def _clear_hands(self) -> None:
        """
        Reset the player and dealers hands
        """
        self.dealer.hand = []
        self.player.hand = []

    def _perform_move(self, choice: str) -> None:
        """
        Translate the string choice into an action
        """
        if choice == "Stand":
            self.dealer.deal(self.dealer)
        elif choice == "Hit":
            self.dealer.deal(self.player)

    def _update_min_max(self) -> None:
        """
        Updates in and max attributes by 50%, to a max threshold of 500
        """
        if self.maximum < 500:
            self.minimum *= 2
            self.maximum *= 2
        else:
            self.minimum = 350
            self.maximum = 500

    def _first_deal(self) -> None:
        """
        Deals 2 cards to the dealer and player
        """
        print("\nDealer dealing cards....")
        sleep()
        self.dealer.deal(self.dealer)
        self.dealer.deal(self.dealer)
        self.dealer.deal(self.player)
        self.dealer.deal(self.player)

    def _natural_21(self) -> bool:
        """
        Determines if player has 21 and hands over winnings if True
        """
        if self.player.card_count == 21:
            winnings = self.bet + (self.bet * 2.5)
            msg = "Natural 21! You earn ${}"
            print(msg.format(winnings))
            sleep()
            self.player.money += winnings
            self._update_min_max()
            self._clear_hands()
            return True
        return False

    def _make_bet(self) -> None:
        """
        Prompts player to make a bet
        """
        clear()
        print("Player: ${}\n".format(self.player.money))
        msg = "Make your bet (min: ${}, max: ${})."
        print(msg.format(self.minimum, self.maximum))
        entered_bet = input(">> ")
        if not entered_bet.isdigit():
            print("Please enter a number.")
            sleep()
            flush_input()
            return self._make_bet()
        bet = int(entered_bet)
        if self.minimum > bet or self.maximum < bet:
            print("${} is outside the min and max bets".format(bet))
            sleep()
            self._make_bet()
        self.bet = bet
        self.player.money -= bet
        flush_input()

    def _construct_screen(self) -> None:
        """
        Constructs players stats and dealers and players hands
        """
        clear()
        print("Player Wallet: ${}".format(self.player.money))
        print("Bet: ${}\n".format(self.bet))
        self._show_cards()
        flush_input()

    def _show_cards(self, show_hidden: bool = False) -> None:
        """ Prints the players and dealers cards in hand.

        Args:
            show_hidden (bool): show dealers face down card if True.
        """
        print("Player: {}".format(self.player.str_hand()))
        print("Dealer: {}\n".format(self.dealer.str_hand(show_hidden)))

    def _determine_winner(self) -> None:
        """
        Determines whether player or dealer has cards closer to 21
        """
        player_hand = self.player.card_count
        dealer_hand = self.dealer.card_count
        if player_hand == dealer_hand:
            self._draws()
        elif player_hand == 21 or dealer_hand > 21:
            self._win()
        elif dealer_hand == 21 or player_hand > 21:
            self._lose()
        elif player_hand > dealer_hand:
            self._win()
        elif dealer_hand > player_hand:
            self._lose()
        else:
            raise ValueError("Unknown winner.")

    def _draws(self) -> None:
        """
        Give back the bet to the player
        """
        print("\nDraw!")
        sleep()
        self.player.money += self.bet
        self.bet = 0

    def _win(self) -> None:
        """
        Give player double his bettings in money
        """
        winnings = self.bet * 2
        print("\nPlayer Wins!")
        sleep()
        print("Player recieves ${}\n".format(self.bet))
        sleep()
        self.player.money += winnings
        self.bet = 0

    def _lose(self) -> None:
        """
        Dealer takes betting money
        """
        print("\nPlayer Loses!\n")
        sleep()
        self.dealer.money += self.bet
        self.bet = 0


# BlackJack/__main__.py
if __name__ == "__main__":
    game = BlackJack()
    game.execute()

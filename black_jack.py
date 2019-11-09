#!/usr/bin/python3

from utils import clear, flush_input, sleep
from characters import Character, Dealer


# BlackJack/menus/menus.py
class Menu(object):
    """ Base class for all menus.

    Attributes:
        options (dict): {option (str): method (func)}
        choices (str): string representation of _options.
    """

    def __init__(self, options, choices):
        self.options = options
        self.choices = choices

    def handle_options(self):
        """ Extract and execute a method from self.options."""
        try:
            print(self.choices)
            choice = input(">> ")
            item = self.options[choice]
            return item
        except KeyError:
            msg = "{} is not a valid choice. Try again.\n"
            print(msg.format(choice))
            sleep()
            return self.handle_options()


# BlackJack/menus/menus.py
class ActionMenu(Menu):
    """ Menu giving player action choice after cards dealt.

    Attributes:
        dealer (Dealer): the dealer.
        options (dict): {option (str): method (func)}
        choices (str): string representation of _options.
    """

    def __init__(self, dealer):
        self.dealer = dealer
        options = {"1": "Stand", "2": "Hit"}
        choices = "1. Stand\n2. Hit"
        Menu.__init__(self, options, choices)


# BlackJack/game/black_jack.py
class BlackJack(object):
    """ BlackJack game.

    Attributes:
        player (Character): players avatar.
        dealer (Dealer): card dealer.
        menu (ActionMenu): menu giving player choce of moves.
        minimum (int): minimum bet.
        maximum (int): maximum bet.
        bet (int): bet player has made.

    Usage:
        game = BlackJack()
        game.execute()
    """

    def __init__(self):
        self.player = Character()
        self.dealer = Dealer()
        self.menu = ActionMenu(self.dealer)
        self.minimum = 10
        self.maximum = int(self.minimum * 1.5)
        self.bet = 0

    def __call__(self):
        self.execute()

    def execute(self):
        """ Starts the game."""
        while self.player.money > self.minimum:
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
        self._game_over()

    def _game_over(self):
        """ Game over messages."""
        msg = "You do not have enough money for the minimum bet of ${}"
        print(msg.format(self.minimum))
        print("\nGAME OVER")

    def _clear_hands(self):
        """ Reset the player and dealers hands."""
        self.dealer.hand = []
        self.player.hand = []

    def _perform_move(self, choice):
        """ Translate the string choice into an action."""
        if choice == "Stand":
            self.dealer.deal(self.dealer)
        elif choice == "Hit":
            self.dealer.deal(self.player)

    def _update_min_max(self):
        """ Updates in and max attributes by 50%, to a max threshold of 500."""
        if self.maximum < 500:
            self.minimum *= 2
            self.maximum *= 2
        else:
            self.minimum = 350
            self.maximum = 500

    def _first_deal(self):
        """ Deals 2 cards to the dealer and player."""
        print("\nDealer dealing cards....")
        sleep()
        self.dealer.deal(self.dealer)
        self.dealer.deal(self.dealer)
        self.dealer.deal(self.player)
        self.dealer.deal(self.player)

    def _natural_21(self):
        """ Determines if player has 21 and hands over winnings if True."""
        if self.player.card_count == 21:
            winnings = self.bet + (self.bet * 2.5)
            msg = "Natural 21! You earn ${}"
            print(msg.format(winnings))
            sleep()
            self.player.money += winnings
            self._update_min_max()
            self._clear_hands()
            return True

    def _make_bet(self):
        """ Prompts player to make a bet."""
        clear()
        print("Player: ${}\n".format(self.player.money))
        msg = "Make your bet (min: ${}, max: ${})."
        print(msg.format(self.minimum, self.maximum))
        bet = input(">> ")
        if not bet.isdigit():
            print("Please enter a number.")
            sleep()
            flush_input()
            return self._make_bet()
        bet = int(bet)
        if self.minimum > bet or self.maximum < bet:
            print("${} is outside the min and max bets".format(bet))
            sleep()
            self._make_bet()
        self.bet = bet
        self.player.money -= bet
        flush_input()

    def _construct_screen(self):
        """ Constructs players stats and dealers and players hands."""
        clear()
        print("Player Wallet: ${}".format(self.player.money))
        print("Bet: ${}\n".format(self.bet))
        self._show_cards()
        flush_input()

    def _show_cards(self, show_hidden=False):
        """ Prints the players and dealers cards in hand.

        Args:
            show_hidden (bool): show dealers face down card if True.
        """
        print("Player: {}".format(self.player.str_hand()))
        print("Dealer: {}\n".format(self.dealer.str_hand(show_hidden)))

    def _determine_winner(self):
        """ Determines whether player or dealer has cards closer to 21."""
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

    def _draws(self):
        """ Give back the bet to the player."""
        print("\nDraw!")
        sleep()
        self.player.money += self.bet
        self.bet = 0

    def _win(self):
        """ Give player double his bettings in money."""
        winnings = self.bet * 2
        print("\nPlayer Wins!")
        sleep()
        print("Player recieves ${}\n".format(self.bet))
        sleep()
        self.player.money += winnings
        self.bet = 0

    def _lose(self):
        """ Dealer takes betting money."""
        print("\nPlayer Loses!\n")
        sleep()
        self.dealer.money += self.bet
        self.bet = 0


# BlackJack/__main__.py
if __name__ == "__main__":
    game = BlackJack()
    game.execute()

from typing import Any, Dict

from characters import Dealer
from utils import sleep


class Menu(object):
    """
    Base class for all menus
    """

    def __init__(self, options: Dict[str, Any], choices: str) -> None:
        self.options = options
        self.choices = choices

    def handle_options(self) -> str:
        """
        Extract and execute a method from self.options
        """
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


class ActionMenu(Menu):
    """
    Menu giving player action choice after cards dealt
    """

    def __init__(self, dealer: Dealer) -> None:
        self.dealer = dealer
        options = {"1": "Stand", "2": "Hit"}
        choices = "1. Stand\n2. Hit"
        Menu.__init__(self, options, choices)

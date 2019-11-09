import os
import sys
import time


def sleep():
    time.sleep(2)


def clear():
    """ Platform agnostic way to clear screen."""
    os.system("cls" if os.name == "nt" else "clear")


def flush_input():
    """ Platform agnostic way to clear key input."""
    if os.name == "nt":
        import msvcrt

        while msvcrt.kbhit():
            msvcrt.getch()
    else:
        from termios import tcflush, TCIFLUSH

        tcflush(sys.stdin, TCIFLUSH)

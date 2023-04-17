"""
File: DoubleBeepers.py
Name:richard
-------------------------------
TODO:
"""

from karel.stanfordkarel import *

def turn_around():
    turn_left()
    turn_left()


def double_beeper():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()
        move()
        turn_around()


def put_beeper_back():
    move()
    while on_beeper():
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        turn_around()
        move()
def karel_goes_home():
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def main():
    """
    Karel will double the beepers
    """
    move()
    double_beeper()
    put_beeper_back()
    karel_goes_home()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)

"""
File: Steeplechase.py
Name: Richard
---------------------------------
TODO:
"""

from karel.stanfordkarel import *
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    """
    pre condition:karel is on the left, facing east
    post condition:karel is on  the right
    """
    up()
    cross()
    down()


def up():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()



def cross():
    move()



def down():
    turn_right()
    while front_is_clear():
        move()
    turn_left()



def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    move()
    # while not front_is_clear():
    #     jump()
    #     while front_is_clear():
    #         move()
    for i in range(10):
        if front_is_clear():
            move()
        else:
            jump()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)

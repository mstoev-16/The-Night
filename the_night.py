import sys
import time
import os

TITLE_SCREEN_FLAG = False
DELAY = 2
TYPING_DELAY = 0.00001
ENDING = 'Congratulations! You won!'
EXIT_MESSAGE = 'See you next time!'
START_MESSAGE = 'Start game? (y/n): '
DEATH_MESSAGE = 'You died.'
PLAY_AGAIN = 'Play again? (y/n): '


# Utility and prompt functions

def read_text_files(text_file, delay):
    with open(text_file, 'r') as file:  # 'with' closes the file after being opened
        lines = file.readlines()        # Each line of text turns into a list element
        for line in lines:
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()      # Flushes out buffer and prints immediately
                time.sleep(delay)       # Text printing delay


def typewriting_strings(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


def refresh_screen():
    os.system('cls')      # Clear screen
    print()
    print(print_title())  # Keep title always on screen
    print()


def print_title():
    with open('text_files/title_screen.txt', 'r') as file:
        title_screen = file.read()
        return title_screen


def continue_story():
    while True:
        choice = input("Type 'c' to continue: ")
        if choice == 'c':
            break
    return


def exit_game():
    typewriting_strings(EXIT_MESSAGE, TYPING_DELAY)
    time.sleep(DELAY)
    os.system('cls')
    exit()


def main_menu():
    os.system('cls')
    print()

    global TITLE_SCREEN_FLAG  # flag to keep the title screen

    if TITLE_SCREEN_FLAG:
        print(print_title())
        print()
    else:
        read_text_files('text_files/title_screen.txt', TYPING_DELAY)
        TITLE_SCREEN_FLAG = True
        print("\n")

    typewriting_strings(START_MESSAGE, TYPING_DELAY)
    start = input()

    if start == 'y':
        refresh_screen()
        wake_up()
    elif start == 'n':
        refresh_screen()
        exit_game()


def play_again():
    typewriting_strings(PLAY_AGAIN, TYPING_DELAY)
    choice = input()

    if choice == 'y':
        refresh_screen()
        wake_up()
    elif choice == 'n':
        refresh_screen()
        exit_game()


def die():
    print('\n')
    continue_story()
    print()
    typewriting_strings(DEATH_MESSAGE, TYPING_DELAY)
    time.sleep(DELAY)
    print('\n')
    play_again()


def win_game():
    typewriting_strings(ENDING, TYPING_DELAY)
    time.sleep(2)
    print('\n')
    play_again()


####################################
# Game starts
def wake_up():
    read_text_files('text_files/wake_up.txt', TYPING_DELAY)
    choice = input()

    if choice == '1':
        refresh_screen()
        hide_in_room()
    elif choice == '2':
        refresh_screen()
        approach_bathroom()


####################################
# Play-through 1 - Hide in room

def hide_in_room():
    read_text_files('text_files/hide_in_room.txt', TYPING_DELAY)
    choice = input()

    if choice == '1':
        refresh_screen()
        hide_under_bed()
    elif choice == '2':
        refresh_screen()
        hide_in_closet()


def hide_in_closet():
    read_text_files('text_files/hide_in_closet.txt', TYPING_DELAY)
    choice = input()

    if choice == '1':
        refresh_screen()
        escape_during_bed()
    elif choice == '2':
        refresh_screen()
        wait_during_bed()


def wait_during_bed():
    read_text_files('text_files/wait_during_bed.txt', TYPING_DELAY)
    choice = input()

    if choice == '1':
        refresh_screen()
        escape_during_curtains()
    elif choice == '2':
        refresh_screen()
        wait_during_curtains()


def wait_during_curtains():
    read_text_files('text_files/wait_during_curtains.txt', TYPING_DELAY)
    choice = input()

    if choice == '1':
        refresh_screen()
        escape_after_curtains()
    elif choice == '2':
        refresh_screen()
        wait_after_curtains()


def escape_during_curtains():
    read_text_files('text_files/escape_during_curtains1.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    read_text_files('text_files/escape_during_curtains2.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    read_text_files('text_files/leave_house4.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    read_text_files('text_files/finish_game3.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    win_game()


def wait_after_curtains():
    read_text_files('text_files/wait_after_curtains1.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    read_text_files('text_files/wait_after_curtains2.txt', TYPING_DELAY)
    choice = input()

    if choice == '1':
        refresh_screen()
        hide_in_storage()
    elif choice == '2':
        refresh_screen()
        sneak_downstairs()


def hide_in_storage():
    read_text_files('text_files/hide_in_storage.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    read_text_files('text_files/leave_house4.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    read_text_files('text_files/finish_game2.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    win_game()


####################################
# Choices that lead to death

def hide_under_bed():
    read_text_files('text_files/hide_under_bed.txt', TYPING_DELAY)
    die()


def escape_after_curtains():
    read_text_files('text_files/escape_after_curtains.txt', TYPING_DELAY)
    die()


def escape_during_bed():
    read_text_files('text_files/escape_during_bed.txt', TYPING_DELAY)
    die()


def sneak_downstairs():
    read_text_files('text_files/sneak_downstairs.txt', TYPING_DELAY)
    die()


####################################
# Play-through 2 - Approach bathroom

def approach_bathroom():
    read_text_files('text_files/approach_bathroom.txt', TYPING_DELAY)
    choice = input()

    if choice == '1':
        refresh_screen()
        peek_through_door()
    elif choice == '2':
        refresh_screen()
        go2_kitchen()
    elif choice == '3':
        refresh_screen()
        try2_leave_house()


def go2_kitchen():
    read_text_files('text_files/go2_kitchen1.txt', TYPING_DELAY)
    print('\n')

    continue_story()
    refresh_screen()
    read_text_files('text_files/go2_kitchen2.txt', TYPING_DELAY)
    choice = input()

    if choice == '1':
        refresh_screen()
        leave_house1()
    elif choice == '2':
        refresh_screen()
        check_whats_happening()


def try2_leave_house():
    read_text_files('text_files/try2_leave_house.txt', TYPING_DELAY)
    choice = input()

    if choice == '1':
        refresh_screen()
        check_basket()
    elif choice == '2':
        refresh_screen()
        check_liquor()
    elif choice == '3':
        refresh_screen()
        check_kitchen()


def check_kitchen():
    read_text_files('text_files/check_kitchen.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    read_text_files('text_files/leave_house3.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    read_text_files('text_files/finish_game2.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    win_game()


def check_basket():
    read_text_files('text_files/check_basket.txt', TYPING_DELAY)
    choice = input()

    if choice == '1':
        refresh_screen()
        keep_looking4key()
    elif choice == '2':
        refresh_screen()
        hide()


def check_liquor():
    read_text_files('text_files/check_liquor.txt', TYPING_DELAY)
    choice = input()

    if choice == '1':
        refresh_screen()
        keep_looking4key()
    elif choice == '2':
        refresh_screen()
        hide()


def hide():
    read_text_files('text_files/hide.txt', TYPING_DELAY)
    choice = input()

    if choice == '1':
        refresh_screen()
        hide_under_sink()
    elif choice == '2':
        refresh_screen()
        hide_behind_sofa()
    elif choice == '3':
        refresh_screen()
        hide_behind_rack()


def hide_under_sink():
    read_text_files('text_files/hide_under_sink.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    read_text_files('text_files/leave_house2.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    read_text_files('text_files/finish_game3.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    win_game()


def hide_behind_rack():
    read_text_files('text_files/hide_behind_rack.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    read_text_files('text_files/leave_house2.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    read_text_files('text_files/finish_game3.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    win_game()


def leave_house1():
    read_text_files('text_files/leave_house1.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    read_text_files('text_files/looking_around.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    read_text_files('text_files/finish_game1.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    win_game()


def look_around():
    read_text_files('text_files/looking_around1.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    read_text_files('text_files/finish_game3.txt', TYPING_DELAY)
    print('\n')
    continue_story()
    refresh_screen()

    win_game()


####################################
# Choices that lead to death
def peek_through_door():
    read_text_files('text_files/peek_through_door.txt', TYPING_DELAY)
    die()


def check_whats_happening():
    read_text_files('text_files/check_whats_happening.txt', TYPING_DELAY)
    die()


def keep_looking4key():
    read_text_files('text_files/keep_looking4key.txt', TYPING_DELAY)
    die()


def hide_behind_sofa():
    read_text_files('text_files/hide_behind_sofa.txt', TYPING_DELAY)
    die()


# Code initiation
main_menu()

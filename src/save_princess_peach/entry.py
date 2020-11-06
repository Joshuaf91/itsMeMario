# -*- coding: utf-8 -*-
"""save_princess_peach

Project entry file.
"""
import sys
from save_princess_peach.constants import DEFAULT_GRID, BOWSER, PEACH
from save_princess_peach.models.bowsers_castle_map import BowsersCastle


def get_file_as_bowsers_castle(file_path: str = None) -> BowsersCastle:
    """Read file

    Get file from path in the command line argument
    or use default if none provided.

    :return
        BowsersCastle
    """
    path_to_file = file_path or DEFAULT_GRID
    if len(sys.argv) == 2:
        path_to_file = sys.argv[1]

    try:
        map_of_castle = BowsersCastle()

        with open(path_to_file, 'r', encoding='utf-8') as file:
            for line in file:
                # break for last line in file
                if not line:
                    break

                current_line = line.rstrip("\n")
                if not map_of_castle.size:
                    map_of_castle.set_size(int(current_line))
                else:
                    map_of_castle.add_map_layer(current_line)

    except FileNotFoundError as error:
        print(f'File: {path_to_file} was not found please update the commandline argument or update'
              f'the DEFAULT_GRID_DIRECTORY constant in constants.py {error}')
        sys.exit('My error message')

    return map_of_castle


def enter_castle(file_path: str = None):
    """Traverse the Castle kill Bowser then save the Princess."""
    bowsers_castle = get_file_as_bowsers_castle(file_path)

    count = 0
    move_to_person = BOWSER
    last_move = None
    last_blocked_move = None
    while count < 1000:
        count += 1
        current_move = bowsers_castle.move_mario_to_person(move_to_person)
        if current_move is None:
            last_blocked_move = last_blocked_move
        else:
            last_move = current_move

        if not bowsers_castle.get_location_of_person(PEACH):
            exit(0)
        elif not bowsers_castle.get_location_of_person(BOWSER):
            move_to_person = PEACH

        print(current_move)

    exit(1)

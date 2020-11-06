# -*- coding: utf-8 -*-
"""save_princess_peach

Project entry file.
"""
import sys
from dataclasses import asdict

from save_princess_peach.constants import DEFAULT_GRID
from save_princess_peach.models.bowsers_castle_map import BowsersCastle


def get_files_as_grid() -> BowsersCastle:
    """Read file

    Get file from path from command line argument
    or use default if none provided.

    :return
        BowsersCastle
    """
    path_to_file = DEFAULT_GRID
    if len(sys.argv) == 2:
        path_to_file = sys.argv[1]

    try:
        map_of_castle = BowsersCastle()

        with open(path_to_file, 'r', encoding='utf-8') as file:
            for line in file:
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

from pprint import pprint

pprint(asdict(get_files_as_grid()))

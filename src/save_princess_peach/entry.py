# -*- coding: utf-8 -*-
"""save_princess_peach

Project entry file.
"""
import sys
from save_princess_peach.constants import DEFAULT_GRID_DIRECTORY


def get_files():
    path_to_file = DEFAULT_GRID_DIRECTORY
    if len(sys.argv) == 2:
        path_to_file = sys.argv[1]

    try:
        file_stream = open(path_to_file)

        for line in file_stream:
            print(line)

    except FileNotFoundError as error:
        print(f'File: {path_to_file} was not found please update the commandline argument or update'
              f'the DEFAULT_GRID_DIRECTORY constant in constants.py {error}')
        sys.exit('My error message')
    finally:
        print('BYE')
        file_stream.close()


get_files()

# -*- coding: utf-8 -*-
"""save_princess_peach.constants.py

Constants for save-princes-peach.
"""

# Default file used as grid
DEFAULT_GRID = '/Users/JFermin/Documents/GitHub/itsMeMario/tests/test_grids/init_grid.txt'

# players
BOWSER = 'b'
PEACH = 'p'
MARIO = 'm'
PLAYERS = [BOWSER, PEACH, MARIO]

# additional tiles
HAZARDS = '*'
SAFE = '-'
VISITED = "v"
ALL_POSITIONS = [BOWSER, PEACH, MARIO, HAZARDS, SAFE, VISITED]
SAFE_POSITION = [SAFE, PEACH, BOWSER]


# Movements
UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

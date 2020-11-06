# -*- coding: utf-8 -*-
"""save_princess_peach.models.grid

Grid data representation.
"""
from dataclasses import dataclass, field

from save_princess_peach.constants import (
    BOWSER, PEACH, MARIO, PLAYERS, ALL_POSITIONS, UP, DOWN, LEFT, RIGHT, VISITED,
    SAFE_POSITION
)


@dataclass
class BowsersCastle:
    """Bowser`s castle"""
    map: list = field(default_factory=list)
    size: int = field(default=0)
    bowser_location: tuple = field(default=None)
    peach_location: tuple = field(default=None)
    mario_location: tuple = field(default=None)

    def location_of_person_on_layer(self, layer: list, layer_level: int) -> tuple:
        """Check layer for any person"""
        bowsers_location = None
        peach_location = None
        mario_location = None

        for idx, map_location_value in enumerate(layer):
            if map_location_value in PLAYERS:
                player_location = (layer_level, idx)
                self.set_person_location(map_location_value, player_location)

        return bowsers_location, peach_location, mario_location

    def set_size(self, size: int):
        """Set size of Boweser's castle map"""
        assert(isinstance(size, int))
        self.size = size

    def add_map_layer(self, layer: str):
        """Add layer to the bottom of the map."""
        assert(isinstance(layer, str))
        split_text = list(layer)

        assert(len(split_text) == self.size)
        self.map.append(split_text)
        current_map_size = len(self.map)

        assert(current_map_size <= self.size)
        self.location_of_person_on_layer(split_text, current_map_size - 1)

    def get_location_of_person(self, person) -> (int, int):
        """Get Persons Location"""
        assert (person in PLAYERS)
        location = None
        if person == BOWSER:
            location = self.bowser_location
        elif person == PEACH:
            location = self.peach_location
        elif person == MARIO:
            location = self.mario_location

        return location

    def set_person_location(self, person: str, location: tuple or None):
        """Set location for Monster"""
        assert(person in PLAYERS)
        if person == BOWSER:
            self.bowser_location = location
        elif person == PEACH:
            self.peach_location = location
        elif person == MARIO:
            self.mario_location = location

    def set_map_location(self, update: str, location: tuple):
        """Set location for Monster"""
        assert(update in ALL_POSITIONS)
        row, col = location
        self.map[row][col] = update
        if update in PLAYERS:
            self.set_person_location(update, location)

    def move_mario_to_person(self, person):
        """Move Mario towards the person"""
        row, col = self.get_location_of_person(person)
        m_row, m_col = self.get_location_of_person(MARIO)
        castle_map = self.map

        up_is_safe = False
        try:
            if m_row - 1 == -1:
                up_is_safe = False
            else:
                up_is_safe = castle_map[m_row - 1][m_col] in SAFE_POSITION
        except IndexError:
            pass

        down_is_safe = False
        try:
            down_is_safe = castle_map[m_row + 1][m_col] in SAFE_POSITION
        except IndexError:
            pass

        left_is_safe = False
        try:
            if m_col - 1 == -1:
                left_is_safe = False
            else:
                left_is_safe = castle_map[m_row][m_col - 1] in SAFE_POSITION
        except IndexError:
            pass

        right_is_safe = False
        try:
            right_is_safe = castle_map[m_row][m_col + 1] in SAFE_POSITION
        except IndexError:
            pass

        m_new_location = None
        # attempt to move vertical until we are on the persons row
        if row != m_row:
            # Should we move up?
            if m_row > row and up_is_safe:
                m_new_location = (m_row - 1, m_col)
                self.set_map_location(VISITED, (m_row, m_col))
                self.set_map_location(MARIO, m_new_location)

                if m_new_location == (row, col):
                    self.set_person_location(person, None)

                return UP

            # Should we move down?
            elif m_row < row and down_is_safe:
                m_new_location = (m_row + 1, m_col)
                self.set_map_location(VISITED, (m_row, m_col))
                self.set_map_location(MARIO, m_new_location)

                if m_new_location == (row, col):
                    self.set_person_location(person, None)

                return DOWN

        # else move horizontal
        # Should we move left?
        if left_is_safe:
            m_new_location = (m_row, m_col - 1)
            self.set_map_location(VISITED, (m_row, m_col))
            self.set_map_location(MARIO, m_new_location)

            if m_new_location == (row, col):
                self.set_person_location(person, None)

            return LEFT

        # Should we move right?
        elif right_is_safe:
            m_new_location = (m_row, m_col + 1)
            self.set_map_location(VISITED, (m_row, m_col))
            self.set_map_location(MARIO, m_new_location)

            if m_new_location == (row, col):
                self.set_person_location(person, None)

            return RIGHT

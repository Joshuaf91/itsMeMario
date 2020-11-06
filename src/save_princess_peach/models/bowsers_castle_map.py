# -*- coding: utf-8 -*-
"""save_princess_peach.models.grid

BowsersCastle data representation.
"""
from dataclasses import dataclass, field

from save_princess_peach.constants import BOWSER, PEACH, MARIO, PLAYERS


@dataclass
class BowsersCastle:
    """Bowser`s castle"""
    map: list = field(default_factory=list)
    size: int = field(default=0)
    bowser_location: tuple = field(default_factory=tuple)
    peach_location: tuple = field(default_factory=tuple)
    mario_location: tuple = field(default_factory=tuple)

    def location_of_person_on_layer(self, layer: list, layer_level: int) -> tuple:
        """Check layer for any person"""
        bowsers_location = None
        peach_location = None
        mario_location = None

        for idx, map_location in enumerate(layer):
            if map_location in PLAYERS:
                player_location = (layer_level, idx)
                self.set_location(map_location, player_location)

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

    def set_location(self, person: str, location: tuple):
        """Set location for Monster"""
        assert(person in PLAYERS)
        if person == BOWSER:
            self.bowser_location = location
        elif person == PEACH:
            self.peach_location = location
        elif person == MARIO:
            self.mario_location = location

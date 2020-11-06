import unittest
from save_princess_peach.entry import enter_castle


class TestSavePrincessPeach(unittest.TestCase):

    def test_init_grid_file(self):
        with self.assertRaises(SystemExit):
            enter_castle('/Users/JFermin/Documents/GitHub/itsMeMario/tests/test_grids/init_grid.txt')

    def test_init_grid_reversed(self):
        with self.assertRaises(SystemExit):
            enter_castle(
                '/Users/JFermin/Documents/GitHub/itsMeMario/tests/test_grids/init_grid_reversed.txt'
            )

    def test_init_grid_flipped(self):
        with self.assertRaises(SystemExit):
            enter_castle(
                '/Users/JFermin/Documents/GitHub/itsMeMario/tests/test_grids/init_grid_flipped.txt'
            )

    def test_init_grid_flipped_reversed(self):
        with self.assertRaises(SystemExit):
            enter_castle(
                '/Users/JFermin/Documents/GitHub/itsMeMario/tests/test_grids/test_test_init_grid_flipped_reversed.txt'
            )

    def test_update_me(self):
        with self.assertRaises(SystemExit):
            enter_castle(
                '/Users/JFermin/Documents/GitHub/itsMeMario/tests/test_grids/update_me.txt'
            )

import unittest
from save_princess_peach.entry import enter_castle


class TestSavePrincessPeach(unittest.TestCase):

    def test_init_grid_file(self):
        with self.assertRaises(SystemExit) as cm:
            enter_castle('/Users/JFermin/Documents/GitHub/itsMeMario/tests/test_grids/init_grid.txt')

        self.assertEqual(cm.exception.code, 0)

    def test_init_grid_reversed(self):
        with self.assertRaises(SystemExit) as cm:
            enter_castle(
                '/Users/JFermin/Documents/GitHub/itsMeMario/tests/test_grids/init_grid_reversed.txt'
            )

        self.assertEqual(cm.exception.code, 0)

    def test_init_grid_flipped(self):
        with self.assertRaises(SystemExit) as cm:
            enter_castle(
                '/Users/JFermin/Documents/GitHub/itsMeMario/tests/test_grids/init_grid_flipped.txt'
            )

        self.assertEqual(cm.exception.code, 0)

    def test_init_grid_flipped_reversed(self):
        with self.assertRaises(SystemExit) as cm:
            enter_castle(
                '/Users/JFermin/Documents/GitHub/itsMeMario/tests/test_grids/test_test_init_grid_flipped_reversed.txt'
            )

        self.assertEqual(cm.exception.code, 0)

    def test_update_me(self):
        with self.assertRaises(SystemExit) as cm:
            enter_castle(
                '/Users/JFermin/Documents/GitHub/itsMeMario/tests/test_grids/update_me.txt'
            )

        self.assertEqual(cm.exception.code, 0)

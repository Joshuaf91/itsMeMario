import unittest
from save_princess_peach.entry import enter_castle
import os
dirname = os.path.dirname(__file__)


class TestSavePrincessPeach(unittest.TestCase):

    def test_init_grid_file(self):
        with self.assertRaises(SystemExit) as cm:
            filename = os.path.join(dirname, '/test_grids/init_grid.txt')
            enter_castle(filename)

        self.assertEqual(cm.exception.code, 0)

    def test_init_grid_reversed(self):
        with self.assertRaises(SystemExit) as cm:
            filename = os.path.join(dirname, '/test_grids/init_grid_reversed.txt')
            enter_castle(filename)

        self.assertEqual(cm.exception.code, 0)

    def test_init_grid_flipped(self):
        with self.assertRaises(SystemExit) as cm:
            filename = os.path.join(dirname, '/test_grids/init_grid_flipped.txt')
            enter_castle(filename)

        self.assertEqual(cm.exception.code, 0)

    def test_init_grid_flipped_reversed(self):
        with self.assertRaises(SystemExit) as cm:
            filename = os.path.join(dirname, '/test_grids/test_test_init_grid_flipped_reversed.txt')
            enter_castle(filename)

        self.assertEqual(cm.exception.code, 0)

    def test_update_me_file(self):
        with self.assertRaises(SystemExit) as cm:
            filename = os.path.join(dirname, '/test_grids/update_me.txt')
            enter_castle(filename)

        self.assertEqual(cm.exception.code, 0)

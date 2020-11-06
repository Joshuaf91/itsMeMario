import unittest
from save_princess_peach.entry import enter_castle


class TestSavePrincessPeach(unittest.TestCase):

    def test_init_grid_file(self):
        with self.assertRaises(SystemExit):
            enter_castle('/Users/JFermin/Documents/GitHub/itsMeMario/tests/test_grids/init_grid.txt')

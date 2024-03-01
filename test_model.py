import unittest
from model import Superhero

class TestSuperhero(unittest.TestCase):
    def setUp(self):
        self.superhero = Superhero("Iron Man", 85, 1.85, "Marvel", 10)

    def test_get_name(self):
        self.assertEqual(self.superhero.get_name(), "Iron Man")

    def test_set_name(self):
        self.superhero.set_name("Captain America")
        self.assertEqual(self.superhero.get_name(), "Captain America")

    def test_get_weight(self):
        self.assertEqual(self.superhero.get_weight(), 85)

    def test_set_weight(self):
        self.superhero.set_weight(90)
        self.assertEqual(self.superhero.get_weight(), 90)

    def test_get_height(self):
        self.assertEqual(self.superhero.get_height(), 1.85)

    def test_set_height(self):
        self.superhero.set_height(1.9)
        self.assertEqual(self.superhero.get_height(), 1.9)

    def test_get_universe(self):
        self.assertEqual(self.superhero.get_universe(), "Marvel")

    def test_set_universe(self):
        self.superhero.set_universe("DC")
        self.assertEqual(self.superhero.get_universe(), "DC")

    def test_get_games_played(self):
        self.assertEqual(self.superhero.get_games_played(), 10)

    def test_set_games_played(self):
        self.superhero.set_games_played(15)
        self.assertEqual(self.superhero.get_games_played(), 15)

    def test_str(self):
        expected_output = "Iron Man (85 kg, 1.85 m) from Marvel played 10 games"
        self.assertEqual(str(self.superhero), expected_output)

if __name__ == '__main__':
    unittest.main()

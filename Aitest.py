import unittest
from unittest.mock import patch
from io import StringIO
from Aicontroller import SuperheroController

class TestSuperheroController(unittest.TestCase):
    def setUp(self):
        self.controller = SuperheroController()

    @patch("builtins.input", side_effect=["Iron Man", "180", "80", "100"])
    def test_create_superhero_valid_input(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            superhero = self.controller.create_superhero()

        expected_output = "Enter superhero name: Enter height (175 - 205): Enter weight (75 - 140): Enter number of games played: "
        self.assertEqual(mock_stdout.getvalue(), expected_output)

        self.assertEqual(superhero.name, "Iron Man")
        self.assertEqual(superhero.height, 180)
        self.assertEqual(superhero.weight, 80)
        self.assertEqual(superhero.games_played, 100)

    @patch("builtins.input", side_effect=["Iron Man", "170", "80", "1000"])
    def test_create_superhero_invalid_input(self, mock_input):
        with self.assertRaises(Exception) as context:
            self.controller.create_superhero()

        self.assertTrue("Error creating superhero:" in str(context.exception))

if __name__ == "__main__":
    unittest.main()
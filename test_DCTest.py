import unittest
from DC import DC

dc = DC()
class DCText(unittest.TestCase):
    def test_setName(self):
        dc.setName("Lin")
        self.assertEqual("Lin", dc.getName())
    def test_setHeight(self):
        dc.setHeight(150)
        self.assertEqual(150,dc.getHeight())
    def test_setWeight(self):
        dc.setWeight(78)
        self.assertEqual(78,dc.getWeight())
    def test_setGames_played(self):
        dc.setGamesPlayed(50)
        self.assertEqual(50,dc.getGamesPlayed())

if __name__ == "__main__":
    unittest.main()
import unittest
from Marvel import Marvel

marvel = Marvel()
class MarvelTest(unittest.TestCase):
    def test_setName(self):

        marvel.setName("Lin")
        self.assertEqual("Lin", marvel.getName())
    def test_setHeight(self):
        marvel.setHeight(150)
        self.assertEqual(150,marvel.getHeight())
    def test_setWeight(self):
        marvel.setWeight(78)
        self.assertEqual(78,marvel.getWeight())
    def test_setGames_played(self):
        marvel.setGamesPlayed(50)
        self.assertEqual(50,marvel.getGamesPlayed())

if __name__ == "__main__":
    unittest.main()
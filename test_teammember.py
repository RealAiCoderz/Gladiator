import unittest
from model import TeamMember


class TestTeamMember(unittest.TestCase):
    def test_valid_height(self):
        member = TeamMember("Test", 180, 80, 50)
        self.assertEqual(member.height, 180)

    def test_valid_weight(self):
        member = TeamMember("Test", 180, 80, 50)
        self.assertEqual(member.weight, 80)
    
    def test_valid_games_played(self):
        member = TeamMember("Test", 180, 80, 50)
        self.assertEqual(member.games_played, 50)

if __name__ == '__main__':
    unittest.main()
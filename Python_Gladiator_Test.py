#Test Module
import unittest
from unittest.mock import MagicMock
from Python_Gladiator_Model import Team, TeamMember
from Python_Gladiator_Controller import Controller
from Python_Gladiator_View import View

#Checks if the add_member method of the Team class adds a member correctly.
class TestTeam(unittest.TestCase):
    def test_add_member(self):
        team = Team("Marvel")
        member = TeamMember("Thor", 182, 90, 105)
        team.add_member(member)
        self.assertEqual(len(team.members), 1)

class TestController(unittest.TestCase):
    #It verifies the functionality of the add_member_to_team method in the Controller class
    def test_add_member_to_team(self):
        controller = Controller()
        team = Team("Marvel")
        controller.add_member_to_team(team)
        self.assertGreater(len(team.members), 0)
    #It ensures that the run method of the Controller class works as expected
    def test_run(self):
        controller = Controller()

        marvel_team = Team("Marvel")
        dc_team = Team("DC")

        view_mock = MagicMock()
        controller.view = view_mock

        controller.run()

        view_mock.display_team_data.assert_called_with(marvel_team)
        view_mock.display_team_data.assert_called_with(dc_team)

class TestView(unittest.TestCase):
    #It checks if the get_member_data method of the View class retrieves member data correctly.
    def test_get_member_data(self):
        view = View()
        view.input = lambda _: "Thor\n182\n90\n105\n"  # Provide correct input for testing
        member_data = view.get_member_data("TestTeam")
        self.assertEqual(member_data.name, "Thor")  # expected name to "Thor"
        self.assertEqual(member_data.height, 182)    # expected height to 182

    #It ensures that the get_valid_input method of the View class correctly validates user input
    def test_get_valid_input(self):
        view = View()
        view.input = lambda _: "182\n90\n"  # Provide correct height and weight input for testing
        height = view.get_valid_input("Height (cm): ", view.validate_height)
        weight = view.get_valid_input("Weight (kg): ", view.validate_weight)
        self.assertEqual(height, 182)  #expected height to 182

if __name__ == '__main__':
    unittest.main()

import unittest
import model

class Test_Model(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obj = model.Star()
    
    @classmethod
    def tearDownClass(cls):
        del cls.obj
        
    def test_name(self):
        self.obj.set_name("testName") 
        self.assertEqual("testName", self.obj.get_name())
        self.assertNotEqual("testname", self.obj.get_name())
    
    def test_height(self):
        self.obj.set_height(150)
        self.assertEqual(150, self.obj.get_height())
        self.assertNotEqual(151, self.obj.get_height())
        
        self.obj.set_height(150.5)
        self.assertEqual(150.5, self.obj.get_height())
        self.assertNotEqual(151.5, self.obj.get_height())
    
    def test_weight(self):
        self.obj.set_weight(180)
        self.assertEqual(180, self.obj.get_weight())
        self.assertNotEqual(181, self.obj.get_weight())
        
        self.obj.set_weight(180.5)
        self.assertEqual(180.5, self.obj.get_weight())
        self.assertNotEqual(181.5, self.obj.get_weight())
        
if __name__ == "__main__":
    unittest.main()
import unittest
class SomeTestClass(unittest.TestCase):
    def setUp(self):
        print("setUp")
    def tearDown(self):
        print("tearDown")

    def test_1(self):
        self.assertTrue(4==4)
    @unittest.expectedFailure
    def test_2(self):
        self.assertFalse(4==4)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(SomeTestClass)
    runner = unittest.TextTestRunner()
    runner.run(suite())
import unittest
#import example
from example import my_function
#import example

class MyTest(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(my_function(1,1),2)
        self.assertEqual(my_function(1,-1),0)
        self.assertEqual(my_function(-1,-1),-2)
        self.assertEqual(my_function(1,1),2)
        self.assertEqual(my_function(1.1,1),2.1)

if __name__ == '__main__':
    unittest.main()

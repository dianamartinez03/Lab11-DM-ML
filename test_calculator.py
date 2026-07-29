import unittest
from calculator import add,subtract,div,mul,square_root,logarithm,hypotenuse

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-10, 50), 40)
        self.assertEqual(add(-15, -30), -45)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(-10, 40), -50)
        self.assertEqual(subtract(-15, -15), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(10, 3), 30)
        self.assertTrue(mul(5, 3),15)
        self.assertTrue(mul(5, 4))

    def test_divide(self): # 3 assertions
        self.assertNotEqual(div(10,3), (0,0))
        self.assertEqual(div(6,3),2)
        self.assertEqual(div(25,5),5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        try:
            div(5, 0)
        except ZeroDivisionError:
            return ZeroDivisionError("Divide by zero failed.")

    def test_logarithm(self):
        self.assertEqual(logarithm(100, 10), 2)
        self.assertEqual(logarithm(65536, 2), 16)
        self.assertEqual(logarithm(390625, 5), 8)

    def test_log_invalid_base(self):
        try:
            logarithm(100, 0)
        except ValueError:
            return ValueError("Invalid base.")
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
         self.assertRaises(ZeroDivisionError)

    

    def test_hypotenuse(self): # 3 assertions
         self.assertEqual(hypotenuse(3, 4), 5)
         self.assertEqual(hypotenuse(5,12),13.0)
         self.assertTrue(hypotenuse(5.0,12.0))
        

    def test_sqrt(self): # 3 assertions
         self.assertTrue(square_root(25))
         self.assertFalse(square_root(36), 3)
         self.assertNotEqual(square_root(49), 6 )
         
    
         self.assertRaises(ValueError)
  
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()

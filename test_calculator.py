import unittest
from calculator import add,sub,div,mult,sqrt,logarithm,hypotenuse

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
     def test_multiply(self): # 3 assertions
        self.assertEqual(mult(10*3), 30)
        self.assertFalse(mult(10*3),15)
        self.assertTrue(mult(5*4) == 20)

     def test_divide(self): # 3 assertions
        self.assertNotEqual((a,b), (0,0))
        self.assertEqual(div(6,3),2)
        self.assertTrue(div(6 \ 3) == 2)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
     def test_log_invalid_argument(self): # 1 assertion
         self.assertRaises(ZeroDivisionError):
             log(0, 5)
    

     def test_hypotenuse(self): # 3 assertions
         self.assertNotEqual((a,b), (0,0)
         self.assertEqual(hypotenuse(5,12),13.0)
         self.assertTrue(hypotenuse(5.0,12.0) == 13.0)
        

     def test_sqrt(self): # 3 assertions
         self.assertTrue(sqrt(25) == 5.0)
         self.assertFalse(sqrt(36), 3)
         self.assertNotEqual((a), (-4))
         
    
        self.assertRaises(ValueError):
            sqrt(-4)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()

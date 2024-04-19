import unittest
from calculator import Calculator

class Test_calculator(unittest.TestCase, Calculator):
    
    def setUp(self):
        self.calculadora = Calculator()
        
    def test_soma(self):
        self.assertEqual(self.soma(2, 8), 10)
        
    def test_divisao_inteira(self):
        
        self.assertEqual(self.divisao(10,5),2)
        

if __name__ == '__main__':
    unittest.main()
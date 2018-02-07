import sys
import unittest
from src import isOddOrEven 
from src import isMultiple
from src import isPrime

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_even(self):
    	for n in range (0,50):
        	self.assertEqual( isOddOrEven(2+(4*n)), 'even')
 
    def test_odd(self):
    	for n in range(1,50):
        	self.assertEqual( isOddOrEven(n*2-1), 'odd')
        	
    def test_even4(self):
    	for n in range(0,50):
    		self.assertEqual( isOddOrEven(n*4), 'divisible by 4')
    		
    def test_multiples(self):
    	for a in range (1, 50):
    		for b in range (1, 50):
    			self.assertEqual( isMultiple(a*b, a), 'divides evenly')
    			self.assertEqual( isMultiple(a*b, b), 'divides evenly')
    
    def test_non_multiples(self):
    	for a in range (1,50):
    		for b in range (2,50):
    			self.assertEqual( isMultiple(a*b+1, b), 'does not divide evenly')
    
    def test_primes(self):
    	f = open('primenumbers.txt', 'r')
    	for line in f:
    		self.assertEqual( isPrime(int(line)), 'prime number' )
    		
    def test_non_primes(self):
    	for n in range(2,50):
    		self.assertEqual( isPrime(n*n), 'not a prime number')
 
if __name__ == '__main__':
    unittest.main()
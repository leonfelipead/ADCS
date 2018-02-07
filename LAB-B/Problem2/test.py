import unittest
from src import commonMembers
from src import commonMembersOneLiner
from src import createLists

class TestUM(unittest.TestCase):

	def setUp(self):
		pass

	def testCommonMembers(self):
		A,B,C = createLists([],[],[])
		self.assertEqual(commonMembers(A,B),C)

	def testCommonMembersOneLiner(self):
		A,B,C = createLists([],[],[])
		Res = commonMembersOneLiner(A,B)
		Res.sort()
		self.assertEqual(Res,C)

	def testEmpty(self):
		self.assertEqual(commonMembers([],[]),[])

	def testOneEmpty(self):
		A,B,C = createLists([],[],[])
		self.assertEqual(commonMembers(A,[]), [])

	def testSameList(self):
		A,B,C = createLists([],[],[])
		APrime = list(set(A))
		APrime.sort()
		self.assertEqual(commonMembers(A,A), APrime)

if __name__ == '__main__':
	unittest.main()
#!/usr/bin/env python

from unittest import TextTestRunner, TestLoader, TestCase

class TestNewtrino(TestCase):
	# no setUp
	# no tearDown
	
	def test_schemaparser(self):
		# TODO PMM implement test
		self.assertTrue(True, "schemaparser test not implemented")
	
	def test_dotoutput(self):
		# TODO PMM implement test
		self.assertTrue(True, "dotoutput test not implemented")
	
if __name__ == '__main__':
	# discovers test_*.py
	suite = TestLoader().discover(".")
	TextTestRunner().run(suite)
		
		

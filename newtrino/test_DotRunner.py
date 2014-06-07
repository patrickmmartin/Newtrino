#!/usr/bin/env python

from unittest import TestCase, TestLoader, TextTestRunner

class TestDotRunner(TestCase):
	def setUp(self):
		from shutil import copy2
		self.dotFile = 'database.txt'
		self.samplePath = '../sample/'
		# copy file in place from SCM safe copy
		copy2(self.samplePath + self.dotFile, self.dotFile)
		
	def tearDown(self):
		from os import remove
		# remove example files and output
		remove(self.dotFile)
		remove(self.dotFile + '.svg')
	
	def test_rundot(self):
		from dotrunner import DotRunner
		from filecmp import cmp
		dotRun = DotRunner()
		ret = dotRun.run(self.dotFile, '-Tsvg')
		self.assertTrue(ret == 0, "return code %d from running dot" % ret)
		self.assertTrue(cmp(self.samplePath + self.dotFile + '.svg', self.dotFile + '.svg'), 
				   'file output %s should be identical to base in %s' %
				   (self.samplePath, self.dotFile + '.svg')	 )
		

	
if __name__ == '__main__':
	suite = TestLoader().loadTestsFromTestCase(TestDotRunner)
	TextTestRunner().run(suite)

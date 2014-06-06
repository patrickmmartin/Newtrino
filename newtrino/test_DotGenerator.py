#!/usr/bin/env python

from unittest import TestCase

class TestDotGenerator(TestCase):
	def setUp(self):
		from shutil import copy2
		self.dotFile = 'database.txt'
		self.samplePath = '../sample/'
		
	def tearDown(self):
		from os import remove
		remove(self.dotFile)
	
	def test_generate(self):
		from dotgenerator import DotGenerator
		from filecmp import cmp
		import io
		dotGen = DotGenerator()
		
		with io.open('database.txt', 'wt') as file:
			file.write(unicode('here is some test text'))
			dotGen.generate(file)

		self.assertTrue(cmp(self.samplePath + 'database.txt', 'database.txt'), 
				   'file output %s should be identical to base in %s' %
				   (self.samplePath + 'database.txt', 'database.txt')	 )



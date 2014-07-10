#!/usr/bin/env python

from subprocess import call

class DotRunner:
	def run(self, filename, options):
		# should run dot here
		return call(["dot", options, "-O " , filename])
		
		
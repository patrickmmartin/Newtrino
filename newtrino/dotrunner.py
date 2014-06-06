#!/usr/bin/env python

from subprocess import call

class DotRunner:
	def run(self, file, options):
		# should run dot here
		return call(["dot", options, "-O " , file])
		
		
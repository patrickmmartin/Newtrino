# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Patrick Martin patrickmmartin@gmail.com 
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from setuptools import setup, find_packages

from distutils.cmd import Command
from distutils.errors import *
import os
import shutil

class CustomCommand(Command):
    user_options = []
    def initialize_options(self):
		None;
    def finalize_options(self):
		None;

class CleanCommand(CustomCommand):
    description = "custom clean command that forcefully removes dist/build directories"
    def initialize_options(self):
        self.cwd = None
    def finalize_options(self):
        self.cwd = os.getcwd()
    def removedir(self, dirname):
		# note the delete race condition: not handled by design:
		if os.path.exists(dirname):
			shutil.rmtree(dirname)
    def run(self):
        assert os.getcwd() == self.cwd, 'Must be in package root: %s' % self.cwd
        self.removedir("build")	
        self.removedir("dist")	
        self.removedir("Newtrino.egg-info")	
		
		
setup(
    name = 'Newtrino', version = '0.0.0',
    author = 'Patrick Martin', author_email = 'patrickmmartin@gmail.com',
    url = 'https://github.com/patrickmmartin',
    description = 'Very lightweight database documenter.',
	long_description = 'Very lightweight database documenter.',
    license = 'BSD',
    packages = find_packages(exclude=['*.tests*']),
	cmdclass = {'clean': CleanCommand},
#    entry_points = {
#        'trac.plugins': ['tracindexserversearch = tracindexserversearch'],	
#    }

)


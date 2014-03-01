## simple makefile - currently *nix like
default: clean all doco tests

clean:
	@echo [$@]
	@python setup.py clean

all: 
	@echo [$@]
	@python setup.py bdist_egg 

doco:
	@echo [$@]
	@pydoc -w newtrino

tests:
	@echo [$@]
	@echo tests - WRITE ME!

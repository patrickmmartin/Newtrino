## simple makefile - currently *nix like
default: clean all tests doco 

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
	@cd newtrino ; python test_newtrino.py

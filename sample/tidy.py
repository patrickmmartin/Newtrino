import sys

if __name__== "__main__":
	with open(sys.argv[1]) as f:
	   for lines in f:
		for line in lines.split(";"):
			if (line != ""): print(line + ";")
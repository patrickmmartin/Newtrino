from unittest import TextTestRunner, TestLoader, TestCase

class TestNewtrino(TestCase):
	# no setUp
	# no tearDown
	
	def test_schemaparser(self):
		self.assertTrue(False, "schemaparser test not implemented")
	
	def test_dotgenerator(self):
		self.assertTrue(False, "dotgenerator test not implemented")
		
	def test_dotoutput(self):
		self.assertTrue(False, "dotoutput test not implemented")
	
if __name__ == '__main__':
	# discovers test_*.py
	suite = TestLoader().discover(".")
	TextTestRunner().run(suite)
		
		
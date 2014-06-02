from unittest import TextTestRunner, TestLoader, TestCase

class TestNewtrino(TestCase):
	# no setUp
	# no tearDown
	
	def test_schemaparser(self):
		self.assertTrue(false, "schemaparser test not implemented")
	
	def test_dotgenerator(self):
		self.assertTrue(false, "dotgenerator test not implemented")
		
	def test_dotrunner(self):
		self.assertTrue(false, "dotrunner test not implemented")
	
if __name__ == '__main__':
	# discovers test_*.py
	suite = TestLoader().discover(".")
	TextTestRunner().run(suite)
		
		
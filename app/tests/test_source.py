import unittest
from app.models import Source

# Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    test class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        run before every test
        '''
        self.new_source = Source(1234,"newyork")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))  

    def test_init(self):
        self.assertEqual(self.new_source.id,1234)  
        self.assertEqual(self.new_source.name,"newyork") 

# if __name__ == '__main__':
    # unittest.main()            
import unittest

class Sources:
    '''
    class to define news source objects
    '''

    def __init__(self,id,name,category,description):
        self.id = id
        self.name = name
        self.category = category
        self.description = description
        
class TestSources(unittest.TestCase):
    '''
    defines test cases for the Sources class behaviours.
    
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_source = Sources("BBC-News","CNN-NEWS","business","") 


    def test_init(self):
        '''
        test if the object is initialized properly
        '''

        self.assertEqual(self.new_source.id,"BBC-News")
        self.assertEqual(self.new_source.name,"CNN-NEWS")
        self.assertEqual(self.new_source.category,"business")
        self.assertEqual(self.new_source.description,"")


if __name__ == '__main__':
    unittest.main()
import unittest

class Articles:
    '''
    class to define news articles objects
    '''
    def __init__(self,title,urlToImage,description,publishedAt,url):
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt= publishedAt
        self.url=url

class TestArticles(unittest.TestCase):
    '''
    Test class that defines test cases for the articles class behaviours.
            
    '''
    def setUp(self):
        '''
        method to run before each test cases.
        '''
        self.new_article = Articles("","","","","","") 


    def test_init(self):
        '''
         test if the object is initialized properly
        '''

        self.assertEqual(self.new_article.title,"")
        self.assertEqual(self.new_article.urlToImage,"")
        self.assertEqual(self.new_article.description,"")
        self.assertEqual(self.new_article.publishedAt,"")
        self.assertEqual(self.new_article.url,"")


if __name__ == '__main__':
    unittest.main()
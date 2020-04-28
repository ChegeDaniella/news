import unittest
from .models import Articles

# Articles = articles.Articles

class ArticlesTest(unittest.TestCase):

    def setUp(self):
        self.new_articles = Articles("20 more people dead","It was a long car accident","null",10,"Alot of things",'http//bbc')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))

    def test_init(self):
        self.assertEqual(self.new_articles.title,"20 more people dead") 
        self.assertEqual(self.new_articles.description,"It was a long car accident") 
        self.assertEqual(self.new_articles.urlToImage,"null") 
        self.assertEqual(self.new_articles.publishedAt,10)    
        self.assertEqual(self.new_articles.content,"Alot of things")
        self.assertEqual(self.new_articles.url,"http//bbc")

# if __name__ == '__main__':
    # unittest.main() 


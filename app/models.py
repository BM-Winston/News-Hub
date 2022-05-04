class Articles:
    """
    Defines objects of the news
    """


    def __init__(self, title,description,urlToImage, publishedAt, url):
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        
        self.publishedAt = publishedAt
        self.url = url

class Sources:
    """
    defines objects of the sources
    """
    def __init__(self,name, description, url):
        self.name = name
        self.description = description
        self.url = url


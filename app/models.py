class News:
    """
    Defines objects of the news
    """


    def __init__(self, title,description,urlToImage, content, publishedAt):
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt = publishedAt

class Sources:
    """
    defines objects of the sources
    """
    def __init__(self,name, description, url):
        self.name = name
        self.description = description
        self.url = url


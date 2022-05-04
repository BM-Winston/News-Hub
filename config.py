import os

class Config:
    

    
    NEWS_API_SOURCES_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    BASE_URL = 'https://newsapi.org/v2/top-headlines?category={}&apiKey={}'
    # NEWS_API_KEY = 'b3dbb2b9093b4fb4bf50993d2e0ab203'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
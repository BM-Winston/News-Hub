import os

class Config:
    pass

    
    NEWS_API_SOURCES_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = 'b3dbb2b9093b4fb4bf50993d2e0ab203'
    SECRET_KEY='SECRET_KEY'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
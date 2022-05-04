import urllib.request, json
from .models import  Articles, Sources

api_key =None

base_url = None


def configure_request(app):
    global api_key,base_url,news_api_sources_url,news_articles_url
    api_key = app.config['NEWS_API_KEY']
    # news_api_sources_url = app.config['NEWS_API_BASE_URL']
    # news_api_sources_url = app.config['NEWS_API_SOURCES_URL']
    base_url = app.config['BASE_URL']



def get_articles():
    get_news_url = 'https://newsapi.org/v2/top-headlines?category=business&language=en&apiKey=b3dbb2b9093b4fb4bf50993d2e0ab203'

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)


        news_result = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
    return news_results


def process_results(news_list):
    news_results = []
    for news_item in news_list:
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        content = news_item.get('content')
        publishedAt = news_item.get('publishedAt')


        news_object = Articles(title, description, urlToImage, content, publishedAt)
        news_results.append(news_object)

    return news_results


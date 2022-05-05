import urllib.request, json
from .models import  Articles, Sources

api_key =None

base_url = None


def configure_request(app):
    global api_key,base_url,news_api_sources_url,news_articles_url
    api_key = app.config['NEWS_API_KEY']
    




def get_articles():
    get_news_url = 'https://newsapi.org/v2/top-headlines?category=sports&language=en&apiKey={}'.format(api_key)

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
        publishedAt = news_item.get('publishedAt')
        url = news_item.get('url')


        news_object = Articles(title,description,urlToImage,publishedAt, url)
        news_results.append(news_object)

    return news_results


def get_sources():
    get_sources_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)


        news_result = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)
    return sources_results


def process_results(sources_list):
    sources_results = []
    for sources_item in sources_list:
        title = sources_item.get('title')
        description = sources_item.get('description')
     
        url = sources_item.get('url')


        news_object = Sources(title, description,  url)
        sources_results.append(news_object)

    return sources_results


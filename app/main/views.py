from flask import render_template
from  .import main
from ..requests import get_news, get_sources


@main.route('/')
def index():
    """
    Function that return news souces

    """
    news = get_news()
    title = 'News Now'
    return render_template('index.html',title = title, articles = news)

@main.route('/articles/<sources_id>')
def sources():
    '''
    Returns the articles for the given sources
    '''
    news = get_sources()
    
    return render_template('news.html',sources = news)

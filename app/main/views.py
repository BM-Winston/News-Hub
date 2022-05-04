from flask import render_template
from  .import main
from ..requests get_sources, get_articles


@main.route('/')
def index():
    """
    Function that return news souces

    """
    sources = get_sources()
    title = 'News Now'
    return render_template('index.html', sources = sources, title = title)

@main.route('/articles/<sources_id>')
def articles(sources_id):
    '''
    Returns the articles for the given sources
    '''
    articles = get_articles(sources_id)
    
    return render_template('articles.html',articles = articles)

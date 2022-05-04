from flask import render_template
from  .import main
from ..requests import get_articles


@main.route('/')
def index():
    """
    Function that return news sources

    """
    my_articles = get_articles()

    return render_template('index.html', articles= my_articles)

# @main.route('/articles/<sources_id>')
# def sources():
#     '''
#     Returns the articles for the given sources
#     '''
#     news = get_articles()
    
#     return render_template('news.html',articles = articles)

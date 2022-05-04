from flask import render_template
from  .import main
from ..requests import get_articles, get_sources


@main.route('/')
def index():
    """
    Function that return news articles

    """
    my_articles = get_articles()

    return render_template('index.html', articles= my_articles)

@main.route('/source')
def source():
    """
    Function that return news sources

    """
    my_sources = get_sources()

    return render_template('source.html', sources= my_sources)


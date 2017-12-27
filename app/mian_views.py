from flask import Blueprint, render_template
from models import Bookmarks

main = Blueprint('main', __name__)


@main.route('/')
def index():
    # for bookmark in Bookmarks.all():
    #     print(bookmark.name)
    bookmarks = Bookmarks.all()
    print(len(bookmarks))
    return render_template('index.html', bookmarks=bookmarks)

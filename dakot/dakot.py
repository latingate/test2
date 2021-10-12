from flask import Flask, redirect, request, render_template, request, session, url_for, jsonify
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_parameter

from pyPodcastParser.Podcast import Podcast
import requests

request = requests.get('https://anchor.fm/s/29360f3c/podcast/rss')
podcast = Podcast(request.content)

# https://pypodcastparser.readthedocs.io/en/latest/index.html
# https://podcastparser.readthedocs.io/en/latest/

from gs_functions import *

app = Flask(__name__)


@app.route('/podcast')
def podcast_main():
    number_of_episodes = len(podcast.items)
    episodes = podcast.items
    print(podcast.items[1].enclosure_url)
    return render_template('podcast_main.html',number_of_episodes=number_of_episodes, episodes=episodes)


if __name__ == '__main__':
    # use the line below to run flask server directly (not recommended for production)
    app.run(host='0.0.0.0', port=5000, debug=True)
    # , use_reloader=False
    # , ssl_context = 'adhoc'
    # , ssl_context=('cert.pem', 'key.pem'))
    #

    # use the line below to run flask through waitress server, and than run waitress_server.py from pycharm or directly from command line using: python waitress_server.py
    # app = Flask(__name__)

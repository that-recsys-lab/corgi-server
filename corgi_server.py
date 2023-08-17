from mastodon import Mastodon
import pandas as pd
import numpy as np
from flask import Flask, Response, jsonify
import json

corgi = Flask(__name__)

# Mastodon.create_app(
#     'corgi_server',
#     api_base_url = 'https://hci.social',
#     to_file = 'corgi_server.secret'
# )

mastodon = Mastodon(api_base_url = 'https://hci.social', access_token = 'corgi_server.secret')

first_twenty = pd.DataFrame(mastodon.timeline(limit=5))
first_twenty.to_csv("first_twenty.csv")

@corgi.route('/get_recent_posts')
def get_recent_posts():
    first_five = []

    timeline = mastodon.timeline(limit = 5)

    for post in timeline:
        # A conditional statement to determine whether a status update is boosted or not.
        # If a post's reblog attribute returns 'None', then only append the username and content.
        if (post.reblog == None):
            first_five.append({
                'username': post.account.username,
                'content': post.content,
                'reblogged_user': None,
                'reblogged_content': None
            })
        # Otherwise, append the username and content of the boosted post.
        else:
            first_five.append({
                'username': post.account.username,
                'content': None,
                'reblogged_user': post.reblog.account.username,
                'reblogged_content': post.reblog.content
            })

    # This returns a .json-formatted data request
    # return jsonify(first_five)

    # This returns an easy-to-read .json format of the collected data
    json_output = json.dumps(first_five, indent = 4)
    return Response(json_output, content_type='application/json')

    # Another method for returning an easy-to-read .json format of the collected data
    # return json.dumps(first_five, indent = 4)

@corgi.route('/')
def index():
    return "Welcome to CORGI"
#
# Might make more sense to refactor this in the future where status.py and timeline.py is its own file but that's a future problem.
# Collecting of timelines API calls
# -----------------------------
@corgi.route('/api/v1/timelines/public', methods = ["GET"]) 
def get_public_timeline(headers=None, local=True, remote=False, only_media=False, max_id=None, since_id=None, min_id=None, limit=20):
    print("Getting public timeline")
    return Response(status = 200)
# -----------------------------
@corgi.route('/api/v1/timelines/tag/<hashtag>', methods = ["GET"])
def get_hashtag_timeline(hashtag, headers=None, any=[], all=[], none=[], local=True, remote=False, only_media=False, max_id=None, since_id=None, min_id=None, limit=20):
    print("Getting hashtag timeline")
    return Response(status = 200)
# -----------------------------
@corgi.route('/api/v1/timelines/home', methods = ["GET"])
def get_home_timeline(headers=None, max_id=None, since_id=None, min_id=None, limit=20):
    print("Getting home timeline")
    return Response(status = 200)
# -----------------------------
@corgi.route('/api/v1/timelines/list/<list_id>', methods = ["GET"])
def get_list_timeline(list_id, headers=None, max_id=None, since_id=None, min_id=None, limit=20):
    print("Getting list timeilne")
    return Response(status = 200)
# -----------------------------

if __name__ == '__main__':
    corgi.run()
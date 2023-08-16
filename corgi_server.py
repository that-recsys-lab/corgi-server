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

# first_twenty = pd.DataFrame(mastodon.timeline(limit=5))
# first_twenty.to_json("first_twenty.jsond")

@corgi.route('/get_recent_posts')
def get_recent_posts():
    first_five = []

    timeline = mastodon.timeline(limit=5)

    for post in timeline:
        print(post)
        first_five.append({
            'username': post.account.username,
            'content': post.content
        })

    # This returns a .json-formatted data request
    # return jsonify(first_five)

    # This returns an easy-to-read .json format of the collected data
    # json_output = json.dumps(first_five, indent=4)
    # return Response(json_output, content_type='application/json')

    # Another method for returning an easy-to-read .json format of the collected data
    return json.dumps(first_five, indent = 4)

if __name__ == '__main__':
    corgi.run()
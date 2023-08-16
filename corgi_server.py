from mastodon import Mastodon
import pandas as pd
import numpy as np

# Mastodon.create_app(
#     'corgi_server',
#     api_base_url = 'https://hci.social',
#     to_file = 'corgi_server.secret'
# )

mastodon = Mastodon(api_base_url = 'https://hci.social', access_token = 'corgi_server.secret')

first_twenty = pd.DataFrame(mastodon.timeline(limit=20))
first_twenty.to_csv("first_twenty.csv")


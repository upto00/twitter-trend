import os, ssl, certifi
os.environ['SSL_CERT_FILE'] = certifi.where()
ssl._create_default_https_context = ssl._create_unverified_context

import snscrape.modules.twitter as sntwitter

query = "lang:ja min_retweets:500"
links = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    links.append(f"https://twitter.com/{tweet.user.username}/status/{tweet.id}")
    if i >= 9:
        break

for idx, link in enumerate(links, start=1):
    print(f"▼{idx}位\n{link}\n")

input("終了するにはEnterを押してください")

import os

_root = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(_root, 'data')
corpus_file = os.path.join(data_dir, "corpus.json")
model_dir = os.path.join(_root, "models")
processed_text_file = os.path.join(model_dir, "processed_tweets.txt")

model_name = "124M"

n_tweet_chars = 280
tweet_delimiter = "<END TWEET>"
link_placeholder = "<LINK>"

generate_length = n_tweet_chars + len(tweet_delimiter)
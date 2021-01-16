import json
import pandas as pd

import config


def get_links(text):
    """Grabs links as they typically appear in tweets from input text."""
    keys = ["pic.twitter.com", "http"]
    links = [s for s in text.split() if any(k in s for k in keys)]
    return links


def text_contains_link(text):
    """Determines whether a tweet contains a link"""
    links = get_links(text)
    return len(links) > 0


def replace_links(text):
    """Replace links with a placeholder."""
    links = get_links(text)
    res = text
    for link in links:
        res = res.replace(link, config.link_placeholder)
    return res


def load_corpus(earliest=None, latest=None):
    """Reads in the tweets."""
    with open(config.corpus_file) as f:
        dicts = json.load(f)

    data = {}
    data["id"] = [d["id"] for d in dicts]
    texts = [d["text"] for d in dicts]
    data["text"] = texts
    data["retweet"] = [d["isRetweet"] == 't' for d in dicts]
    data["contains_link"] = [text_contains_link(s) for s in texts]
    data["date"] = [d["date"].split(" ")[0] for d in dicts]

    df = pd.DataFrame(data=data)

    if not earliest:
        earliest = min(df["date"])
    if not latest:
        latest = max(df["date"])

    df = df[(df["date"] >= earliest) & (df["date"] <= latest)].copy()
    return df


def process_tweet(text):
    """Prepares a tweet for use in GPT-2 model. Replaces links with placeholders and inserts end of tweet tokens."""
    res = replace_links(text)
    res += config.tweet_delimiter
    return res


def process_tweets(earliest="2015-05-01", latest=None, include_urls=False):
    """Processes all tweets and saves them."""
    df = load_corpus(earliest=earliest, latest=latest)
    if not include_urls:
        df = df[~df["contains_link"]]
    processed = [process_tweet(s) for s in df["text"]]

    output = "\n\n".join(processed)
    with open(config.processed_text_file, "w") as f:
        f.write(output)

import gpt_2_simple as gpt2

import config
import utils


def download_model(model_name=None):
    """Downloads a pre-trained GPT-2 model and stores it locally."""
    if not model_name:
        model_name = config.model_name
    gpt2.download_gpt2(model_dir=config.model_dir, model_name=model_name)


class TweetGenerator:
    def __init__(self):
        self.sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(self.sess)

    def generate(self):
        texts = gpt2.generate(
            self.sess,
            return_as_list=True,
            model_name=config.model_name,
            model_dir=config.model_dir,
            length=config.generate_length,
            truncate=config.tweet_delimiter,
            temperature=0.90)

        text = texts[0]
        longest_par = max(text.split("\n\n"), key=lambda s: len(s))

        return longest_par


def train_model(steps=100):
    sess = gpt2.start_tf_sess()
    gpt2.finetune(
        sess,
        config.processed_text_file,
        model_name=config.model_name,
        steps=steps)

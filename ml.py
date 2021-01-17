import gpt_2_simple as gpt2

import config
import utils


def download_model(model_name=None):
    """Downloads a pre-trained GPT-2 model and stores it locally."""
    if not model_name:
        model_name = config.model_name
    gpt2.download_gpt2(model_dir=config.model_dir, model_name=model_name)


class TweetGenerator:
    """Just a class to handle content generation."""

    def __init__(self):
        self.sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(self.sess)

    def generate(self, temperature=0.90):
        """Generate a content for a single tweet.
        temperature is a free parameter in the softmax function in the final neural network layer which controls
        'randomness', i.e. low temperatures gives content with more 'boring' words that are more common in training
        data, whereas higher temperatures gives more random content."""

        texts = gpt2.generate(
            self.sess,
            return_as_list=True,
            model_name=config.model_name,
            model_dir=config.model_dir,
            length=config.generate_length,
            truncate=config.tweet_delimiter,
            temperature=temperature)

        # gpt returns a list by default. Grab the text in it.
        text = texts[0]
        # Training data is separated by double newlines. Grab the longest paragraph
        longest_par = max(text.split("\n\n"), key=lambda s: len(s))

        return longest_par


def train_model(steps=1000):
    """Trains the GPT-2 model for the specified number of steps."""

    sess = gpt2.start_tf_sess()
    gpt2.finetune(
        sess,
        config.processed_text_file,
        model_name=config.model_name,
        steps=steps)

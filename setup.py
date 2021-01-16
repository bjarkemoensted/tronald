import utils
import ml


def print_status(*args, **kwargs):
    sep = 42*"*"
    print(sep)
    print("***", end=" ")
    print(*args, **kwargs)
    print(sep)


def main():
    print_status("Downloading GPT-2 model")
    ml.download_model()

    print_status("Preprocessing tweets")
    utils.process_tweets()

    print_status("Training model")
    ml.train_model()


if __name__ == '__main__':
    main()

"""Generate markov models and try output some sentences."""
import argparse
import markovify

if __name__ == '__main__':
    # Get raw text as string.

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--file', type=str, default='corpus.txt',
        help='File path that contains the corpus')
    args = parser.parse_args()

    with open(args.file) as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text)

    # Print five randomly-generated sentences
    # for i in range(5):
    #     print(text_model.make_sentence())

    # Print three randomly-generated sentences of no more than 140 characters
    for i in range(10):
        print(text_model.make_short_sentence(140))

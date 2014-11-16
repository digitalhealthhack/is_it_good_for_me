from nltk import pos_tag
from nltk.tokenize import RegexpTokenizer
from collections import Counter

def get_conclusions_contents():
    with open('conclusions.txt', 'r') as text_file:
        contents = text_file.read()
    return contents


def text_analysis(contents):
    # DONOT USE
    tokens = pos_tag(contents.encode('unicode-escape'))

    with open('text_analysis.txt', 'w') as out_file:
        for token in tokens:
            out_file.write('{} {}\n'.format(token[0], token[1]))


def words(contents):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = Counter(tokenizer.tokenize(contents))

    with open('words.txt', 'w') as out_file:
        for token in tokens.most_common(100):
            out_file.write('{} {}\n'.format(token[0], token[1]))


def main():
    contents = get_conclusions_contents()
    words(contents)

main()

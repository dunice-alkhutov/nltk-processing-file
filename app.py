"""Module to create n-grams.

@ params will be described here
"""
# import string


# def main():
#     stop = stopwords.words('english') + string.punctuation + '\n'
#     with open('text.txt', 'r') as sample_file:
#         for line in sample_file:
#             print('*', [i for i in word_tokenize(line.lower()) if i not in stop])

# if __name__ == "__main__":
#     main()
#########

import sys, getopt
import nltk
import re
import string
from string import maketrans
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams

def word_grams(text, n):
    print('text',text)
    s = []
    for ngram in ngrams(text, n):
        print('ngram', ngram)
        s.append(tuple(ngram))
    return s

def process_file(path, n):
    """
    Process file
    @path is path to file what is needed to process
    @n is number of n-grams
    """
    print word_grams('one two three four'.split(' '), n)
    # with open('text.txt', 'r') as sample_file:
    #     for line in sample_file:
    #         print('*', [i for i in word_tokenize(line.lower()) if i not in stop])
    print('Start processing...')
    try:
        sample_file = open(path, 'r')
        read_file = sample_file.read()
        print(read_file)
        stop = string.punctuation + '\n'
        print(stop)
        file_content = re.split(r'\s+|[,;:.-]\s*|\\n', read_file)
        print(file_content)
        print('Result:{}'.format(word_grams(file_content, n)))
    except (IOError, TypeError) as ex:
        print('FILE ERROR! {}'.format(ex))
        print('You may forgot -p flag with value')

def main(argv):
    ngrams = 2
    path = None
    try:
        opts, args = getopt.getopt(argv,"n:p:",["ngrams=","path="])
    except getopt.GetoptError as ex:
        print(ex)
        print('example: "python app.py -n 2" for 2-grams')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-n':
            ngrams = arg
        elif opt == '-p':
            path = arg
        else:
            sys.exit()

    process_file(path, int(ngrams))

if __name__ == "__main__":
   main(sys.argv[1:])
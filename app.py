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
from datetime import datetime
from string import maketrans
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
# from sklearn.feature_extraction.text import CountVectorizer

def word_grams(text, n):
    """
    Create list with ngrams
    """
    ngram_list = []
    for ngram in ngrams(text, n):
        ngram_list.append(tuple(ngram))
    return ngram_list

def process_file(path, n):
    """
    Process file
    @path is path to file what is needed to process
    @n is number of n-grams
    """
    # print word_grams('one two three four'.split(' '), n)
    print('* Start processing...')
    try:
        sample_file = open(path, 'r')
        read_file = sample_file.read()
        stop = string.punctuation + '\n'
        file_content = re.split(r'\s+|[,;:.-]\s*|\\n', read_file)
        print("* Removed specsymbols and punctuation")

        filtered_words = [word for word in file_content if word not in stopwords.words('english')]
        print("* Removed stop words")

        fdist = nltk.FreqDist(word_grams(filtered_words, n))
        top10 = sorted(fdist.items(), key=lambda x: x[1], reverse=True)[:10]
        print('TOP10 result:')
        for k,v in top10:
            print k,v
    except (IOError, TypeError) as ex:
        print('FILE ERROR! {}'.format(ex))
        print('You may forgot -p flag with value')


def main(argv):
    """
    Starting function
    Variable 'ngrams' has default value - 2
    """
    
    start_time = datetime.now()
    n_grams = 2
    path = None
    try:
        opts, _ = getopt.getopt(argv, "n:p:", ["ngrams=", "path="])
    except getopt.GetoptError as ex:
        print(ex)
        print('example: "python app.py -n 2" for 2-grams')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-n':
            n_grams = arg
        elif opt == '-p':
            path = arg
        else:
            sys.exit()

    process_file(path, int(n_grams))
    end_time = datetime.now()
    delta = end_time - start_time
    # print(delta.total_seconds())
    # m, s = divmod(delta.total_seconds(), 60)
    # h, m = divmod(m, 60)
    # print "It talkes %d hours %02d minutes and %02d seconds" % (h, m, s)
    print("It talkes {} seconds".format(delta.total_seconds()))
if __name__ == "__main__":
    main(sys.argv[1:])

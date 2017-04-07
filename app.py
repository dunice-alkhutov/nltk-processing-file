"""Module to create n-grams.

@ params will be described here
"""
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


def word_grams(text, ngram_list, n = 0):
    """
    Create list with ngrams
    """
    
    n_min = 1
    n_max = 4
    if n != 0:
        n_min = n_max = n
    for n_ in range(n_min, n_max+1):
        for ngram in ngrams(text, n_):
            try:
                ngram_list[str(n_)].append(tuple(ngram))
            except KeyError as ex:
                ngram_list[str(n_)] = []
                ngram_list[str(n_)].append(tuple(ngram))
    return ngram_list


def process_file(path, n, top_number, print_result_to_terminal=False, add_stats=False):
    """
    Process file
    @path is path to file what is needed to process
    @n is number of n-grams
    """
    print('* Start processing...')
    try:
        sample_file = open(path, 'r')
        read_file = sample_file.read()
        file_sentenses = re.split(r'\s*[,.\-;\'()\/*\/+<=>?@[\]^_`{|}]\s*|[,.\-;\'()\/*\/+<=>?@[\]^_`{|}]|\\t|\\f|\\v|\\n|\\r', read_file)
        print("* [Completed step 1 of 3] Removed specsymbols and punctuation")
        
        print("* Staring create ngrams")
        ngram_list = {}
        for sentense in file_sentenses:
            created_ngrams = word_grams(sentense.split(' '), ngram_list, n)
        print("* [Completed step 2 of 3] Created ngrams")

        stop = stopwords.words('english') + ['']

        def has_stop(words):
            for word in words:
                if word in stop:
                    return True
            return False

        def lo_lower(words):
            return tuple(word.lower().strip() for word in words if '' not in words)

        print('* Start removing stopwords and writting to files')
        for n_, arr in ngram_list.items():
            filtered_words = [lo_lower(words) for words in arr if not has_stop(words)]
            print("-Removed stop words for {}-grams".format(n_))
            fdist = nltk.FreqDist(filtered_words)

            result = sorted(fdist.items(), key=lambda x: x[1], reverse=True)
            write_result(result, n_, add_stats)
            top = result[:top_number]

            if print_result_to_terminal:
                print('TOP{} result for {}-grams:'.format(top_number, n_))
                for k,v in top:
                    print k,v
        print('* [Completed step 3 of 3] Removing stopwords and writting to files')
        return result

    except (IOError, TypeError) as ex:
        print('FILE ERROR! {}'.format(ex))
        print('You may forgot -p flag with value')


def write_result(result, n, add_stats):
    """
    Write stats to file
    @result is result of file processing
    @n is n-grams, needed to choose target file to write
    """
    file_name = '{}-grams'.format(n)
    print("-Starting write to file {}".format(file_name))
    f = open(file_name, 'w')
    f.write('{}-grams \t frequency\n'.format(n))
    if not add_stats:
        f.write('[')

    for words, value in result:
        if add_stats:
            f.write('{0} {1} \n'.format(words, value))
        else:
            f.write('{},\n'.format(words))

    if not add_stats:
        f.write(']')
    f.close()
    print("-Writing to file {} completed".format(file_name))


def main(argv):
    """
    Starting function
    Variable 'ngrams' has default value - 2
    """
    start_time = datetime.now()

    n_grams = 0
    path = None
    top_number = 10
    enable_printing = False
    add_stats = False
    try:
        opts, _ = getopt.getopt(argv, "n:p:t:e h s", ["ngrams=", "path=", "top_number="])
    except getopt.GetoptError as ex:
        print(ex)
        print("See help by 'python app.py -h'")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            message = '''You can use next flags:
            -p  path to file
            -h  show help
            -n  process file only for this grams (need number)
            -e  enable additional printing to terminal
            -t  show top results for each n-grams(works only with -e, need number)
            -s  put statistics to output files
            Example: "python app.py -p /path/to/file -n 2" for 2-grams'''
            print(message)

            sys.exit()
        if opt == '-n':
            n_grams = 4 if int(arg) > 4 else int(arg)
        elif opt == '-p':
            path = arg
        elif opt == '-t':
            top_number = int(arg)
        elif opt == '-e':
            enable_printing = True
        elif opt == '-s':
            add_stats = True
        else:
            sys.exit()
    process_file(path, n_grams, top_number, enable_printing, add_stats)

    end_time = datetime.now()
    delta = end_time - start_time
    m, s = divmod(int(delta.total_seconds()), 60)
    print "It talkes %02d minutes and %02d seconds" % (m, s)
if __name__ == "__main__":
    main(sys.argv[1:])

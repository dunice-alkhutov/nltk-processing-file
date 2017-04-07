Python tool to find a histogram of most common n-grams where n=1,2,3, or 4 in a body of text
==========

Instalation
-----------

You need install nltk lib:

```shell
$ pip install nltk
```

Quick start
-----------
Example running comand:
```shell
$ python app.py -n 2 -p text.txt -e -t 10
```
This command will process _text.txt_ file, write result to 2-grams(_-n_ flag) file and show in console(_-e_ flag) top 10(_-t_ flag) the most common 2-grams

Running without _-n_ flag will write n-grams from 1-gram to 4-gram to the relevant files: 1-grams, 2-grams, etc


You can type
```shell
$ python app.py -h
```
to see all flags and them description

create_random_sample.py
-----------
There is help script `create_random_sample.py`
It can create small sample file to test

Usage:
```shell
$ python create_random_sample.py -s src.txt -d dest.txt -n 150
```

Also you can see it help by
```shell
$ python create_random_sample.py -h
```
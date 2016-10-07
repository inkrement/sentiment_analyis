#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textblob.classifiers import NaiveBayesClassifier
import pickle
import os.path
import hashlib
from textblob import TextBlob
import json

DEBUG=True

trained_classifier = 'nb.classifier'

def loadSet(path, polarity):
    sentences = []
    with open(path) as f:
        for line in f:
            sentences.append((line, polarity))
    return sentences

def storeClassifier(object):
    file = open(trained_classifier ,'wb')
    pickle.dump(object,file)

def loadClassifier():
    with open(trained_classifier, 'rb') as handle:
        return pickle.load(handle)


test = [
    ('Ohne Köttbullar seid ihr nichts!', 'neg'),
    ('Bitte um Erklärung !!!', 'neg'),
    ('ich bin enttäuscht', 'neg'),
    ('IKEA ich liebe dich :D ♥', 'pos'),
    ('Ein tolles blau gelbes Bild...', 'pos'),
    ('Besser als im Kino hier :D', 'pos')
    ]

train = loadSet('negativ.txt', 'neg') + loadSet('positiv.txt', 'pos')


if os.path.isfile(trained_classifier) and not DEBUG:
    nb_cl = loadClassifier()
else:
    nb_cl = NaiveBayesClassifier() #train
    storeClassifier(nb_cl)

print(nb_cl.accuracy(test))

nb_cl.show_informative_features(30)


for i in test:
    blob = TextBlob(i[0], classifier=nb_cl)
    print(i)
    print(blob.classify())
#test_sentence = "ich mag sie wirklich über alles"
#print ("NaiveBayes: %d,%d" % (nb_cl.prob_classify(test_sentence).prob("positive"),nb_cl.accuracy(test)) )

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textblob_de import TextBlobDE as TextBlob

blob = TextBlob("Ich mag nicht Tee.")

print(blob.sentiment)

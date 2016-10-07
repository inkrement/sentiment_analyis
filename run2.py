import spacy

nlp = spacy.load('de')
doc = nlp(u'Ich bin ein Berliner.')

print(' '.join('{word}/{tag}'.format(word=t.orth_, tag=t.pos_) for t in doc))

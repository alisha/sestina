import json, random, requests
import secret
from pprint import pprint

# Build corpus
# Datasets in "data" are from corpora
# https://github.com/dariusk/corpora
corpus = json.load(open('data/objects/objects.json'))['objects']
oneWordCorpus = [x for x in corpus if x.count(' ') == 0]

# Grab six words from corpus, will be at the end of each line
# Right now these will just be nouns
# TODO: add support for other types of words
repeated_words = []
for x in xrange(0,6):
  index = random.randrange(len(oneWordCorpus))
  repeated_words.append(oneWordCorpus[index])

# Generate phrases that contain sets of words
# Generate verbs
all_verbs = json.load(open('data/words/verbs.json'))['verbs']
verbs = []
for verb in all_verbs:
  verbs.append(verb['past'])

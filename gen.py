import json, random
import secret
from pprint import pprint

# Build corpus
# Datasets in "data" are from corpora
# https://github.com/dariusk/corpora
corpus = json.load(open('data/objects/objects.json'))['objects']
oneWordCorpus = [x for x in corpus if x.count(' ') == 0]

# Grab six words from corpus
# Right now these will just be nouns
# TODO: add support for other types of words
repeated_words = []
for x in xrange(0,6):
  index = random.randrange(len(oneWordCorpus))
  repeated_words.append(oneWordCorpus[index])

pprint(repeated_words)
# Generate phrases that contain sets of words

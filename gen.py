import json, random, requests, tracery
import secret
from pprint import pprint
from tracery.modifiers import base_english

# DATA COLLECTION

# Build corpus
# Datasets in "data" are from corpora
# https://github.com/dariusk/corpora
corpus = json.load(open('data/objects/objects.json'))['objects']
one_word_corpus = [x for x in corpus if x.count(' ') == 0]

# Grab six words from corpus, will be at the end of each line
# Right now these will just be nouns
# TODO: add support for other types of words
repeated_words = []
for x in xrange(0,6):
  index = random.randrange(len(one_word_corpus))
  repeated_words.append(one_word_corpus[index])
  del one_word_corpus[index]

# Get occupations
occupations = json.load(open('data/humans/occupations.json'))['occupations']

# Get verbs
all_verbs = json.load(open('data/words/verbs.json'))['verbs']
verbs = []
for verb in all_verbs:
  verbs.append(verb['past'])

# POEM GENERATION

# Sestina poem structure
poem_structure = [
  [1,2,3,4,5,6],
  [6,1,5,2,4,3],
  [3,6,4,1,2,5],
  [5,3,2,6,1,4],
  [4,5,1,3,6,2],
  [2,4,6,5,3,1]
]

# Tracery rules
rules = {
  'origin': 'The #occupation# #verb# #object.a#',
  'occupation': occupations,
  'verb': verbs,
  'object': repeated_words
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
print grammar.flatten("#origin#")

# Build a poem
for stanza in xrange(0,6):
  for line in xrange(0,6):
    # This word must occur at the end of the line
    special_word = repeated_words[poem_structure[stanza][line] - 1]
    rules['object'] = special_word
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    print grammar.flatten("#origin#")

  print "\n"

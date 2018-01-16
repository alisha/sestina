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
repeated_words = [''] * 6
def generate_repeated_words(repeated_words):
  for x in xrange(0,6):
    index = random.randrange(len(one_word_corpus))
    repeated_words[x] = one_word_corpus[index]

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

# Build a poem
# Print to absurdist-unity.txt
f = open('absurdist-unity', 'w')

total_words = 0

while total_words < 50000:
  generate_repeated_words(repeated_words);

  # Title
  f.write("A Tale of " + repeated_words[random.randrange(len(repeated_words))] + " and " + repeated_words[random.randrange(len(repeated_words))] + "\n\n")

  # Stanzas 1-5
  for stanza in xrange(0,6):
    line_num = 0
    line = ""
    while line_num < 6:
      if stanza != 5:
        # This word must occur at the end of the line
        special_word = repeated_words[poem_structure[stanza - 1][line_num - 1] - 1]

        # Generate Tracery rules
        rules['origin'] = 'The #occupation# #verb# #object.a#'
        rules['object'] = special_word
        grammar = tracery.Grammar(rules)
        grammar.add_modifiers(base_english)
        line = grammar.flatten("#origin#")

      # Last stanza has a special structure
      else:
        # Generate Tracery rules
        rules['origin'] = 'The #occupation# #verb# #object1.a# and #object2.a#'
        rules['object1'] = repeated_words[poem_structure[stanza - 1][line_num - 1] - 1]
        rules['object2'] = repeated_words[poem_structure[stanza - 1][line_num] - 1]

        rules['object'] = special_word
        grammar = tracery.Grammar(rules)
        grammar.add_modifiers(base_english)
        line = grammar.flatten("#origin#")

        line_num += 1

      f.write(line + "\n")
      total_words += len(line.split())
      line_num += 1

    f.write("\n")

  f.write("\n\n")

f.write("\nTOTAL WORDS: " + str(total_words))
f.close()


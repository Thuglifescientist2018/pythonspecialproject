nums = [x for x in range(1, 10)]

phrases  = [
    "satawa",
    "sudhrida",
    "tiraanka",
    "chaarpani",
    "prachastha",
    'chhawastha',
    "satatwa",
    "asthastwa",
    "nawama",
    "dasata"
]
affirmitions = [
    "ma",
    "chetanaa",
    "dharana",
    "ahankaara",
    "bajramurti",
    "shalyasa",
    "ghrutan",
    "nuwanka",
    "ghrasanam",
    "chuptarthi"
]

voices = [ 
  'dha', 'wa', 'ma', 'pa', 'ka', 
  'sha', 'sa', 'na', 
]

# print(len(phrases), len(affirmitions))
for phrase in range(len(phrases)):
  print(phrases[phrase], affirmitions[phrase])

import random 

print(random.choice(voices))
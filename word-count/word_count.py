import string

def clean_word(word):
  new_word = word.strip(string.punctuation).lower()
  return new_word

# list comprehension

def extract_words(phrase):
  phrase = phrase.replace('_', ' ').replace(',', ' ')
  words = phrase.split()
  return words

def word_count(phrase):
  wc = {}
  words = [clean_word(w) for w in extract_words(phrase)]

  for word in words:
    if word:
      if word in wc:
        wc[word] += 1
      else:
        wc[word] = 1
  return wc
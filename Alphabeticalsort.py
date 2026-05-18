#Write a python program to sort the sentence in alphabetical order
def sort_sentence(sentence):
  """Sorts the words in a sentence alphabetically.
  Args:
      sentence: The sentence to sort.
  Returns:
      A new string with the words sorted alphabetically.
  """
  # Split the sentence into words
  words = sentence.split()
  # Sort the list of words
  sorted_words = sorted(words)
  # Join the sorted words back into a sentence
  return " ".join(sorted_words)
# Example usage
sentence = "This is a sentence to be sorted."
sentence=sentence.lower()
sorted_sentence = sort_sentence(sentence)
print(sorted_sentence)

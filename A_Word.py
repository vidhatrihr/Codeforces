word = input()
new_word = []
for x in word:
  if x.isupper():
    new_word.append(x.lower())
  else:
    new_word.append(x)
  # if len(word.upper()) > len(word.lower()):
  #   new_word.append(x.upper())
print(''.join(new_word))

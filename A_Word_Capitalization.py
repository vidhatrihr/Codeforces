word = input()

for x in range(len(word)):
  if x == 0:
    new_word = word[x].upper()+word[1:]
    print(new_word)

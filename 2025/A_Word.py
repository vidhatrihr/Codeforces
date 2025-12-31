word = input()

upper = ''
lower = ''

for char in word:
  if char == char.upper():
    upper += char
  else:
    lower += char
  if len(upper) > len(lower):
    word = word.upper()
  else:
    word = word.lower()

print(word)

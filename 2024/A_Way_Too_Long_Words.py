T = int(input())

for _ in range(T):
  word = input()
  if len(word) <= 10:
    print(word)
  else:
    abbreviate = f'{word[0]}{len(word)-2}{word[-1]}'
    print(abbreviate)

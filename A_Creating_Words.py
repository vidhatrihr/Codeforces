T = int(input())

for _ in range(T):
  word1, word2 = input().split()
  new_word1 = word2[0]+word1[1:]
  new_word2 = word1[0]+word2[1:]

  print(f'{new_word1} {new_word2}')

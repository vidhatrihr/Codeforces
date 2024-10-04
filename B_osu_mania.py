T = int(input())

for _ in range(T):
  n = int(input())
  cols = []
  for _ in range(n):
    row = input()
    cols.append(str(row.index('#')+1))
  print(' '.join(cols[::-1]))

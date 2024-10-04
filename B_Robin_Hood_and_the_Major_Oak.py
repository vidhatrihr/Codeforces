T = int(input())

for _ in range(T):
  n, k = map(int, input().split())
  nos_even = 0
  nos_odd = 0

  # goal 6E 6O : nos_even  nos_odd
  if n % 2 == 0:
    if k % 2 == 0:
      nos_even = k // 2
      nos_odd = k // 2
    else:
      nos_even = k // 2 + 1
      nos_odd = k // 2
  else:
    if k % 2 == 0:
      nos_even = k // 2
      nos_odd = k // 2
    else:
      nos_even = k // 2
      nos_odd = k // 2 + 1

  # print(nos_even, nos_odd)
  # goal E / O

  if nos_even % 2 == 0 and nos_odd % 2 == 0:
    print('YES')
  elif nos_even % 2 == 0 and nos_odd % 2 == 1:
    print('NO')
  elif nos_even % 2 == 1 and nos_odd % 2 == 0:
    print('YES')
  elif nos_even % 2 == 1 and nos_odd % 2 == 1:
    print('NO')

T = int(input())

for _ in range(T):
  n, k = map(int, input().split())
  people = list(map(int, input().split()))

  wallet = 0
  count = 0
  for gold in people:
    if gold >= k:
      wallet += gold
    elif gold == 0 and wallet > 0:
      wallet -= 1
      count += 1
  print(count)

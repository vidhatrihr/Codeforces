T = int(input())

for _ in range(T):
  a, b = map(int, input().split())
  array = []
  for c in range(a, b+1):
    array.append((c-a)+(b-c))
  print(min(array))

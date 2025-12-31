n, m = map(int, input().split())


def is_prime(x):
  for i in range(2, int(x**0.5)+1):
    if x % i == 0:
      return False
  return True


my_prime = 0
for i in range(n+1, 50):
  if is_prime(i):
    my_prime = i
    break

if my_prime == m:
  print('YES')
else:
  print('NO')

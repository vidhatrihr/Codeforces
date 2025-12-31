import math
T = int(input())

for _ in range(T):
  x, y, k = map(int, input().split())
  x_steps = math.ceil(x/k)
  y_steps = math.ceil(y/k)
  # clip = abs(x_steps-y_steps) - 1
  # ans = x_steps+y_steps + clip
  # if x < y:
  #   ans += 1
  # if x_steps == x:
  #   ans -= 1
  # elif y_steps == y:
  #   ans -= 1
  # print(ans)

  clip = 1
  if x < y or x_steps == y_steps:
    clip = 0
  print(x_steps + y_steps + abs(x_steps-y_steps)-clip)

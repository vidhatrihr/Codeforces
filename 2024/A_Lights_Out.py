light_grid = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
]

pressed = []
for i in range(3):
  pressed.append([int(x) for x in input().split()])


def toggle(i, j):
  if 0 <= i < 3 and 0 <= j < 3:
    light_grid[i][j] = 1 if light_grid[i][j] == 0 else 0


for i in range(3):
  for j in range(3):
    if pressed[i][j] % 2 == 1:
      toggle(i, j)
      toggle(i, j+1)
      toggle(i, j-1)
      toggle(i+1, j)
      toggle(i-1, j)

for row in light_grid:
  print(''.join([str(num) for num in row]))

n = int(input())
result = 0
for _ in range(1, n+1):
  operation = input()
  if operation == '++X' or operation == 'X++':
    result += 1
  # print(result)
  if operation == '--X' or operation == 'X--':
    result -= 1
print(result)

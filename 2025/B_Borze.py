mapping = {
    ".": '0',
    "-.": '1',
    "--": '2'
}
message = input()

encoded = ''

i = 0
while i < len(message):
  unit1 = message[i]
  if unit1 in mapping:
    encoded += mapping[unit1]
    i += 1
    continue

  if i < len(message) - 1:
    unit2 = message[i] + message[i+1]
    if unit2 in mapping:
      encoded += mapping[unit2]
      i += 2

print(encoded)

num1 = input()
num2 = input()

new_num = ''
for i in range(len(num1)):
  new_num += str(int(num1[i] != num2[i]))

print(new_num)

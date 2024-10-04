# sum of all vectors must be zero
# 3 vectors as input

T = int(input())

for _ in range(T):
    x, y, z = list(map(int, input().split()))

    sum = x + y + z
    # print(sum)
    vector_sum = 0
for vectors in range(T):
    vector_sum += sum
    # print(vector_sum)
    if vector_sum == 0:
        print('YES')
    else:
        print('NO')

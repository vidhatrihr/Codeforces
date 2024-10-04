T = int(input())

for _ in range(T):
    x, y = list(map(int, input().split()))
    
    if x < y:
        print(x, y)
    else:
        print(y, x)
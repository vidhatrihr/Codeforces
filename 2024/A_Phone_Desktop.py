import math
T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    screens_used = math.ceil(y/2)
    unused_cells = (screens_used*15) - (y*4)

    if unused_cells >= x:
        print(screens_used)
        continue

    x -= unused_cells
    screens_used += math.ceil(x/15)
    print(screens_used)

    # T = int(input())

    # for _ in range(T):
    #     x, y = map(int, input().split())
    #     screens_used = math.ceil(y/2)
    #     unused_cells = (screens_used*15) - (y*4)

    #     if unused_cells >= x:
    #         print(screens_used)
    #         continue

    #     x -= unused_cells
    #     screens_used += math.ceil(x/15)
    #     print(screens_used)
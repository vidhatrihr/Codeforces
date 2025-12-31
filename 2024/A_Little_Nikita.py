T = int(input())

for _ in range(T):
    x, y = list(map(int,input().split()))

    if x == y:
        print('yes')
    elif x > y:
        z = x - y
         
        if z % 2 == 0:
            print('yes')
        else:
            print('no') 
    else:
        print('no')
       


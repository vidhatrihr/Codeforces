n = int(input())

nums = list(map(int, input().split()))

count = 0
max_num = max(nums)
min_num = min(nums)

print(nums.index(max_num))

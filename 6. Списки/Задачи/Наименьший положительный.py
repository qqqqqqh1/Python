nums = list(map(int, input().split()))
print(min(nums, key=lambda x: x if x > 0 else 1001))
nums = list(map(int, input().split()))
count = 1
for i in range(len(nums) - 1):
    if nums[i] != nums[i + 1]:
        count += 1
print(count)

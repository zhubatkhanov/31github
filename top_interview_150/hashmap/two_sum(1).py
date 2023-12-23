from collections import defaultdict

def twoSum(nums, target):
    dict = defaultdict(int)

    for i in range(len(nums)):
        if target - nums[i] in dict:
            return i, dict[target - nums[i]]
        else:
            dict[nums[i]] = i


nums = [2,7,9,11,13,15]
target = 24

print(twoSum(nums, target))
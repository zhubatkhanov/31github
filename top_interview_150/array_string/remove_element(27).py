

def removeElement(nums, val):
    slow = fast = 0
    while fast < len(nums):
        if nums[fast] == val:
            while nums[fast] == val:
                fast += 1
                if fast == len(nums):
                    return slow
        nums[slow] = nums[fast]
        slow, fast = slow + 1, fast + 1

    return slow


nums = [3]
print(removeElement(nums, 2))
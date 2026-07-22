class Solution:
    def removeElement(self, nums, val):
        i = 0  # pointer for position

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i
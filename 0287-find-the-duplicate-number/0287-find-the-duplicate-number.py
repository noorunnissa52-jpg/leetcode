class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        i=0
        while i<len(nums):
            correct_idx=nums[i]-1
            if nums[i]!=nums[correct_idx]:
                nums[i],nums[correct_idx]=nums[correct_idx],nums[i]
            else:
                if i!=correct_idx:
                    return nums[i]
                i+=1
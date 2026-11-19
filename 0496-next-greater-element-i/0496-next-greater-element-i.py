class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans=[]
        for x in nums1:
            num=False
            result=-1
            for y in nums2:
                if x==y:
                    num=True
                    continue
                if num and y>x:
                    result=y
                    break
            ans.append(result)
        return ans
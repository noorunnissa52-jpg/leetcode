class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        result=sorted(freq,key=freq.get,reverse=True)
        return result[:k]
        


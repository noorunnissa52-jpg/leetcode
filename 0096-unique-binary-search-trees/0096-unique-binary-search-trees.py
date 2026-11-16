class Solution:
    def numTrees(self, n: int) -> int:
        result=1
        for i in range(n):
            result=result*2*(2*i+1)//(i+2)
        return result
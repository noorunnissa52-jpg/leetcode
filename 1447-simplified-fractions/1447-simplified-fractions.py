class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        result = []

        for i in range(2, n+1):
            for j in range(1, i):
                if self.gcd(i, j) == 1:
                    result.append(str(j) + "/" + str(i))

        return result

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
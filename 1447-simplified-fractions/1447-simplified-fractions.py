class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        result = []

        for i in range(2, n + 1):
            for j in range(1, i):
                a = i
                b = j

                while b != 0:
                    temp = b
                    b = a % b
                    a = temp

                if a == 1:
                    result.append(str(j) + "/" + str(i))

        return result
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) != (divisor < 0) else 1

        a, b = abs(dividend), abs(divisor)
        result = 0

        while a >= b:
            temp = b
            multiple = 1

            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            a -= temp
            result += multiple

        result = result if sign == 1 else -result

        return min(max(result, -2**31), 2**31 - 1)
class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        total = 0

        while i < len(s) - 1:
            num1 = s[i]
            num2 = s[i+1]
            total = abs(ord(num1) - ord(num2)) + total
            i += 1

        return total
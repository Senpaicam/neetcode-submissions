class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < len(numbers) - 1:
            diff = target - numbers[l]

            while numbers[r] != diff and r > l:
                r -= 1
            if numbers[r] == diff and l < r:
                return [l+1, r+1]

            l += 1
            r = len(numbers) - 1
        return False
            
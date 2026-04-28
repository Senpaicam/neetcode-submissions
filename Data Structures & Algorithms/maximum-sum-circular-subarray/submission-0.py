class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gloMax, gloMin = nums[0], nums[0]
        curMax, curMin = 0,0
        total = 0

        for n in nums:
            curMax = max(n, curMax + n)
            curMin = min(n, curMin + n)
            total +=n
            gloMax = max(gloMax, curMax)
            gloMin = min(gloMin, curMin)

        return max(gloMax, total - gloMin) if gloMax > 1 else gloMax 
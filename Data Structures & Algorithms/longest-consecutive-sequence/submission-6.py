class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        maxCount = 1
        round = 0
        if len(nums) == 0:
            return 0
            
        while round < len(nums):
            if nums[round] + count in nums:
                count += 1
            else:
                maxCount = max(count, maxCount)
                count = 1
                round += 1
        return maxCount

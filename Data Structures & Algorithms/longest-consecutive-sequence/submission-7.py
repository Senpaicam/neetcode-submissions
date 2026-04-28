class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myDict = {}
        count = 1
        maxCount = 1
        round = 0
        if len(nums) == 0:
            return 0
        for i in nums:
            myDict[i] = i + 1
        while round < len(nums):
            if nums[round] + count in myDict:
                count += 1
            else:
                maxCount = max(count, maxCount)
                count = 1
                round += 1
        return maxCount

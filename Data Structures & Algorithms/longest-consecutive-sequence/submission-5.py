class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myDict = {}
        count = 1
        maxCount = 1

        if len(nums) == 0:
            return 0

        for i in nums:
            myDict[i] = i + 1
        
        for i in nums:
            flag = True
            while flag:
                if i + count in myDict:
                    count += 1
                else:
                        flag = False
            maxCount = max(count, maxCount)
            count = 1
        return maxCount

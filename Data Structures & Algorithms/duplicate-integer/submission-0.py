class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        prevMap = {}
        
        for key in range(len(nums)):
            if nums[key] in prevMap:
                return True
            prevMap[nums[key]] = nums[key]
        return False
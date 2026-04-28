class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {}

        for key,value in enumerate(nums):
            ans = target - nums[key]
            if ans in prevMap:
                return [prevMap[ans],key]
            prevMap[value] = key
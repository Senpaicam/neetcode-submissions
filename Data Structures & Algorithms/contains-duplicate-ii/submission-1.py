class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numMap = {}

        for key,value in enumerate(nums):
            if value in numMap:
                if abs(numMap[value] - key) <= k:
                    return True
            numMap[value] = key
        return False


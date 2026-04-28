class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for key, value in enumerate(nums):
            diff = target - value
            if diff in num_map:
                return [num_map[diff], key]
            num_map[value] = key
        
        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_Map = set()

        for i in nums:
            if i in num_Map:
                return True
            num_Map.add(i)
        return False
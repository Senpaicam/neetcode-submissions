class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_1 = []

        for i in range(len(nums)):
            if nums[i] in list_1:
                return True
            else:
                list_1.append(nums[i])

        return False

        

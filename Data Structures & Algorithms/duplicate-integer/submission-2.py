class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        numSet = set(nums)
        if len(numSet) != len(nums):
            return True
        else:
            return False
      

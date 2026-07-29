class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        l = 0
        for num in nums:
            numSet.add(num)
            if len(numSet) == l:
                return True
            l = len(numSet)
        return False

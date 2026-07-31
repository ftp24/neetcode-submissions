class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}
        for i, num in enumerate(nums):
            difference = target - nums[i]
            if difference in numSet:
                return [numSet[difference], i]
            numSet[nums[i]] = i
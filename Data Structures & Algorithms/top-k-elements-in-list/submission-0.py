class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyCount = defaultdict(int)
        for num in nums:
            frequencyCount[num]+=1
        sortedFrequencyCount = sorted(frequencyCount.items(), key=lambda item:item[1], reverse=True)
        result = []
        it = iter(sortedFrequencyCount)
        for i in range(k):
            result.append(next(it)[0])
        return result
        

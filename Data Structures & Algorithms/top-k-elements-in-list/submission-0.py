class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = dict()
        #nums = sorted(nums)
        for x in set(nums):
            result.update({x : nums.count(x)})
        result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        
        out = list(result.keys())
        return out[:k]


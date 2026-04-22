class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)
        for i in range(n):
            x = nums[i]
            diff = target - x

            if diff in seen:
                return [seen[diff], i]
            
            seen[x] = i
        
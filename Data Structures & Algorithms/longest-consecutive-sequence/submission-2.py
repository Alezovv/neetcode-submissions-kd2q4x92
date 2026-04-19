class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        numbers = {x: 0 for x in nums}

        for x in nums:
            if x - 1 in numbers:
                numbers[x] = 1
        result = 0
        for key, value in numbers.items():
            if value == 0:
                count = 1
                
                while key + count in numbers:
                    count += 1
                
                result = max(result, count)
         
        
        print(numbers)
        return result
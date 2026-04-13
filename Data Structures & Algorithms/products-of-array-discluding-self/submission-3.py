class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        count = 0
        isZero = [] 
        for i in range(len(nums)):
            if nums[i] == 0:
                isZero.append(i)
            else:
                count = 1
                mult *= nums[i]
        
        if count == 0:
            mult = 0

        result = []
        if len(isZero) > 0:
            for i in range(len(nums)):
                if i in isZero and len(isZero) == 1:
                    result.append(mult)
                else:
                    result.append(0)
        else:
            for i in range(len(nums)):
                result.append(mult // nums[i])
        
        return result
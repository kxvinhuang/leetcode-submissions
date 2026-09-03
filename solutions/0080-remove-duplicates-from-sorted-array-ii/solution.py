class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
            
        k = 0

        for num in nums:
            if k < 2 or num != nums[k - 2]:
                nums[k] = num
                k = k + 1
        
        return k

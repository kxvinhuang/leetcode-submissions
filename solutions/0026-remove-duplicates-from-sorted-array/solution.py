class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for curr_num in nums:
            if k == 0 or curr_num != nums[k - 1]:
                nums[k] = curr_num
                k = k + 1
        
        return k

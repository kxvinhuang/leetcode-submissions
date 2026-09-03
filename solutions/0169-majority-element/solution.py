class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        i = 0
        majority = 0

        for num in nums:
            if i == 0:
                majority = num
                i = 1
            else:
                if majority == num:
                    i += 1
                else:
                    i -= 1
        
        return majority

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # only works for sorted arrays
        # left, right = 0, len(nums) - 1

        # while left < right:
        #     sum = nums[left] + nums[right]

        #     if sum > target:
        #         right -= 1
        #     elif sum < target:
        #         left += 1
        #     elif sum == target:
        #         return [left, right]

        # O(n) time complexity
        seen = {}

        for index, num in enumerate(nums):
            need = target - num

            if need in seen:
                return [seen[need], index]
            
            seen[num] = index

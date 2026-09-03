class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # traverse from end to start, continue adding 1 to every digit unless it exits from a digit that isn't 9
        for i in range(len(digits)-1, -1, -1):
            # add one
            digits[i] += 1
            digits[i] %= 10

            # if the digit after the mod 10 isnt 0, then its done
            if digits[i] != 0:
                return digits
        
        # edge case where all the digits were 9 so have to add a 1 at the very start
        return [1] + digits

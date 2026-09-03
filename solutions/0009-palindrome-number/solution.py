class Solution:
    def isPalindrome(self, x: int) -> bool:
        # edge case where it cant be a palindrome if its a negative
        if x < 0:
            return False
        # excluding 0, if its positive and ends in a 0, it cant be a palindrome
        if x > 0 and x % 10 == 0:
            return False

        y = 0
        # split the given number in half where you take digits from the end of x and reveres it in y until y is equal or greater than x e.g for 1221/12321, x=12, y=12 or 123.
        while y < x:
            y = y * 10 + x % 10
            x //= 10
        
        # return if x is the same as either y or y with end digit removed for odd number of digits
        return x in (y, y // 10)

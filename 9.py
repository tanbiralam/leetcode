# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Quick rejection: negative numbers and numbers ending with 0 (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even-length: x == reversed_half
        # For odd-length: x == reversed_half // 10 (removes middle digit)
        return x == reversed_half or x == reversed_half // 10

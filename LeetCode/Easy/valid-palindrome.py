class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = ""
        for i in s.lower():
            if i in 'abcdefghijklmnopqrstuvwxyz1234567890': n += i


        return n == n[::-1]

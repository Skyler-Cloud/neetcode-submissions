class Solution:
    def isPalindrome(self, s: str) -> bool:
        # make the string correct
        new_s = ''
        for c in s:
            if c.isalnum():
                new_s += c
        # reverse & test
        new_s = (new_s).lower()
        return new_s == new_s[::-1]
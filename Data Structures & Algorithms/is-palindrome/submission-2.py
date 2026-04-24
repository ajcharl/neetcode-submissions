class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed = ""
        clean_s = ""

        for words in s:
            if words.isalnum():
                clean_s += words.lower()

        for i in range(len(clean_s) - 1, -1, -1):
            reversed += clean_s[i]

        if clean_s != reversed:
            return False
        return True
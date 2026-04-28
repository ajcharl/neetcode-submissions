class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        dictionary = {
        ")": "(", 
        "}": "{",  
        "]": "["  
        }

        for char in s:
            if char in dictionary:
                if not stack or stack[-1] != dictionary[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
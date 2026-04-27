class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # this is our "box" to store opening brackets

        pairs = {
        ")": "(",  # ) needs (
        "}": "{",  # } needs {
        "]": "["   # ] needs [
        }

        for char in s:  # go through each character in the string
            if char in pairs:  # if this is a closing bracket

            # check for two problems:
            # 1. stack is empty → nothing to match
            # 2. last opening bracket doesn't match this closing bracket
                if not stack or stack[-1] != pairs[char]:
                    return False  # invalid string

                stack.pop()  # match found → remove the last opening bracket

            else:
                # this is an opening bracket → store it
                    stack.append(char)

            # at the end:
            # if stack is empty → everything matched → True
            # if not empty → something didn't close → False
        return len(stack) == 0
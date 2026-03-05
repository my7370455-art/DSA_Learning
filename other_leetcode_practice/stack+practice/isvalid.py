class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == ']' and stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif char == ')' and stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif char == '}' and stack:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False
            
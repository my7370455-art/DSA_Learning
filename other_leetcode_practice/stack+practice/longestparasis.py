class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        index_stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                index_stack.append(i)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                    index_stack.pop()
                else:
                    stack.append(s[i])
                    index_stack.append(i)
        if not index_stack:
            return len(s)
        max_len = 0
        index_stack.append(len(s))
        prev = -1
        for i in index_stack:
            max_len = max(max_len, i - prev - 1)
            prev = i
        return max_len
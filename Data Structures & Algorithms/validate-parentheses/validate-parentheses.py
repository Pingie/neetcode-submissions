class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])

            elif s[i] == ')':
                if not stack:
                    return False

                peek = stack.pop()
                if(peek != '('):
                    return False

            elif s[i] == ']':
                if not stack:
                    return False
                peek = stack.pop()
                if(peek != '['):
                    return False
            
            else:
                if not stack:
                    return False
                peek = stack.pop()
                if(peek != '{'):
                    return False

        return len(stack) == 0

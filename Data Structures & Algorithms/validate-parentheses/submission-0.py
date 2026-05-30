class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                if stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False

        
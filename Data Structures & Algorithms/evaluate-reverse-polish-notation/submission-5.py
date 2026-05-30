class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                a, b = (stack.pop()), stack.pop()
                stack.append(int(a) + int(b))
            elif t == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(int(a) * int(b))
            elif t == '-':
                a, b = stack.pop(), stack.pop()
                print(a)
                print(b)
                stack.append(int(b) - int(a))
            elif t == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(t)
        return stack[-1]

        
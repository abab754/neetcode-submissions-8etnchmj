class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                i1 = stack.pop()
                i2 = stack.pop()
                stack.append(i1+i2)
            elif token == '-':
                i1 = stack.pop()
                i2 = stack.pop()
                stack.append(i2 - i1)
            elif token == '*':
                i1 = stack.pop()
                i2 = stack.pop()
                stack.append(i1*i2)
            elif token == '/':
                i1 = stack.pop()
                i2 = stack.pop()
                stack.append(int(i2/i1))
            else:
                stack.append(int(token))
            
        return stack.pop()

            
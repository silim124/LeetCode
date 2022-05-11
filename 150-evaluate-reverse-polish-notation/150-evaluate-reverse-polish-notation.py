class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                first, last = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(last + first)
                elif token == "-":
                    stack.append(last - first)
                elif token == "*":
                    stack.append(last * first)
                elif token == "/":
                    stack.append(int(last / first))
            else:
                stack.append(int(token))
        return stack.pop()
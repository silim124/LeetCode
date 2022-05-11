class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []

        for token in tokens:
            if token in "+-*/%":
                second, first = nums.pop(), nums.pop()
                if token == "+":
                    nums.append(first + second)
                elif token == "-":
                    nums.append(first - second)
                elif token == "*":
                    nums.append(first * second)
                else:
                    nums.append(int(float(first) / second))

            else:
                nums.append(int(token))

        return nums.pop()
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        result = 0
        stack = []
        for c in tokens:
            if c == '+' or c == '-' or c == '*' or c == '/':
                if len(stack) < 2:
                    return -1
                y = stack.pop()
                x = stack.pop()
                stack.append(str(self.get_calculate(x, y, c)))
            else:
                stack.append(c)
        return int(stack[0])
                
    def get_calculate(self, x, y, c):
        if c == '+':
            return int(x) + int(y)
        if c == '-':
            return int(x) - int(y)
        if c == '*':
            return int(x) * int(y)
        if c == '/':
            return int(x) / int(y)

        
s = Solution()
a = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print s.evalRPN(a)

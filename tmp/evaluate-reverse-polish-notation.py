
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }
        
        stack = []

        for t in tokens:
            if t in op:
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(op[t](n1, n2))
            else:
                stack.append(int(t))
        return stack[0]


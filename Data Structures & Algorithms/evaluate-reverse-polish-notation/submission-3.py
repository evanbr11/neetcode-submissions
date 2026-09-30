class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [0]
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(int(tokens[i]))
            else:
                if tokens[i] == "+":
                    res = stack.pop() + stack.pop()
                    stack.append(res)
                elif tokens[i] == "-":
                    temp = stack.pop()
                    res = stack.pop() - temp
                    stack.append(res)
                elif tokens[i] == "*":
                    res = stack.pop() * stack.pop()
                    stack.append(res)
                else:
                    denom = stack.pop()
                    res = int(stack.pop() / denom)
                    stack.append(res)
        return stack.pop()
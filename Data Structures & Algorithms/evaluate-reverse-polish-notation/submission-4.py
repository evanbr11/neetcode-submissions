class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [0]
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(int(tokens[i]))
            else:
                if tokens[i] == "+":
                    stack.append(stack.pop() + stack.pop())
                elif tokens[i] == "-":
                    temp = stack.pop()
                    stack.append(stack.pop() - temp)
                elif tokens[i] == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    denom = stack.pop()
                    stack.append(int(stack.pop() / denom))
        return stack.pop()
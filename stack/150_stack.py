class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #* Just use a stack
        operators = set(['+', '-', '*', '/'])
        #* Reverse the tokens
        tokens.reverse()
        stack = []

        def calculate(o1, o2, operator):
            match operator:
                case '+': return o1 + o2
                case '-': return o1 - o2
                case '*': return o1 * o2
                #! "The division between two integers always truncates toward zero."
                #^ result1 = int(o1 / o2) -> Result is -3
                #^ result2 = o1 // o2     -> Result is -4 (rounded towards negative infinity)
                case '/': return int(o1 / o2)

        while tokens:
            token = tokens.pop()
            if token in operators:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                result = calculate(operand1, operand2, token)
                stack.append(result)
            else:
                stack.append(int(token))

        # assert len(stack) == 1
        return stack[0]
        
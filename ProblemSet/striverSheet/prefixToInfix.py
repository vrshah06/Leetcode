def prefixToInfix(prefix):
    stack = []
    # Iterate over the prefix expression in reverse order
    for char in reversed(prefix):
        #if the character is an operand, push it to the stack
        if char.isalnum():
            stack.append(char)
        #if the character is an operator, pop two elements from the stack, combine them with the operator and push back to the stack
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            new_expr = f"({operand1}{char}{operand2})"
            stack.append(new_expr)
    # The final element in the stack is the infix expression
    return stack[-1]
if __name__ == "__main__":
    prefix = "*-A/BC-/AKL"
    infix = prefixToInfix(prefix)
    print(infix)  # Output: ((A-(B/C))*((A/K)-L))
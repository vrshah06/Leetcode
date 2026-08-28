def postfixToInfix(postfix):
    stack = []
    # Iterate over the postfix expression
    for char in postfix:
        # If the character is an operand, push it to the stack
        if char.isalnum():
            stack.append(char)
        # If the character is an operator, pop two elements from the stack, combine them with the operator and push back to the stack
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            new_expr = f"({operand1}{char}{operand2})"
            stack.append(new_expr)
    # The final element in the stack is the infix expression
    return stack[-1]
if __name__ == "__main__":
    postfix = "ABC/-AK/L-*"
    infix = postfixToInfix(postfix)
    print(infix)  # Output: ((A-(B/C))*((A/K)-L))
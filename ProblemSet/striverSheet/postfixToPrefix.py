def postfixToPrefix(postfix):
    stack = []
    # Iterate over the postfix expression
    for char in postfix:
        #if the character is an operand, push it to the stack
        if char.isalnum():
            stack.append(char)
        #if the character is an operator, pop two elements from the stack, combine them with the operator and push back to the stack
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            new_expr = f"({char}{operand1}{operand2})"
            stack.append(new_expr)
    # The final element in the stack is the prefix expression
    return stack[-1]
if __name__ == "__main__":
    postfix = "abc*+d-"
    prefix = postfixToPrefix(postfix)
    print(prefix)  # Output: -+a*bc d
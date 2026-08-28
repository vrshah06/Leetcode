def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return -1
def infixToPostfix(expression):
    stack = []
    result = ''
    for char in expression:
        #if the character is an operand, add it to output
        if char.isalnum():
            result += char
        #if the character is '(', push it to stack
        elif char == '(':
            stack.append(char)
        #if the character is ')', pop  from the stack until an '(' is encountered
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # pop '(' from the stack
        #if the character is an operator
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                result += stack.pop()
            stack.append(char) # push the current operator to stack
    #pop all the operators from the stack
    while stack:
        result += stack.pop()
    print(result)
if __name__ == "__main__":
    expression = "a+b*(c^d-e)^(f+g*h)-i"
    infixToPostfix(expression)
    


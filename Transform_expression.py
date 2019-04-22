top = -1
stack = []

for i in range(int(input())):
    infix = input()
    print(postfix)

def infix_to_postfix():
    p = 0
    for i in range(len(infix)):
        symbol = infix[i]
        if(not white_space(symbol)):
            if(symbol == '('):
                push(symbol)
            elif(symbol == ')'):
                while((next = pop())!='('):
                    postfix[p+1] = next
            elif(symbol == '+' or symbol == '-' or symbol == '*' or symbol == '/' or symbol == '%' or symbol == '^'):
                while((not isEmpty()) and priority(stack[top]) >= priority(symbol)):
                    postfix[p+1] = pop()
                push(symbol)
            else:
                postfix[p+1] = symbol
    while(not isEmpty()):
        postfix[p+1] = pop()
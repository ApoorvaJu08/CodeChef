t = int(input())

for i in range(t):
    n = input()
    result = ''
    operator = []
    
    for j in n:
        if j.isalpha():
            result += j 
        elif j == ')':
            result += operator.pop()
        elif j != '(':
            operator.append(j) 
        
            
    print(result)


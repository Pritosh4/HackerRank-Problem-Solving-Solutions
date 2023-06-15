# Enter your code here. Read input from STDIN. Print output to STDOUT
q = int(input())
stack = ['']
for i in range(q):
    op = input()
    if op[0] != '4':
        op, val = op.split()
    if op == '1':
        stack.append(stack[-1] + val)
    elif op =='2':
        stack.append(stack[-1][:-int(val)])
    elif op == '3':
        print(stack[-1][int(val) - 1])
    elif op == '4':
        stack.pop()

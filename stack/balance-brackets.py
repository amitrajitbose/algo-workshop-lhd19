opp = {
    '}':'{',
    ']':'[',
    ')':'('
}
for _ in range(int(input())):
    exp = list(input())
    stack = []
    if len(exp) < 2:
        print('not balanced')
        continue
    stack.append(exp[0])
    for i in exp[1:]:
        if i in opp and len(stack) and stack[-1] == opp[i]:
            stack.pop(-1)
        else:
            stack.append(i)
    if len(stack) == 0:
        print('balanced')
    else:
        print('not balanced')


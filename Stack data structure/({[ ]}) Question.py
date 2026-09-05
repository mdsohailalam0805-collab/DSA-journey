s = "({[]})"

stack = []

pairs = {
    
    ')' : '(',
    '}' : '{',
    ']' : '[',
    
}
valid = True

for bracket in s :
    
    # opening bracket
    if bracket in "({[":
        stack.append(bracket)
        
        # closing bracket
    else:
        # stack empty
        if not stack:
            valid = False
            break
        
        # if top bracket does'nt matching
        
        if stack[-1] != pairs[bracket]:
            valid = False
            break
        
        # matching bracket remove
        stack.pop()

if valid and len(stack) == 0:
    print("Valid Pranthesis")
    
else:
    print("Invalid Paranthesis")
        
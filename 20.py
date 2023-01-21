def isValid(s):
    if s[0] in ')}]':
        return False
    stack = []
    closeToOpen = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    for c in s:
        if c in closeToOpen: # if c is a key (closing parentheses)
            # if stack is not empty and the last element is a key (closing parentheses)
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop() # remove the last element
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False





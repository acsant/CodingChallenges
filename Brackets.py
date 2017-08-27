import sys

stack = []
lookup = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

def isValid(bracketString):
    for brack in bracketString:
        if len(stack) == 0:
            stack.append(brack)
        else:
            if brack in lookup and stack[-1] == lookup[brack]:
                stack.pop()
            else:
                if brack in lookup.keys() or brack in lookup.values():
                    stack.append(brack)

    return len(stack) == 0

arg = sys.argv[1]
print(isValid(arg))

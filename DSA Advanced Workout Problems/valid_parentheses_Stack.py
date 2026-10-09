s = "({[]})"

stack = []

pairs = {
    ')': '(',
    '}': '{',
    ']': '['
}

valid = True

for char in s:

    if char in "({[":
        stack.append(char)

    else:
        if len(stack) == 0 or stack[-1] != pairs[char]:
            valid = False
            break

        stack.pop()

if len(stack) != 0:
    valid = False

print(valid)
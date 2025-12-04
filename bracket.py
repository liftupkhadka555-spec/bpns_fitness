def is_brackets_balanced(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


print(is_brackets_balanced("()"))
print(is_brackets_balanced("([])"))
print(is_brackets_balanced("(abc[123]{})"))
print(is_brackets_balanced("(]"))
print(is_brackets_balanced("([)]"))
print(is_brackets_balanced("((("))
print(is_brackets_balanced(""))
print(is_brackets_balanced("no brackets here"))

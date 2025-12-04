def is_strictly_increasing(steps: list[int]) -> bool:
    if len(steps) == 0 or len(steps) == 1:
        return True

    for i in range(len(steps) - 1):
        if steps[i + 1] <= steps[i]:
            return False

    return True
print(is_strictly_increasing([1000, 2000, 3000, 4000]))
print(is_strictly_increasing([3000, 3000, 4000]))
print(is_strictly_increasing([5000, 7000, 6000]))
print(is_strictly_increasing([]))
print(is_strictly_increasing([4500]))
print(is_strictly_increasing([100, 200, 500, 1000, 2000]))
print(is_strictly_increasing([8000, 8000]))
print(is_strictly_increasing([8000, 9000]))

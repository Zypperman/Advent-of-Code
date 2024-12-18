arr = [
    ["M", "M", "M", "X"],
    ["M", "M", "M", "X"],
    ["M", "S", "A", "x"],
    ["A", "M", "X", "X"],
    ["M", "S", "A", "M"],
    ["M", "S", "A", "M"],
    ["M", "S", "A", "M"],
    ["M", "S", "A", "M"],
    ["M", "S", "A", "M"],
    ["M", "S", "A", "M"],
]

# transpose
# arr = [[arr[i][j] for i in range(len(arr))] for j in range(len(arr[0]))]

for i in arr:
    print(i)

print(" ", " ".join([str(i) for i in range(len(arr[0]))]), len(arr[0]))
for i in range(len(arr)):
    print(i, " ".join([str(j) for j in arr[i]]))
print(len(arr))


test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

alt = [
    [row[len(test[0]) - i - 1] for row in test]
    for i in range(max(len(r) for r in test))
]

for i in alt:
    print(i)
new = []

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
# matrix can be printed normally

for row in matrix:
    for item in row:
        print(item)
        # or in a nested for loop
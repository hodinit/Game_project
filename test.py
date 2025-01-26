# ...existing code...

def check_win(matrix):
    n = len(matrix)
    win_or_lose = True

    # Check rows
    for row in matrix:
        if len(set(row)) != 1:
            win_or_lose = False
            break

    # Check columns
    if win_or_lose:
        for col in range(n):
            column = [matrix[row][col] for row in range(n)]
            if len(set(column)) != 1:
                win_or_lose = False
                break

    # Check diagonals
    if win_or_lose:
        if len(set(matrix[i][i] for i in range(n))) != 1:
            win_or_lose = False

    if win_or_lose:
        if len(set(matrix[i][n - 1 - i] for i in range(n))) != 1:
            win_or_lose = False

    return win_or_lose

# Example usage
n = int(input("Enter the size of the matrix: "))
x = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input("Enter a number: ")))
    x.append(row)

if check_win(x):
    print("Win")
else:
    print("Lose")

for row in x:
    print(row)
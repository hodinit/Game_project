x = []
n = int(input("Enter the number of rows x columns: "))
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input("Enter a number: ")))
    x.append(row)

win_or_lose = True

for i in range(n):
    for j in range(n):
        if x[i][i] != x[j][j]:
            win_or_lose = False
for i in range(n):
    for j in range(i+1, n):
        if x[0][i] != x[0][j]:
            win_or_lose = False

for i in range(n):
    for j in range(n):
        if x[i][0] != x[j][0]:
            win_or_lose = False

for row in x:
    print(row)

print(win_or_lose)


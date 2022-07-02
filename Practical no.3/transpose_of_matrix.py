
# Python program to find the transpose of a matrix...!!

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print("Matrix a:\n", a[0], "\n", a[1], "\n", a[2])


b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print("Transpose of matrix a:")

for i in range(len(a)):
    for j in range(len(a)):
        b[i][j] = a[j][i]
    print(b[i])

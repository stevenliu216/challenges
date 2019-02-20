# List Comprehensions

Let's learn about list comprehensions! You are given three integers X, Y and Z
representing the dimensions of a cuboid along with an integer N. You have to
print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of
i + j + k is not equal to N. Here,

### Input Format

Four integers X, Y, Z, and N each on four separate lines, respectively.

### Constraints

Print the list in lexicographic increasing order.

### Function prototype:
    def list_comp(x, y, z, n):
 

    if __name__ == '__main__':
        x = int(input())
        y = int(input())
        z = int(input())
        n = int(input())
        list_comp(x, y, z, n)

### Sample Input

    1
    1
    1
    2

### Sample Output

    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
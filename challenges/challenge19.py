def list_comp(x, y, z, n):
    pos_coords = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
    print(pos_coords)
    return pos_coords


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list_comp(x, y, z, n)

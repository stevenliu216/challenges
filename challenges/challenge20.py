def print_rangoli(size):
    """Prints a rangoli of variable length size.

    Starts with an a in the middle, and then goes up a letter for each column
    and row offset off the middle.
    """

    rangoli = ""
    width = 4 * size - 3
    for row in range(1, size * 2):
        line = ""
        for column in range(1, size * 2):
            if row == size and column == size:
                line = line + "a-"
            else:
                row_offset = abs(row - size)
                col_offset = abs(column - size)
                total_offset = row_offset + col_offset
                if total_offset < size:
                    line = line + chr(ord("a") + total_offset)

                # Only add a dash between characters if not last column
                if column != size * 2 - 1:
                    line = line + "-"
        rangoli = rangoli + line.center(width, "-") + "\n"
    return rangoli


if __name__ == '__main__':
    n = int(input())
    print(print_rangoli(n))

def replace_spaces_dashes(line):
    return "-".join(line.split())


def last_five_lowercase(line):
    return line[-5:].lower()


def backwards_skipped(line):
    return line[::-2]


if __name__ == '__main__':
    line = input("Enter a string: ")
    print(replace_spaces_dashes(line))
    print(last_five_lowercase(line))
    print(backwards_skipped(line))

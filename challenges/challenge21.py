def replace_spaces_dashes(line):
    no_spaces = "-".join(line.split())
    return no_spaces


def last_five_lowercase(line):
    five_lowercase = line[-5:].lower()
    return five_lowercase


def backwards_skipped(line):
    back_skip = line[::-2]
    return back_skip


if __name__ == '__main__':
    line = input("Enter a string: ")
    print(replace_spaces_dashes(line))
    print(last_five_lowercase(line))
    print(backwards_skipped(line))

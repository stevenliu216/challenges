def swap_case(string):
    swapped_chars = []
    for char in string:
        if char.isupper():
            swapped_chars.append(char.lower())
        else:
            swapped_chars.append(char.upper())
    return "".join(swapped_chars)


if __name__ == "__main__":
    s = input("Enter String: ")
    result = swap_case(s)
    print("Swapped String:", result)

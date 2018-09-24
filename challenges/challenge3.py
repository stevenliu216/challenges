def is_unique(string):
    unique_dict = {}
    for char in string:
        if char in unique_dict:
            return False
        unique_dict[char] = True
    return True

print(is_unique("alabama"))
print(is_unique("Ford"))

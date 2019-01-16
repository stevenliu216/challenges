import numpy as np


def shape_reshape(array: str) -> np.array:
    list_array = [int(num) for num in array.split()]
    np_array = np.array(list_array)
    np_array.shape = (3, 3)
    return np_array


if __name__ == "__main__":
    array = input("Enter the array you want to shape:")
    print(shape_reshape(array))

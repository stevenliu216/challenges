from challenges.challenge13 import shape_reshape
import numpy as np


def test_shape_reshape():
    reshaped_array = shape_reshape("1 2 3 4 5 6 7 8 9")
    np.testing.assert_array_equal(
        reshaped_array, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    )

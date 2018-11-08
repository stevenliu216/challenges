def max_area(height):
    """Calculates the max area of a container.

    Start at opposite ends of the list, the only way for the area to increase
    is if the lower of the two heights is increased.

    Args:
        height (list): An array of the line heights.

    Returns:
        int: The max area of the container.

    """
    left = 0  # Left pointer
    right = len(height) - 1  # Right pointer
    maxarea = 0
    while left < right:
        height_left = height[left]
        height_right = height[right]
        container_height = min(height_left, height_right)
        current_area = area(right - left, container_height)
        if current_area > maxarea:
            maxarea = current_area
        if height_left < height_right:
            left += 1
        else:
            right -= 1
    return maxarea


def area(width, height):
    return width * height

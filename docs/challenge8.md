# Challenge 8
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the
most water.

Note: You may not slant the container and n is at least 2.
![alt text](challenge8.jpg "Container with the Most Water")
### Function prototype:
    def max_area(self, height):
 
height (list): an array of the line heights
### Return values
Max Area (int): The max area of the container
 
### Example
##### Sample Input
    [1,8,6,2,5,4,8,3,7]
 
##### Sample Output
    49
 
### Explanation
49 is the total area of the water container between the red lines.
If you start with heights at opposite ends of the list, the only way for the area to
increase is if the lower of the two heights is increased.

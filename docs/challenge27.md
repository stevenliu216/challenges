# Challenge 27

### Battery Swap 
You are driving a BEV, and your goal is to reach the finish line. Given an array
of non-negative integers, you are initially positioned at the first index of the
array. The number at that position represents your starting battery range.

Each value in the array represents a battery laying in a road. You can
either swap the battery with yours or keep going, but each move to the next
element in the array uses one unit of range from your battery.

Determine if you are able to reach the last index.

### Function Prototype
```python
from typing import List


def reach_the_finish(batteries: List[int]) -> bool:
    pass


if __name__ == "__main__":
    road_length = int(input("Please enter length of road: "))
    battery_locations = [
        int(input(f"Please enter battery {pos + 1}: ")) for pos in range(road_length)
    ]
    print(reach_the_finish(battery_locations))
```

### Example 1

#### Input
    [2,3,1,1,4]
    
#### Output
    True
#### Explanation
Drive 1 step from index 0 to 1, swap your battery, then 3 steps to the last index.

### Example 2

#### Input
    [3,2,1,0,4]
#### Output
    False
#### Explanation

You will always arrive at index 3 and then run out of charge. There is no
battery available at this index (value of zero), which makes it impossible to
reach the last index.


# Challenge 30

Given a score sheet for competition, you are required to find the runner-up
score.

Note: This isn't golf, the highest score wins.

### Input Format

The first line contains n. The second line contains an array A[] of n integers
each separated by a space.

### Output Format

Print the runner-up score.

### Function Prototype

```
def runner_up_score(scores):
    pass


if __name__ == '__main__':
    num = int(input(f"Enter the number of scores: "))
    arr = [int(input(f"Enter score {score + 1}: ")) for score in range(num)]
    print(runner_up_score(arr))
```

### Example

#### Input
    5
    2 3 6 6 5

#### Output
    5

#### Explanation

Given list is `[2, 3, 6, 6, 5]`. The maximum score is `6`. The second highest
score is `5`. 

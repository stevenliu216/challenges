# Challenge 28

### Palindrome Number
Determine whether an integer is a palindrome. A palindrome is a word, number, or
other sequence of characters which reads the same backward as forward.

### Function Prototype
```python
def is_palindrome(checked_int: int) -> bool:
    pass


if __name__ == "__main__":
    checked_int = int(input("Please enter the integer: "))
    print(is_palindrome(checked_int))
```

### Example 1

#### Input
    121
    
#### Output
    True
    
### Example 2

#### Input
    -121
#### Output
    False
#### Explanation
From left to right, it reads -121. From right to left, it becomes
121-. Therefore it is not a palindrome.

### Example 3
#### Input
    10
#### Output
    False
#### Explanation
Reads 01 from right to left. Therefore it is not a palindrome.

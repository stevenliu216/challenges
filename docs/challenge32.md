# Challenge 32
### Happiness Factor

There is an array of `n` integers. There are also 2 disjoint sets, `A` and `B`,
each containing `m` integers. You like all the integers in set `A` and dislike all
the integers in set `B`. Your initial happiness is 0. For each integer in `A`
you add 1 to your happiness. For each integer in `B` you subtract 1 from your
happiness. Otherwise, your happiness does not change. Output your final
happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array
might contain duplicate elements.

### Input Format

The first line contains integers n and m separated by a space. 
The second line contains n integers, the elements of the array. 
The third and fourth lines contain m integers, A and B, respectively.

### Output Format

Output a single integer, your total happiness.

### Function Prototype

```
def calc_happiness(valid_elements, pos_adder, neg_adder):
    pass
    
    
if __name__ == "__main__":
    m, n = input("Enter the space-separated values of m and n: ").split()
    valid_elements = [int(num) for num in input("Enter the valid elements of the array: ").split()]
    a = [int(num) for num in input(f"Enter the array A: ").split()]
    b = [int(num) for num in input("Enter the array B: ").split()]
    print(f"The happiness is {calc_happiness(valid_elements, a, b)}")
```

### Sample Input

```
3 2
1 5 3
3 1
5 7
```

### Sample Output

    1

### Explanation

You gain 1 unit of happiness for elements 3 and 1 in set A. You lose 1 unit for
5 in set B. The element 7 in set B does not exist in the array so it is not
included in the calculation.

The total happiness is 2 - 1 = 1.

# Challenge 25

## Buy and Sell Stock

Say you have an array for which the i<sup>th</sup> element is the price of a
given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one
and sell one share of the stock), design an algorithm to find the maximum
profit.

Note that you cannot sell a stock before you buy one.

## Function Prototype
    from typing import List
    
    
    def max_profit(prices: List[int]) -> int:
        pass
    
    
    if __name__ == "__main__":
        num = int(input("Enter number of stock prices: "))
        prices = [int(input(f"Enter stock price {price + 1}: ")) for price in range(num)]
        print("The max profit is", max_profit(prices))
    
## Example 1
### Input
    [7, 1, 5, 3, 6, 4]
### Output
    5
### Explanation
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

## Example 2
### Input
    [7, 6, 4, 3, 1]
### Output
    0
### Explanation
In this case, no transaction is done because max profit is 0.

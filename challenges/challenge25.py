from typing import List


def max_profit(prices: List[int]) -> int:
    max_profit = 0
    min_price = prices[0]
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
    return max_profit


if __name__ == "__main__":
    num = int(input("Enter number of stock prices: "))
    prices = [int(input(f"Enter stock price {price + 1}: ")) for price in range(num)]
    print("The max profit is", max_profit(prices))

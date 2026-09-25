# 2. 📈 Stock Market Analyzer

# Given:

# prices = np.array([
#     100, 105, 102, 110, 115, 112, 120
# ])

# Calculate:

# Daily price change
# Percentage change
# Highest price
# Lowest price
# Average price
# Best-performing day
# Days where price increased
# Simple moving average

import numpy as np

days = ["mon","tues","wed","thurs","fri","sat","sun"]
prices = np.array([100,105,300,200,450,7000,120])
daily_price_change = np.diff(prices)
print(daily_price_change)

percentage_change = (np.diff(prices) / prices[:-1]) * 100
print(percentage_change)

highest_price = np.max(prices)
print("highest price =", highest_price)

lowest_price = np.min(prices)
print("lowest price", lowest_price)
avg = np.mean(prices)
print("avg is",avg)
best = np.argmax(daily_price_change)
print("best day = ", best)

inc_price = daily_price_change>0
print(inc_price)

moving_average = np.convolve(prices, np.ones(3)/3, mode='valid')
print("moving_average", moving_average)






























# #Simple Sales Analyzer ⭐
# 2D arrays, axis, aggregation

import numpy as np
days = ["mon", "tues","wed","thur","fri"]
arr = np.array([[1000,5500,2000,9000,3000],
                [5550,7000,9000,1200, 900],
                [4000,8000,7500,1000, 800],
                [2020,4500,800,9000,3000],
                [1200,2000,3000,400,6000]])

total_sales = np.sum(arr, axis = 1)
print("total sales",total_sales)

for day, sales in zip(days, total_sales):
    print(day, sales)

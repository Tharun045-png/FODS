import numpy as np

# Each row represents a product; columns contain prices for its sales
sales_data = np.array([
    [100.0, 120.0, 110.0],
    [80.0,  90.0,  85.0],
    [150.0, 140.0, 160.0]
])

# Calculate the average price across all sales values
average_price = np.mean(sales_data)

print(f"Average price of all products sold: {average_price:.2f}")

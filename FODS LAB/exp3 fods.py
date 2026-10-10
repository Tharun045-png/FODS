import numpy as np

# Columns: bedrooms, square footage, sale price
# Example data loaded from a CSV file with a header row
house_data = np.genfromtxt(
    "house_data.csv",
    delimiter=",",
    skip_header=1
)

# Select houses with more than four bedrooms
selected_houses = house_data[house_data[:, 0] > 4]

if selected_houses.size > 0:
    average_sale_price = np.mean(selected_houses[:, 2])
    print(f"Average sale price for houses with more than 4 bedrooms: "
          f"{average_sale_price:.2f}")
else:
    print("No houses with more than four bedrooms were found.")

import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

###### Sales Data for Locations by Day ######
# Define parameters
num_days = 90  # Number of days to generate data for
locations = ['TimesSquare', 'CentralPark', 'UpperWest']
items = ['Burger', 'Fries', 'Soda', 'Water', 'Salad']

# Generate date range
date_range = pd.date_range(start=fake.date_this_year(), periods=num_days, freq='D')

# Generate random data
data = []
for date in date_range:
    for location in locations:
        for item in items:
            quantity_sold = np.random.randint(20, 150)  # Random quantity sold between 20 and 150
            data.append([date, location, item, quantity_sold])

# Create DataFrame
df = pd.DataFrame(data, columns=['Date', 'Location', 'Item', 'Quantity Sold'])

# Export to CSV
df.to_csv('FoodTruckSalesData.csv', index=False)

# Display the first few rows
print(df.head())
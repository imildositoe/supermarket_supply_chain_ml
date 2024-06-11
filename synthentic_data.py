import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker for generating random data
fake = Faker()

# Define the initial data
data = [
    {
        "Store ID": 1, "Store Name": "Store A", "Country": "USA", "Address": "123 Main St, Anytown",
        "Region": "East Coast",
        "Product ID": 101, "Product Name": "Apples", "Category": "Fresh Produce", "Supplier ID": 201, "Unit Cost": 1.50,
        "Shelf Life": 5, "Transaction ID": 1001, "Date": "2024-04-01", "Quantity Sold": 100, "Sales Amount": 150.00,
        "Forecasted Demand": 110, "Opening Inventory": 50, "Closing Inventory": 40, "Days of Inventory": 5,
        "Supplier Name": "Supplier X", "On-time Delivery Rate": 90, "Quality Rating": 4.5, "Order Accuracy Rate": 95,
        "Temperature": 72, "Precipitation": 0.2, "Weather Condition": "Sunny", "Advertisement Type": "Digital",
        "Advertisement Cost": 100, "Click-through Rate": 2.5
    },
    {
        "Store ID": 1, "Store Name": "Store A", "Country": "USA", "Address": "123 Main St, Anytown",
        "Region": "East Coast",
        "Product ID": 102, "Product Name": "Bananas", "Category": "Fresh Produce", "Supplier ID": 202,
        "Unit Cost": 0.75,
        "Shelf Life": 3, "Transaction ID": 1002, "Date": "2024-04-01", "Quantity Sold": 200, "Sales Amount": 150.00,
        "Forecasted Demand": 180, "Opening Inventory": 100, "Closing Inventory": 90, "Days of Inventory": 4,
        "Supplier Name": "Supplier Y", "On-time Delivery Rate": 85, "Quality Rating": 4.2, "Order Accuracy Rate": 92,
        "Temperature": 72, "Precipitation": 0.2, "Weather Condition": "Sunny", "Advertisement Type": "Digital",
        "Advertisement Cost": 100, "Click-through Rate": 2.5
    },
    {
        "Store ID": 2, "Store Name": "Store B", "Country": "UK", "Address": "456 High St, Anycity", "Region": "London",
        "Product ID": 103, "Product Name": "Milk", "Category": "Dairy", "Supplier ID": 203, "Unit Cost": 2.00,
        "Shelf Life": 7, "Transaction ID": 1003, "Date": "2024-04-02", "Quantity Sold": 50, "Sales Amount": 100.00,
        "Forecasted Demand": 60, "Opening Inventory": 30, "Closing Inventory": 20, "Days of Inventory": 6,
        "Supplier Name": "Supplier Z", "On-time Delivery Rate": 95, "Quality Rating": 4.8, "Order Accuracy Rate": 97,
        "Temperature": 65, "Precipitation": 0.1, "Weather Condition": "Cloudy", "Advertisement Type": "TV",
        "Advertisement Cost": 150, "Click-through Rate": 3.0
    },
    {
        "Store ID": 2, "Store Name": "Store B", "Country": "UK", "Address": "456 High St, Anycity", "Region": "London",
        "Product ID": 104, "Product Name": "Chicken", "Category": "Meat", "Supplier ID": 204, "Unit Cost": 5.00,
        "Shelf Life": 4, "Transaction ID": 1004, "Date": "2024-04-02", "Quantity Sold": 20, "Sales Amount": 80.00,
        "Forecasted Demand": 25, "Opening Inventory": 10, "Closing Inventory": 15, "Days of Inventory": 3,
        "Supplier Name": "Supplier W", "On-time Delivery Rate": 88, "Quality Rating": 4.4, "Order Accuracy Rate": 93,
        "Temperature": 65, "Precipitation": 0.1, "Weather Condition": "Cloudy", "Advertisement Type": "TV",
        "Advertisement Cost": 150, "Click-through Rate": 3.0
    },
]

# Create a DataFrame
df = pd.DataFrame(data)


# Define function to generate synthetic data
def generate_synthetic_data(num_rows):
    synthetic_data = []
    for _ in range(num_rows):
        store_id = random.randint(1, 10)
        store_name = f"Store {chr(64 + store_id)}"
        country = fake.country()
        address = fake.address()
        region = fake.state()
        product_id = random.randint(101, 110)
        product_name = fake.word()
        category = random.choice(
            ["Fresh Produce", "Dairy", "Meat", "Frozen Food", "Drinks", "Household Items", "Bakery"])
        supplier_id = random.randint(201, 210)
        unit_cost = round(random.uniform(0.5, 5.0), 2)
        shelf_life = random.randint(2, 10)
        transaction_id = fake.unique.random_number(digits=4)
        date = fake.date_between(start_date='2024-04-01', end_date='2024-04-30')
        quantity_sold = random.randint(10, 200)
        sales_amount = round(quantity_sold * unit_cost, 2)
        forecasted_demand = quantity_sold + random.randint(-10, 20)
        opening_inventory = random.randint(10, 100)
        closing_inventory = opening_inventory - quantity_sold if opening_inventory > quantity_sold else random.randint(
            0, 50)
        days_of_inventory = random.randint(2, 7)
        supplier_name = fake.company()
        on_time_delivery_rate = round(random.uniform(80, 100), 1)
        quality_rating = round(random.uniform(3.5, 5.0), 1)
        order_accuracy_rate = round(random.uniform(85, 100), 1)
        temperature = random.randint(50, 100)
        precipitation = round(random.uniform(0.0, 1.0), 2)
        weather_condition = random.choice(["Sunny", "Cloudy", "Rainy"])
        advertisement_type = random.choice(["Digital", "TV", "Print"])
        advertisement_cost = random.randint(50, 200)
        click_through_rate = round(random.uniform(1.0, 5.0), 1)

        synthetic_data.append({
            "Store ID": store_id, "Store Name": store_name, "Country": country, "Address": address, "Region": region,
            "Product ID": product_id, "Product Name": product_name, "Category": category, "Supplier ID": supplier_id,
            "Unit Cost": unit_cost, "Shelf Life": shelf_life, "Transaction ID": transaction_id, "Date": date,
            "Quantity Sold": quantity_sold, "Sales Amount": sales_amount, "Forecasted Demand": forecasted_demand,
            "Opening Inventory": opening_inventory, "Closing Inventory": closing_inventory,
            "Days of Inventory": days_of_inventory,
            "Supplier Name": supplier_name, "On-time Delivery Rate": on_time_delivery_rate,
            "Quality Rating": quality_rating,
            "Order Accuracy Rate": order_accuracy_rate, "Temperature": temperature, "Precipitation": precipitation,
            "Weather Condition": weather_condition, "Advertisement Type": advertisement_type,
            "Advertisement Cost": advertisement_cost,
            "Click-through Rate": click_through_rate
        })
    return synthetic_data


# Generate 1000 additional rows
additional_data = generate_synthetic_data(1000)

# Convert to DataFrame and append to existing data
additional_df = pd.DataFrame(additional_data)
df = df.append(additional_df, ignore_index=True)

# Display the first few rows of the DataFrame
print(df.head())

import datetime

import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker for generating random data
fake = Faker()
data = []

# Create a DataFrame
df = pd.DataFrame(data)


# Define function to generate synthetic data
def generate_synthetic_data(num_rows):
    synthetic_data = []
    for i in range(num_rows):
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
        date = fake.date_between(start_date=datetime.date(2018, 1, 1))
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
            "ID": i + 1, "Store ID": store_id, "Store Name": store_name, "Country": country, "Address": address,
            "Region": region, "Product ID": product_id, "Product Name": product_name, "Category": category,
            "Supplier ID": supplier_id, "Unit Cost": unit_cost, "Shelf Life": shelf_life,
            "Transaction ID": transaction_id, "Date": date, "Quantity Sold": quantity_sold,
            "Sales Amount": sales_amount, "Forecasted Demand": forecasted_demand,
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
additional_data = generate_synthetic_data(5000)

# Convert to DataFrame and append to existing data
additional_df = pd.DataFrame(additional_data)
df = pd.concat([df, additional_df], ignore_index=True)

# Display the first few rows of the DataFrame
print(df.head())

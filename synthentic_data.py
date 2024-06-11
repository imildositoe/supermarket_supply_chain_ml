import datetime

import faker_food
import pandas as pd
from faker import Faker
import random
from faker_food import FoodProvider

# Initialization of Faker object to generate random data fake data
# Initialization of the Dataframe object to store the data
faker = Faker()
df = pd.DataFrame()
fake_food = FoodProvider_


# This function is responsible in generating the synthetic data
# Parameter num_rows in the number of rows needed to be generated
def generate_synthetic_data(num_rows):
    synthetic_data = []
    for i in range(num_rows):
        store_id = random.randint(1, 100) # change here to have 100 unique stores
        store_name = f"Store {chr(64 + store_id)}"
        country = faker.country() # this must have maximum 10 countries
        address = faker.address()
        region = faker.state()
        product_id = random.randint(101, 110)
        product_name = random.choice([
            random.choice(["Apple", "Banana", "Carrot", "Lettuce", "Tomato", "Potato", "Orange", "Strawberry", "Grape",
                           "Peppers"]),
            random.choice(["Roses", "Tulips", "Daisies", "Lilies", "Sunflowers", "Orchids", "Carnations",
                           "Chrysanthemums", "Peonies", "Hydrangeas"]),
            random.choice(["Milk", "Cheese", "Yogurt", "Butter", "Cream", "Ice Cream", "Sour Cream", "Cottage Cheese",
                           "Eggs", "Buttermilk"]),
            random.choice(["Chicken", "Beef", "Pork", "Turkey", "Lamb", "Sausage", "Bacon", "Ham", "Ground Beef",
                           "Steak"]),
            random.choice(["Frozen Vegetables", "Frozen Fruits", "Frozen Pizza", "Frozen Dinners", "Ice Cream",
                           "Frozen Fish", "Frozen Chicken", "Frozen Beef", "Frozen Sausages", "Frozen Desserts"]),
            random.choice(["Soda", "Juice", "Water", "Milk", "Coffee", "Tea", "Wine", "Beer", "Energy Drinks",
                           "Smoothies"]),
            random.choice(["Paper Towels", "Toilet Paper", "Laundry Detergent", "Dish Soap", "Cleaning Supplies",
                           "Trash Bags", "Light Bulbs", "Batteries", "Air Fresheners", "Disinfectant Wipes"]),
            random.choice(["Bread", "Bagels", "Muffins", "Cakes", "Cookies", "Croissants", "Donuts", "Pies", "Buns",
                           "Pastries"])
        ])
        category = random.choice(
            ["Fresh Produce", "Flowers", "Dairy", "Meat", "Frozen Food", "Drinks", "Household Items", "Bakery"])
        supplier_id = random.randint(201, 210)
        unit_cost = round(random.uniform(0.5, 5.0), 2)
        shelf_life = random.randint(2, 10)
        transaction_id = faker.unique.random_number(digits=7)
        date = faker.date_between(start_date=datetime.date(2018, 1, 1))
        quantity_sold = random.randint(10, 200)
        sales_amount = round(quantity_sold * unit_cost, 2)
        forecasted_demand = quantity_sold + random.randint(-10, 20)
        opening_inventory = random.randint(10, 100)
        closing_inventory = opening_inventory - quantity_sold if opening_inventory > quantity_sold else random.randint(
            0, 50)
        days_of_inventory = random.randint(2, 7)
        supplier_name = faker.company()
        on_time_delivery_rate = round(random.uniform(80, 100), 1)
        quality_rating = round(random.uniform(3.5, 5.0), 1)
        order_accuracy_rate = round(random.uniform(85, 100), 1)
        temperature = random.randint(50, 100)
        precipitation = round(random.uniform(0.0, 1.0), 2)
        weather_condition = random.choice(["Sunny", "Cloudy", "Rainy"])
        advertisement_type = random.choice(["Digital", "TV", "Print"])
        advertisement_cost = random.randint(50, 200)
        click_through_rate = round(random.uniform(1.0, 5.0), 1)

        # Appending each fake created row into the synthetic_data array
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


# Calling the function to generate the rows specifying the quantity needed
# Appending the generated rows into the existing dataframe
additional_data = generate_synthetic_data(10000)
additional_df = pd.DataFrame(additional_data)
df = pd.concat([df, additional_df], ignore_index=True)

# Create and add all created rows in a csv file and store in the specified relative path
df.to_csv('../../Dashboard/master_database.csv', sep=';', index=False)

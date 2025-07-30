# receipt.py
# Enhancement: Adds a "Return by" date 30 days in the future at 9:00 PM

import csv
import datetime
from datetime import datetime, timedelta

PRODUCT_NUM_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2
SALES_TAX_RATE = 0.06


def read_dictionary(filename, key_column_index):
    """
    Reads the product data from the csv file and returns a dictionary.
    Each key is from key_column_index, and each value is the row list.
    """
    dictionary = {}
    try:
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) != 0:
                    key = row[key_column_index]
                    dictionary[key] = row
        return dictionary
    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
        exit()
    except PermissionError as e:
        print("Error: permission denied")
        print(e)
        exit()


def main():
    try:
        # Read product catalog
        products_dict = read_dictionary("products.csv", PRODUCT_NUM_INDEX)

        # Open and read request.csv
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skip header

            print("Inkom Emporium\n")

            total_items = 0
            subtotal = 0

            for row in reader:
                if len(row) != 0:
                    prod_num = row[0]
                    quantity = int(row[1])
                    
                    # This may raise KeyError, which we want to catch
                    product_info = products_dict[prod_num]
                    product_name = product_info[PRODUCT_NAME_INDEX]
                    price = float(product_info[PRODUCT_PRICE_INDEX])

                    line_total = quantity * price
                    subtotal += line_total
                    total_items += quantity

                    print(f"{product_name}: {quantity} @ {price:.2f}")

            # Compute totals
            sales_tax = subtotal * SALES_TAX_RATE
            total = subtotal + sales_tax

            # Print receipt summary
            print(f"\nNumber of Items: {total_items}")
            print(f"Subtotal: {subtotal:.2f}")
            print(f"Sales Tax: {sales_tax:.2f}")
            print(f"Total: {total:.2f}")
            print("\nThank you for shopping at the Inkom Emporium.")

            # Print current date and time
            current_datetime = datetime.now()
            print(current_datetime.strftime("%a %b %d %H:%M:%S %Y"))

            # Enhancement: Add return-by date (30 days from now at 9:00 PM)
            return_date = current_datetime + timedelta(days=30)
            return_date = return_date.replace(hour=21, minute=0, second=0)
            print("Return by:", return_date.strftime("%a %b %d %I:%M %p %Y"))

    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
    except PermissionError as e:
        print("Error: permission denied")
        print(e)
    except KeyError as key_err:
        print("Error: unknown product ID in the request.csv file")
        print(f"{key_err}")


if __name__ == "__main__":
    main()

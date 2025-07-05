import math
from datetime import date

# Prompt user for input
width = int(input("Enter the width of the tire in mm (e.g., 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (e.g., 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (e.g., 15): "))

# Calculate the tire volume using the given formula
volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Round the volume to two decimal places
volume_rounded = round(volume, 2)

# Display the result
print(f"\nThe approximate volume of the tire is {volume_rounded} liters.")

# Get the current date
today = date.today()

# Write the data to a log file
with open("tire_volume_log.txt", "a") as log_file:
    log_file.write(f"{today}, {width}, {aspect_ratio}, {diameter}, {volume_rounded}\n")

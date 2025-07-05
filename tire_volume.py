"""
tire_volume program accepts user input that describes a tire then calculate and display the tire's volume.
"""
import math
from datetime import datetime as date

# User enters the tire width in mm
tire_width = float(input("pleae enter the tire width: "))

# User enters the aspect ratio
aspect_ratio = float(input("please enter the aspect ratio: "))

# User enters the diameter of the wheel in inches
wheel_diameter = float(input("please enter the wheel diameter: "))

#Calculate and displays the tire's volume.
tire_volume = math.pi * tire_width ** 2 * aspect_ratio * (tire_width * aspect_ratio + 2540 * wheel_diameter) / 10000000000
result = tire_volume

# Display the result
print(f"\nThe approximate volume of the tire is {result:.2f} liters.")

# Current date
today = date.now()
current_date = today.strftime("%Y-%m-%d")
print(f"Current date is {current_date}")

# Write the data to a log file
with open("tire_volume_log.txt", "a") as log_file:
    log_file.write(f"Current Date: {current_date}, Width: {tire_width}, Aspect Ratio: {aspect_ratio}, Diameter: {wheel_diameter}, Tire Volume: {result:.2f}\n")



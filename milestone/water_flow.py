"""
W03 Project: Water Pressure System Calculator

Enhancements:
- Used constants for gravity, water density, and viscosity
- Added a function to convert kPa to psi
- Displays final pressure in both kPa and psi
"""

# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s^2
WATER_DENSITY = 998.2  # kg/m^3
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pa·s

def water_column_height(tower_height, tank_height):
    return tower_height + (3 * tank_height) / 4

def pressure_gain_from_water_height(height):
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    return (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2) / (2000 * pipe_diameter)

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    return (-0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    d_ratio = (larger_diameter / smaller_diameter)**4 - 1
    k = 0.1 + (50 / reynolds_number) * d_ratio
    return (-k * WATER_DENSITY * fluid_velocity**2) / 2000

def kpa_to_psi(kpa):
    return kpa * 0.145038

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    supply_pipe_length = float(input("Length of supply pipe from tank to lot (meters): "))
    num_fittings = int(input("Number of 90° angles in supply pipe: "))
    house_pipe_length = float(input("Length of pipe from supply to house (meters): "))

    h = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(h)

    velocity = 1.75  # assumed average velocity in m/s
    friction_factor = 0.018
    diameter_supply = 0.048692
    diameter_house = 0.048692

    pressure += pressure_loss_from_pipe(diameter_supply, supply_pipe_length, friction_factor, velocity)
    pressure += pressure_loss_from_fittings(velocity, num_fittings)
    pressure += pressure_loss_from_pipe(diameter_house, house_pipe_length, friction_factor, velocity)

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {kpa_to_psi(pressure):.1f} psi")

if __name__ == "__main__":
    main()

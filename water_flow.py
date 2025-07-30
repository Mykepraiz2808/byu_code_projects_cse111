"""
W03 Project: Water Pressure System

Enhancements:
1. Uses named constants for gravity, water density, and viscosity.
2. Includes a conversion function from kPa to psi.
3. Calls all major functions and prints output in both kPa and psi.
"""

# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s²
WATER_DENSITY = 998.2  # kg/m³
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pa·s

def water_column_height(tower_height, tank_height):
    """Compute height of water column from tower and 3/4 tank height."""
    return tower_height + (3 * tank_height / 4)

def pressure_gain_from_water_height(height):
    """Compute pressure gained from water height."""
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Compute pressure loss from a pipe."""
    return (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2) / (2000 * pipe_diameter)

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Compute pressure loss due to fittings."""
    return (-0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Compute Reynolds number for a pipe."""
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Compute pressure loss from a reduction in pipe size."""
    d_ratio = (larger_diameter / smaller_diameter)**4 - 1
    k = 0.1 + (50 / reynolds_number) * d_ratio
    return (-k * WATER_DENSITY * fluid_velocity**2) / 2000

def kpa_to_psi(kpa):
    """Convert pressure from kilopascals to pounds per square inch."""
    return kpa * 0.145038

def main():
    """Main function to calculate final house pressure."""
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    pipe_length_to_lot = float(input("Length of supply pipe from tank to lot (meters): "))
    num_fittings = int(input("Number of 90° angles in supply pipe: "))
    pipe_length_to_house = float(input("Length of pipe from supply to house (meters): "))

    h = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(h)

    # Assumed values
    velocity = 1.75  # m/s
    f = 0.018
    d1 = d2 = 0.048692  # diameter in meters (supply and house)

    pressure += pressure_loss_from_pipe(d1, pipe_length_to_lot, f, velocity)
    pressure += pressure_loss_from_fittings(velocity, num_fittings)
    pressure += pressure_loss_from_pipe(d2, pipe_length_to_house, f, velocity)

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {kpa_to_psi(pressure):.1f} psi")

if __name__ == "__main__":
    main()

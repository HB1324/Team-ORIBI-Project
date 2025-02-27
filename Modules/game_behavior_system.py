"""
Program Title: game_behavior_system.py
Program Version: 0.0.2
Author: -Hunter Brown-
Date Created: (02/26/2025)
Description: Behavior module concept for ORIBI Project: Defenders of LA
Dependencies: Python 3.12
License: None
FIXME- DEV Notes: Used as a concept document. Can be modified to fit use case.
"""

### Wind + Fire Direction & Intensity ###
# ---------------------------------------------------------------------------------------
import random


def generate_wind_direction():
    """
    Generates a random wind direction represented by numbers 0-7.
    0 - N, 1 - NE, 2 - E, 3 - SE, 4 - S, 5 - SW, 6 - W, 7 - NW.

    Returns:
        int: A random number between 0 and 7 representing wind direction.
    """
    return random.randint(0, 7)


def get_wind_direction():
    """
    Gets the wind direction as a string.

    Returns:
        tuple: (direction_code, direction_name)
    """
    directions_map = {
        0: "N",
        1: "NE",
        2: "E",
        3: "SE",
        4: "S",
        5: "SW",
        6: "W",
        7: "NW",
    }
    direction = generate_wind_direction()
    return direction, directions_map[direction]


def generate_wind_intensity():
    """
    Gets a random wind intensity represented by numbers 0-5.

    Returns:
        int: A random number between 0 and 5 representing wind intensity.
    """
    return random.randint(0, 5)


def get_wind_intensity():
    """
    Gets the wind intensity as a string.

    Returns:
        tuple: (intensity_level, intensity_name)
    """
    intensity_map = {
        0: "Very Low",
        1: "Low",
        2: "Medium",
        3: "High",
        4: "Very High",
        5: "Extreme",
    }
    intensity = generate_wind_intensity()
    return intensity, intensity_map[intensity]


def get_fire_spread_direction(wind_direction, wind_intensity):
    """
    Determines the fire spread direction based on wind.

    The fire will primarily spread in the wind's direction but has a chance to deviate
    based on wind intensity.

    Args:
        wind_direction (int): The wind direction (0-7).
        wind_intensity (int): The wind intensity (0-5).

    Returns:
        str: The direction the fire is spreading.
    """
    spread_map = {
        0: "N",
        1: "NE",
        2: "E",
        3: "SE",
        4: "S",
        5: "SW",
        6: "W",
        7: "NW",
    }

    # Higher intensity means more chaotic spread
    deviation_chance = max(1, 8 - (2 * wind_intensity))  # Lower intensity = more stability
    if random.randint(1, deviation_chance) != 1:  # Higher intensity = more stable
        fire_direction = wind_direction  # Fire follows wind
    else:
        # Small chance to spread to an adjacent direction
        fire_direction = (wind_direction + random.choice([-1, 1])) % 8

    return spread_map[fire_direction]


# Example usage
if __name__ == "__main__":
    wind_direction_code, wind_direction = get_wind_direction()
    wind_intensity_level, wind_intensity = get_wind_intensity()
    fire_spread = get_fire_spread_direction(wind_direction_code, wind_intensity_level)

    print(f"Wind Direction: {wind_direction}")
    print(f"Fire Spread: {fire_spread}")
    print(f"Intensity: {wind_intensity}")

# Desired Result
"Wind Direction: (Direction)"
"Fire Spread: (Direction close to Wind Direction)"
"Intensity: (Intensity that dictates the deviation of the fire spread)"

# ---------------------------------------------------------------------------------------

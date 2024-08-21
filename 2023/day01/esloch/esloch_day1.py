"""
Advent of Code 2023 - Day 1 by Esloch
"""


def count_line(path_file):
    """
    Counts the sum of the first and last digits of each line in a file.
    
    Returns:
        int: The sum of the first and last digits of each line.
    """
    count = 0
    with open(path_file) as f:
        for line in f:
            # Extract all the digits from the line
            digits = [char for char in line if char.isdigit()]
            calibration_value = int(digits[0] + digits[-1])
            count += calibration_value
    
    return count

# Advent of Code 2025 - Day 3, Puzzle 1
# This script reads numbers from a file, splits each number into its digits,
# finds the two largest digits, and calculates a total output joltage.

def parse_input_file(file_path, array):
    """
    Reads integers from a file, one per line, and appends them to 'array'.
    Returns the list of numbers read.
    """
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
        array.extend(numbers)
    return numbers

def two_max_numbers(nums):
    """
    Returns the two largest numbers in the list 'nums'.
    Raises ValueError if the list contains fewer than two numbers.
    """
    if len(nums) < 2:
        raise ValueError("List must contain at least two numbers.")
    max1 = max(nums[:-1])
    idx1 = nums.index(max1)
    # Find the next max after idx1
    max2 = None
    for i in range(idx1 + 1, len(nums)):
        if max2 is None or nums[i] > max2:
            max2 = nums[i]
    return max1, max2

if __name__ == "__main__":
    batteries = []
    sum_of_max = 0

    # Read numbers from input file and store in batteries
    numbers = parse_input_file('day_3/input.txt', batteries)
    # Split each number into its digits
    bank_of_batteries = [list(map(int, str(num))) for num in batteries]

    # For each battery, find the two largest digits and calculate output
    for battery in bank_of_batteries:
        max1, max2 = two_max_numbers(battery)
        sum_of_max += max1*10 + max2

    print(f"Total output joltage: {sum_of_max}")

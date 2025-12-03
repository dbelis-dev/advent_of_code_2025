# Advent of Code 2025 - Day 2, Puzzle 1
# This script parses a file containing ID ranges and calculates the sum of IDs
# where the left half of the digits matches the right half.

def parse_input_file(file_path):
    """
    Parses the input file and returns a list of ID ranges.
    Each line in the file is expected to be a comma-separated list of ranges.
    """
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split(',')
        return line

def find_repeated_ids(id_lists):
    """
    For each ID range, finds IDs where the left half of the digits matches the right half.
    Returns the sum of such IDs.
    """
    sum = 0
    for ids in id_lists:
        min, max = ids.split('-')
        id_range = range(int(min), int(max) + 1)
        # Iterate through each ID in the range
        for id in id_range:
            lng = len(str(id))
            left_digits = str(id)[:lng//2]
            right_digits = str(id)[-lng//2:]
            if left_digits == right_digits:
                sum += id
    return sum


if __name__ == "__main__":
    # Parse the input file to get ID ranges
    id_lists = parse_input_file('day_2/input.txt')
    # Find and sum repeated IDs
    sum = find_repeated_ids(id_lists)
    print(f"Sum of repeated IDs: {sum}")

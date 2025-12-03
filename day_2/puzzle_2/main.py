# Advent of Code 2025 - Day 2, Puzzle 2
# This script parses a list of ID ranges from an input file,
# checks for IDs with repeated character groups, and sums them.

def parse_input_file(file_path):
    """
    Reads the input file and returns a list of ID range strings.
    Each line in the file is expected to be a comma-separated list of ranges.
    """
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split(',')
        return line

def group_chars_with_step(str, n):
    """
    Splits the input string into groups of size n.
    Returns a list of these groups.
    """
    return [str[i:i+n] for i in range(0, len(str), n)]

def all_groups_match(group):
    """
    Checks if all elements in the group list are identical.
    Returns True if all match, False otherwise.
    """
    if not group:
        return False
    first_group = group[0]
    return all(g == first_group for g in group)

def find_repeated_ids(id_lists):
    """
    For each ID range in id_lists, checks each ID to see if it can be split
    into groups of equal characters (with any possible group size).
    Sums and returns all such IDs.
    """
    sum = 0
    for ids in id_lists:
        min, max = ids.split('-')
        id_range = range(int(min), int(max) + 1)
        for id in id_range:
            step = 1
            while step <= len(str(id)) // 2:
                char_groups = group_chars_with_step(str(id), step)
                if all_groups_match(char_groups):
                    sum += id
                    break
                step += 1
    return sum


if __name__ == "__main__":
    # Parse the input file to get the list of ID ranges
    id_lists = parse_input_file('day_2/input.txt')
    # Find and sum all IDs with repeated character groups
    sum = find_repeated_ids(id_lists)
    print(f"Sum of repeated IDs: {sum}")

def read_ranges(filename):
    """
    Reads range pairs from a file and returns a list of tuples.

    Each line in the file should contain two integers separated by a dash (e.g., "10-15").
    The function parses each line, and for valid lines, appends a tuple (b, b - a) to the result list,
    where 'a' and 'b' are the parsed integers.

    Args:
        filename (str): Path to the file containing range pairs.

    Returns:
        list of tuple: A list of tuples, each containing (b, b - a).
    """
    ranges = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split('-')
            if len(parts) != 2:
                continue
            try:
                a = int(parts[0])
                b = int(parts[1])
                ranges.append((b, b - a))
            except ValueError:
                continue
    return ranges

def read_ingredients(filename, fresh_ranges):
    """
    Counts the number of ingredients that fall within any of the provided fresh ranges.

    Each line in the file should contain a single integer representing an ingredient.
    For each ingredient, the function checks if it falls within any of the ranges in 'fresh_ranges'.
    A range is represented as a tuple (b, length), and an ingredient is valid if
    (b - ingredient) is between 0 and length (inclusive).

    Args:
        filename (str): Path to the file containing ingredient values.
        fresh_ranges (list of tuple): List of tuples representing ranges as (b, length).

    Returns:
        int: The count of valid ingredients.
    """
    counter = 0
    with open(filename, 'r') as f:
        for ingr in f:
            ingr = int(ingr.strip())
            if not ingr:
                continue
            for fresh in fresh_ranges:
                sub = fresh[0] - ingr
                if sub >= 0 and sub <= fresh[1]:
                    counter += 1
                    break
    return counter


if __name__ == "__main__":
    # Read the ranges from the input file
    ranges = read_ranges('day_5/input1.txt')
    # Read the ingredients from the array and count how many are valid
    counter = ingredients = read_ingredients('day_5/input2.txt', ranges)

    print(f"Number of valid ingredients: {counter}")


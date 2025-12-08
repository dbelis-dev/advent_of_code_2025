import re

def read_triplets_from_file(filename):
    """
    Reads a file containing lines of three comma-separated integers and returns a list of triplets.

    Args:
        filename (str): The path to the file to read.

    Returns:
        list[tuple[int, int, int]]: A list of tuples, each containing three integers from a line in the file.

    Notes:
        - Lines that do not contain exactly three comma-separated values are ignored.
        - Lines with non-integer values are skipped.
    """
    triplets = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 3:
                try:
                    triplet = tuple(int(x) for x in parts)
                    triplets.append(triplet)
                except ValueError:
                    continue
    return triplets

def add_and_sort(items, value, idx1, idx2):
    """
    Adds a formatted string representing a value and its associated indices to the provided list.

    Parameters:
        items (list of str): The list to which the new item will be added.
        value (int): The integer value to include in the formatted string.
        idx1 (int): The first index to include in the formatted string.
        idx2 (int): The second index to include in the formatted string.

    Returns:
        list of str: The updated list with the new formatted item appended.

    Note:
        The function does not perform any sorting, despite the name and initial docstring.
        The item is added in the format "value (idx1, idx2)".
    """
    item = f"{value} ({idx1}, {idx2})"
    items.append(item)
    return items

def euclidean_distance_3d(p1, p2):
    """
    Calculate the Euclidean distance between two points in 3D space.

    Args:
        p1 (tuple[float, float, float]): The first point as a tuple of (x, y, z) coordinates.
        p2 (tuple[float, float, float]): The second point as a tuple of (x, y, z) coordinates.

    Returns:
        float: The Euclidean distance between p1 and p2.

    Example:
        >>> euclidean_distance_3d((1, 2, 3), (4, 5, 6))
        5.196152422706632
    """
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2) ** 0.5

def process_point_pairs(points):
    """
    Processes all unique pairs of points from the input list and calculates their Euclidean distance in 3D space.
    
    For each unique pair (i, j) where i < j, computes the distance between points[i] and points[j] using euclidean_distance_3d,
    and updates the global distance_results by adding and sorting the new distance with its corresponding indices.

    Args:
        points (list of tuple or list): A list of 3D points, where each point is represented as a tuple or list of three coordinates (x, y, z).

    Returns:
        None: The function updates the global variable distance_results in place.
    """
    global distance_results
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1 = points[i]
            p2 = points[j]
            dist = euclidean_distance_3d(p1, p2)
            distance_results = add_and_sort(distance_results, dist, i, j)

def add_or_update_tuple(tup, tup_list):
    """
    Adds or updates a tuple in a list of tuples based on shared values.

    Given a tuple `tup` and a list of tuples `tup_list`, this function checks if any value in `tup` exists in any tuple in `tup_list`:
    - If both values of `tup` exist in different tuples, those tuples are merged into one containing all unique values.
    - If one value exists in a tuple, the other value is added to that tuple.
    - If neither value exists, `tup` is appended to `tup_list`.

    Returns:
        list: The updated list of unique tuples, with merged or added values as necessary.
    """
    updated = False
    first = second = ()
    for i, existing in enumerate(tup_list):
        if tup[0] in existing:
            first = existing
            updated = True
        elif tup[1] in existing:
            second = existing
            updated = True
    if first and second:
        tup_list.remove(first)
        tup_list.remove(second)
        tup_list.append(tuple(set(first + second)))
    elif first:
        tup_list.remove(first)
        tup_list.append(tuple(set(first + (tup[1],))))
    elif second:
        tup_list.remove(second)
        tup_list.append(tuple(set(second + (tup[0],))))
    if not updated:
        tup_list.append(tup)
    return list(set(tup_list))

def process_distance_results(distance_results, tuple_list, max_counter):
    """
    Processes a list of distance result strings, updating a tuple list with extracted index tuples.

    Each item in `distance_results` is expected to be a string containing a floating-point number
    followed by a tuple in the format "(int, int)". The function extracts the tuple, updates
    `tuple_list` using the `add_or_update_tuple` function, and stops processing if the length of
    the first element in `tuple_list` reaches `max_counter`.

    Args:
        distance_results (list of str): List of strings containing distance results and index tuples.
        tuple_list (list): List to be updated with extracted tuples.
        max_counter (int): Maximum allowed length for the first element in `tuple_list`.

    Returns:
        tuple: A tuple containing the updated `tuple_list` and the last extracted index tuple.

    Raises:
        AttributeError: If a string in `distance_results` does not match the expected format.
    """
    for i, item in enumerate(distance_results):
        m = re.match(r"([+-]?\d+(?:\.\d+)?)\s+\((\d+),\s*(\d+)\)", item)
        idx_tuple = (int(m.group(2)), int(m.group(3)))
        tuple_list = add_or_update_tuple(idx_tuple, tuple_list)
        if len(tuple_list[0]) == max_counter:
            break
    return tuple_list, idx_tuple


if __name__ == "__main__":
    # Initialize the results and tuple list
    distance_results = []
    tuple_list = []
    
    # Read 3D points from the input file
    points = read_triplets_from_file('day_8/input.txt')
    
    # Process all unique pairs of points to calculate their distances
    process_point_pairs(points)
    
    # Set the maximum counter to the number of points
    max_counter = len(points)

    # Define a sorting key to sort distance_results by the numeric distance value
    def sort_key(s):
        m = re.match(r"([+-]?\d+(?:\.\d+)?)\s+\((\d+),\s*(\d+)\)", s)
        return float(m.group(1))
    
    # Sort the distance results by distance
    distance_results.sort(key=sort_key)

    # Process the sorted distance results to update tuple_list and get the last index tuple
    tuple_list, idx_tuple = process_distance_results(distance_results, tuple_list, max_counter)
    
    # Multiply together the coordinates of the last two junction boxes
    mult_tuple = tuple(a * b for a, b in zip(points[idx_tuple[0]], points[idx_tuple[1]]))
    
    # Print the result for the X coordinates
    print(f"Multiply together the X coordinates of the last two junction boxes: {mult_tuple[0]}")



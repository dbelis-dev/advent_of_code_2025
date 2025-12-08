import re

def read_triplets_from_file(filename):
    """
    Reads a file and stores each triplet of integers in a list.
    Assumes each line contains three integers separated by commas.
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

def add_indexes(items, value, idx1, idx2):
    """
    Appends a formatted string containing a value and two indexes to a list.

    Args:
        items (list): The list to which the formatted string will be appended.
        value (Any): The value to include in the formatted string.
        idx1 (int): The first index to include in the formatted string.
        idx2 (int): The second index to include in the formatted string.

    Returns:
        list: The updated list with the new formatted string appended.
    """
    item = f"{value} ({idx1}, {idx2})"
    items.append(item)
    return items

def euclidean_distance_3d(p1, p2):
    """
    Calculate the Euclidean distance between two points in 3D space.

    Args:
        p1 (tuple or list of float): The coordinates (x, y, z) of the first point.
        p2 (tuple or list of float): The coordinates (x, y, z) of the second point.

    Returns:
        float: The Euclidean distance between p1 and p2.

    Example:
        >>> euclidean_distance_3d((1, 2, 3), (4, 5, 6))
        5.196152422706632
    """
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2) ** 0.5

def process_point_pairs(points):
    """
    Processes all unique pairs of points from the given list and computes the Euclidean distance between each pair.
    For each pair, updates the global variable `distance_results` by adding the computed distance along with the indexes of the points.

    Args:
        points (list): A list of points, where each point is expected to be a 3D coordinate (e.g., tuple or list of three numbers).

    Side Effects:
        Updates the global variable `distance_results` with the computed distances and corresponding point indexes.
    """
    global distance_results
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1 = points[i]
            p2 = points[j]
            dist = euclidean_distance_3d(p1, p2)
            distance_results = add_indexes(distance_results, dist, i, j)

def add_or_update_tuple(tup, tup_list):
    """
    Adds a tuple to a list of tuples, merging or updating existing tuples if there are shared elements.

    If either element of `tup` exists in any tuple in `tup_list`, the function will:
    - Merge tuples if both elements are found in different tuples.
    - Add the missing element to the existing tuple if only one element is found.
    - If neither element is found, add `tup` as a new tuple.

    Args:
        tup (tuple): A tuple of two elements to add or update in the list.
        tup_list (list of tuple): The list of tuples to update.

    Returns:
        list of tuple: The updated list of tuples with merged or added tuples as necessary.
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
    Processes a list of distance result strings, extracts tuple indices from each string,
    and updates the provided tuple list using the add_or_update_tuple function. The function
    processes up to max_counter items from the distance_results list.

    Args:
        distance_results (list of str): List of strings containing distance results in the format
            "<number> (<int>, <int>)".
        tuple_list (list): List of tuples to be updated.
        max_counter (int): Maximum number of items to process from distance_results.

    Returns:
        list: The updated tuple_list after processing the specified number of distance results.

    Note:
        The function expects the existence of an add_or_update_tuple function that handles
        updating or adding tuples to tuple_list.
    """
    counter = 0
    for i, item in enumerate(distance_results):
        counter += 1
        m = re.match(r"([+-]?\d+(?:\.\d+)?)\s+\((\d+),\s*(\d+)\)", item)
        idx_tuple = (int(m.group(2)), int(m.group(3)))
        tuple_list = add_or_update_tuple(idx_tuple, tuple_list)
        if counter > max_counter - 1:
            break
    return tuple_list


if __name__ == "__main__":
    # Initialize the results and tuple list
    distance_results = []
    tuple_list = []
    counter = 0
    max_counter = 1000  # Maximum number of distances to process

    # Read 3D points from the input file
    points = read_triplets_from_file('day_8/input.txt')

    # Compute all pairwise Euclidean distances and store them in distance_results
    process_point_pairs(points)

    # Helper function to extract the distance value for sorting
    def sort_key(s):
        m = re.match(r"([+-]?\d+(?:\.\d+)?)\s+\((\d+),\s*(\d+)\)", s)
        return float(m.group(1))

    # Sort the distance results by distance value (ascending)
    distance_results.sort(key=sort_key)

    # Process the sorted distances to build/merge tuples of connected point indexes
    tuple_list = process_distance_results(distance_results, tuple_list, max_counter)

    # Find the lengths of the three largest circuits (tuples)
    top_lengths = sorted([len(t) for t in tuple_list], reverse=True)[:3]

    # Compute the product of the sizes of the three largest circuits, if there are at least three
    product_of_top_lengths = top_lengths[0] * top_lengths[1] * top_lengths[2] if len(top_lengths) >= 3 else None

    # Output the result
    print("Product of the three largest circuits:", product_of_top_lengths)


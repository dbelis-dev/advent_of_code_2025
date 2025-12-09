def read_tiles_from_file(filename):
    """
    Each line in the file is expected to contain two integers separated by a comma.
    Lines that do not contain exactly two comma-separated values or contain non-integer values are ignored.

    Args:
        filename (str): The path to the file containing the tiles.

    Returns:
        list[tuple[int, int]]: A list of tuples, each containing two integers representing a tile.
    """
    tiles = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 2:
                try:
                    tile = tuple(int(x) for x in parts)
                    tiles.append(tile)
                except ValueError:
                    continue
    return tiles

def calculate_areas_between_tiles(tiles):
    """
    Calculates the area between each pair of points in the 'tiles' list.

    Each point in 'tiles' is represented as a tuple (x, y). For every unique pair of points,
    the function computes the area of the rectangle defined by the two points as opposite corners,
    including both endpoints.

    Args:
        tiles (list of tuple): A list of tuples, where each tuple represents a point (x, y).

    Returns:
        list of tuple: A list of tuples, where each tuple contains:
            - a pair of points ((x1, y1), (x2, y2))
            - the area (int) of the rectangle defined by these two points
    """
    areas = []
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            area = (abs((x2 - x1)) + 1) * (abs(y2 - y1) + 1)
            areas.append(((tiles[i], tiles[j]), area))
    return areas

if __name__ == "__main__":
    # Read the list of tiles (points) from the input file
    tiles = read_tiles_from_file('day_9/input.txt')
    
    # Calculate the area between every unique pair of tiles
    areas = calculate_areas_between_tiles(tiles)
    
    # Sort the list of areas by the area value (ascending order)
    sorted_areas = sorted(areas, key=lambda x: x[1])
    
    # Get the largest area from the sorted list (last element)
    _, max_area = sorted_areas[-1]
    
    # Print the largest area found between any pair of tiles
    print(f"Largest Area between tile pairs: {max_area}")

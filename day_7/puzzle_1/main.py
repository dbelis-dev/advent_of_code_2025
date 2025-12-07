def read_file_to_2d_array(filename):
    """
    Reads a text file and converts it into a 2D array (list of lists), 
    where each inner list represents a line split into characters.

    Args:
        filename (str): Path to the input file.

    Returns:
        List[List[str]]: 2D array of characters from the file.
    """
    with open(filename, 'r') as f:
        return [list(line.rstrip('\n')) for line in f]
    
def get_index_below(grid, row, col):
    """
    For a given (row, col) in a 2D array, checks the element directly below.
    If it's not '.', returns the indexes (row+1, col-1) and (row+1, col+1).
    Otherwise, returns an empty list.

    Args:
        grid (List[List[str]]): 2D array.
        row (int): Row index.
        col (int): Column index.

    Returns:
        List[Tuple[int, int]]: List of (row, col) tuples for left and right below, or empty list.
    """
    global counter
    next = (row + 1, col)
    # Check if the next row is out of bounds
    if row + 1 >= len(grid):
        return None
    # If the cell below is not '.', we have a split
    if grid[row + 1][col] != '.':
        # Increment the split counter
        counter += 1
        result = []
        # Check if the left diagonal cell is within bounds
        left = (row + 1, col - 1) if col - 1 >= 0 else None
        # Check if the right diagonal cell is within bounds
        right = (row + 1, col + 1) if col + 1 < len(grid[0]) else None
        if left:
            result.append(left)
        if right:
            result.append(right)
        # Return the indices of the split positions
        return result
    else:
        # If the cell below is '.', continue straight down
        return [next]

def traverse_grid(grid, start):
    """
    Traverses the grid starting from the given start position,
    following the logic in get_index_below, and counts splits.

    Args:
        grid (List[List[str]]): 2D array.
        start (Tuple[int, int]): Starting position (row, col).

    Returns:
        int: Total splits found (value of global counter).
    """
    global counter
    # Get the next index(es) to traverse from the starting position
    new_index = get_index_below(grid, start[0], start[1])
    # If there are two indices (split), wrap them in a list for uniform processing
    if len(new_index) == 2:
        new_index = [new_index]
    # Continue traversing until there are no more indices to process
    while True:
        row_idx = []
        # For each current index, get the next index(es) below
        for index in new_index:
            new_idx = get_index_below(grid, index[0], index[1])
            # If we've reached the end of the grid, stop processing
            if new_idx is None:
                break
            # Accumulate all next indices to process in the next iteration
            row_idx += (new_idx)
        # Remove duplicates by converting to a set
        new_index = set(row_idx)
        # If there are no more indices to process, exit the loop
        if len(new_index) == 0:
            break


if __name__ == "__main__":
    # Read the input file into a 2D array
    grid = read_file_to_2d_array('day_7/input.txt')
    
    s_index = grid[0].index('S')
    start = (0, s_index)
    counter = 0

    traverse_grid(grid, start)
    print(f"Total splits found: {counter}")

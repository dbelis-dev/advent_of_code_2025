
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

def iterate_2d_array(array):
    """
    Iterates over a 2D array, searching for '@' characters. For each '@', 
    extracts a 3x3 window centered on it and counts the number of '@' 
    characters in the window (up to a limit of 8). Increments a counter 
    if the count is 4 or less.

    Args:
        array (List[List[str]]): 2D array to process.

    Returns:
        int: Total count of qualifying '@' positions.
    """
    counter = 0
    for i, row in enumerate(array):
        for j, elem in enumerate(row):
            if elem == '@':
                window = get_square_window(grid, i, j, 3)
                count = count_char_with_limit(window, '@', 8)
                if count > 4:
                    continue
                else:
                    counter += 1
    return counter

def get_square_window(array, i, j, window_size):
    """
    Extracts a square window of given size centered at (i, j) from a 2D array.
    Pads with None if the window extends beyond the array boundaries.

    Args:
        array (List[List[str]]): 2D array to extract window from.
        i (int): Row index of the center.
        j (int): Column index of the center.
        window_size (int): Size of the square window.

    Returns:
        List[List[Optional[str]]]: Extracted window as a 2D array.
    """
    half = window_size // 2
    rows = len(array)
    cols = len(array[0]) if rows > 0 else 0
    window = []
    for di in range(-half, half + 1):
        row_idx = i + di
        if 0 <= row_idx < rows:
            row = []
            for dj in range(-half, half + 1):
                col_idx = j + dj
                if 0 <= col_idx < cols:
                    row.append(array[row_idx][col_idx])
                else:
                    row.append(None)
            window.append(row)
        else:
            window.append([None] * (window_size))
    return window

def count_char_with_limit(array, char, limit):
    """
    Counts occurrences of a specific character in a 2D array, 
    stopping early if the count exceeds the given limit.

    Args:
        array (List[List[str]]): 2D array to search.
        char (str): Character to count.
        limit (int): Maximum count before early exit.

    Returns:
        int: Number of occurrences found (may exceed limit).
    """
    count = 0
    for row in array:
        for elem in row:
            if elem == char:
                count += 1
                if count > limit:
                    return count
    return count


if __name__ == "__main__":
    # Read the input file into a 2D array
    grid = read_file_to_2d_array('day_4/input.txt')
    # Process the array and get the final count
    counter = iterate_2d_array(grid)

    print(f"Total count of rolls of paper: {counter}")
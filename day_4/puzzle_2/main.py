
def read_file_to_2d_array(filename):
    """
    Reads a text file and converts it into a 2D array (list of lists), where each line is split into characters.
    Args:
        filename (str): Path to the input file.
    Returns:
        list[list[str]]: 2D array representation of the file's contents.
    """
    with open(filename, 'r') as f:
        return [list(line.rstrip('\n')) for line in f]

def iterate_2d_array(array):
    """
    Iterates over a 2D array, searching for '@' characters. For each '@', checks its 3x3 window for the number of '@' characters.
    If the count is less than or equal to 4, increments the counter and marks the position as 'x'.
    Args:
        array (list[list[str]]): The 2D array to process.
    Returns:
        int: Number of '@' characters processed and marked as 'x' in this iteration.
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
                    array[i][j] = 'x'
    return counter

def get_square_window(array, i, j, window_size):
    """
    Extracts a square window of given size centered at (i, j) from a 2D array.
    Out-of-bounds positions are filled with None.
    Args:
        array (list[list[str]]): The 2D array to extract from.
        i (int): Row index of the center.
        j (int): Column index of the center.
        window_size (int): Size of the square window.
    Returns:
        list[list[Optional[str]]]: The extracted window as a 2D list.
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
    Counts occurrences of a character in a 2D array, stopping early if the count exceeds the given limit.
    Args:
        array (list[list[str]]): The 2D array to search.
        char (str): The character to count.
        limit (int): The maximum count before early exit.
    Returns:
        int: The number of occurrences found (may exceed limit if early exit).
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
    sum_counter = 0
    # Iteratively process the grid until no more changes occur
    while True:
        # Count the number of '@' characters processed in this iteration
        counter = iterate_2d_array(grid)
        # If no more '@' characters are processed, exit the loop
        if counter == 0:
            break
        sum_counter += counter
        
    print(f"Total count of rolls of paper: {sum_counter}")
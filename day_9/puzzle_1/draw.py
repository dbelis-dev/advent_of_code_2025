import curses
# Import functions from main.py
from main import read_tiles_from_file, calculate_areas_between_tiles

# Animate the board updates
def animate_board(stdscr):
    stdscr.clear()
    stdscr.nodelay(True)
    
    for i, (pair, area) in enumerate(areas):
        # Update board for current area
        stdscr.clear()
        max_y, max_x = stdscr.getmaxyx()
        
        # Draw the board as background
        for y, row in enumerate(board):
            for x, val in enumerate(row):
                if 0 <= y < max_y and 0 <= x < max_x:
                    stdscr.addch(y, x, val)
        # Draw the points between the pair
        (x1, y1), (x2, y2) = pair
        # Draw horizontal line
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if 0 <= y1 < max_y and 0 <= x < max_x:
                    if board[y1][x] != '#':
                        stdscr.addch(y1, x, 'o')
                    else:
                        stdscr.addch(y1, x, 'O')
        # Draw vertical line
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if 0 <= y < max_y and 0 <= x1 < max_x:
                    if board[y][x1] != '#':
                        stdscr.addch(y, x1, 'o')
                    else:
                        stdscr.addch(y, x1, 'O')
        # Draw diagonal or all points in rectangle
        else:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    if 0 <= y < max_y and 0 <= x < max_x:
                        if board[y][x] != '#':
                            stdscr.addch(y, x, 'o')
                        else:
                            stdscr.addch(y, x, 'O')
        
        # Display info about current pair
        info = f"Pair {i+1}/{len(areas)}: {pair} - Area: {area}"
        if len(info) < max_x and max_y > len(board) + 1:
            stdscr.addstr(len(board) + 1, 0, info)
        
        stdscr.refresh()
        curses.napms(3000)  # Wait 3 seconds
        
        # Check if user pressed a key to skip
        key = stdscr.getch()
        if key != -1:  # Key was pressed
            return


if __name__ == "__main__":
    # Read the list of tiles (points) from the input file
    tiles = read_tiles_from_file('day_9/sample.txt')
    
    rows, cols = 10, 15
    board = [['.' for _ in range(cols)] for _ in range(rows)]

    for x, y in tiles:
        if 0 <= y < rows and 0 <= x < cols:
            board[y][x] = '#'

    # Calculate the area between every unique pair of tiles
    areas = calculate_areas_between_tiles(tiles)
    
    curses.wrapper(animate_board)

    # Sort the list of areas by the area value (ascending order)
    sorted_areas = sorted(areas, key=lambda x: x[1])
    
    # Get the largest area from the sorted list (last element)
    _, max_area = sorted_areas[-1]
    
    # Print the largest area found between any pair of tiles
    print(f"Largest Area between tile pairs: {max_area}")

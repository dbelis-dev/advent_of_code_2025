# Advent of Code 2025 - Day 1, Puzzle 1
# This script parses a list of dial rotation instructions from a file,
# applies them to a dial, and calculates a password based on the rotations.

def parse_input_file(file_path):
    """
    Reads the instruction file and returns a list of parsed instructions.
    """
    with open(file_path, 'r') as file:
        instructions = file.readlines()
    return parse_instructions_list(instructions)

def parse_instruction(instruction):
    """
    Parses a single instruction string into a (direction, distance) tuple.
    """
    instruction.strip('\n')
    direction = instruction[0]
    distance = int(instruction[1:])
    return (direction, distance)

def parse_instructions_list(instructions):
    """
    Parses a list of instruction strings into a list of (direction, distance) tuples.
    """
    return [parse_instruction(instr) for instr in instructions]

def rotate_dial(dial, direction, distance):
    """
    Rotates the dial left or right by the specified distance.
    """
    if direction == 'L':
        distance = -distance
    distance = distance % len(dial)
    return dial[distance:] + dial[:distance]

def calculate_password(dial, instructions):
    """
    Applies the list of instructions to the dial and counts how many times
    the first element is 0 after a rotation.
    """
    rotated_dial = rotate_dial(dial, 'R', 50)
    counter = 0
    for instr in instructions:
        rotated_dial = rotate_dial(rotated_dial, instr[0], instr[1])
        if rotated_dial[0] == 0:
            counter += 1
    return counter

if __name__ == "__main__":
    # Initialize variables
    instructions = []
    arr_size = 100
    # Parse instructions from input file
    file_instructions = parse_input_file('day_1/input.txt')
    # Create the initial dial
    dial = list(range(arr_size))
    # Calculate the password
    counter = calculate_password(dial, file_instructions)
    print(f"Password to open the door: {counter}")

# Advent of Code 2025 - Day 1 Puzzle 2 Solution
# This script parses a set of dial rotation instructions from a file,
# simulates the rotations, and calculates a password based on the rules.

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


def calculate_password(dial):
    """
    Applies the list of instructions to the dial and counts how many times
    any click causes the dial to point at 0 after a rotation.
    """
    rotated_dial = rotate_dial(dial, 'R', 50)
    counter = 0
    for instr in file_instructions:
        bfr = rotated_dial[0]
        rotated_dial = rotate_dial(rotated_dial, instr[0], instr[1])
        aft = rotated_dial[0]

        # Count full rotations
        if instr[1] >= arr_size:
            counter += instr[1] // arr_size

        # Count if dial lands on 0
        if rotated_dial[0] == 0:
            counter += 1

        # Additional counting rules based on direction and dial position
        if bfr < aft and instr[0] == 'L':
            if bfr == 0:
                continue
            counter += 1
        if bfr > aft and instr[0] == 'R':
            if aft == 0:
                continue
            counter += 1
    return counter

if __name__ == "__main__":
    # Initialize variables and parse input
    instructions = []
    arr_size = 100
    file_instructions = parse_input_file('day_1/input.txt')
    dial = list(range(arr_size))
    # Calculate and print the password
    counter = calculate_password(dial)
    print(f"Password to open the door: {counter}")

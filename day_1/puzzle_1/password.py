# Function to parse a single instruction
def parse_instruction(instruction):
    instruction.strip('\n')
    direction = instruction[0]
    distance = int(instruction[1:])
    return (direction, distance)

# Function to parse a list of instructions
def parse_instructions(instructions):
    return [parse_instruction(instr) for instr in instructions]

def read_instructions_from_file(file_path):
    with open(file_path, 'r') as file:
        instructions = file.readlines()
    return parse_instructions(instructions)

def rotate_dial(dial, direction, distance):
    if direction == 'L':
        distance = -distance
    distance = distance % len(dial)
    return dial[distance:] + dial[:distance]

instructions = []
arr_size = 100
file_instructions = read_instructions_from_file('instructions.txt')
dial = list(range(arr_size)) 
rotated_dial = rotate_dial(dial, 'R', 50)
counter = 0
for instr in file_instructions:
    rotated_dial = rotate_dial(rotated_dial, instr[0], instr[1])
    if rotated_dial[0] == 0:
        counter += 1

print(f"Number of times 0 is at the front: {counter}")
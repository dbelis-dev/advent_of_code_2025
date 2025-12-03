def parse_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split(',')
        return line

def find_repeated_ids(id_lists):
    sum = 0
    for ids in id_lists:
        min, max = ids.split('-')
        id_range = range(int(min), int(max) + 1)
        # print(f"IDs from {min} to {max}: {list(id_range)}")
        for id in id_range:
            lng = len(str(id))
            left_digits = str(id)[:lng//2]
            right_digits = str(id)[-lng//2:]
            if left_digits == right_digits:
                sum += id
    return sum

id_lists = parse_file('day_2/input.txt')
sum = find_repeated_ids(id_lists)
print(f"Sum of repeated IDs: {sum}")
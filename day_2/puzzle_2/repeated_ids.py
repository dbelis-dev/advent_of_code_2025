def parse_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split(',')
        return line

def group_chars_with_step(str, n):
    return [str[i:i+n] for i in range(0, len(str), n)]

def all_groups_match(group):
    if not group:
        return False
    first_group = group[0]
    return all(g == first_group for g in group)

def find_repeated_ids(id_lists):
    sum = 0
    for ids in id_lists:
        min, max = ids.split('-')
        id_range = range(int(min), int(max) + 1)
        for id in id_range:
            step = 1
            while step <= len(str(id)) // 2:
                char_groups = group_chars_with_step(str(id), step)
                if all_groups_match(char_groups):
                    sum += id
                    break
                step += 1
    return sum

id_lists = parse_file('day_2/input.txt')
sum = find_repeated_ids(id_lists)
print(f"Sum of repeated IDs: {sum}")
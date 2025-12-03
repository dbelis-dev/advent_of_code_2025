def two_max_numbers(nums):
    if len(nums) < 2:
        raise ValueError("List must contain at least two numbers.")
    max1 = max(nums[:-1])
    idx1 = nums.index(max1)
    # Find the next max after idx1
    max2 = None
    for i in range(idx1 + 1, len(nums)):
        if max2 is None or nums[i] > max2:
            max2 = nums[i]
    return max1, max2

def read_numbers_from_file(file_path, array):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
        array.extend(numbers)
    return numbers

batteries = []
sum_of_max = 0

numbers = read_numbers_from_file('day_3/input.txt', batteries)
bank_of_batteries = [list(map(int, str(num))) for num in batteries]

for battery in bank_of_batteries:
    max1, max2 = two_max_numbers(battery)
    sum_of_max += max1*10 + max2

print(f"Total output joltage: {sum_of_max}")

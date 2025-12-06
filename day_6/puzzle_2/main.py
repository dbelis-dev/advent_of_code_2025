def read_space_separated_values_as_matrix(filename):
    """
    Reads a text file where each line contains space-separated values, and returns a matrix (list of lists) of the values.
    The function identifies the positions of spaces that are common across all non-empty lines, replaces those spaces with commas,
    and then splits each line by commas to extract the values. Empty strings are filtered out from the results.
    Args:
        filename (str): The path to the file to be read.
    Returns:
        list[list[str]]: A matrix where each sublist contains the values from a line in the file, split by the common space positions.
    Example:
        Given a file with the following content:
            12  34   56
            786 90  127
        The function will return:
            [['12 ', '34', ' 56'],
             ['786', '90', '127']]
    """
    result = []
    spaces = []
    rows = []
    with open(filename, 'r') as f:
        for line in f:
            if line.strip():  # skip empty lines
                rows.append(line.rstrip('\n'))
                # Find indexes of all space characters in the line
                space_indexes = [i for i, c in enumerate(line) if c == ' ']
                if space_indexes:
                    spaces.append(space_indexes)
    
    # Join all lists in spaces and keep only the values that are common across all lists
    if spaces:
        equal_elements = set(spaces[0])
        for s in spaces[1:]:
            equal_elements &= set(s)
        equal_elements = list(equal_elements)
    else:
        equal_elements = []

    # Replace characters at equal_elements indexes with commas in each row
    new_rows = []
    for row in rows:
        row_list = list(row)
        for idx in equal_elements:
            if idx < len(row_list):
                row_list[idx] = ','
        new_rows.append(''.join(row_list))
    
    # Split each row by commas and filter out empty strings
    for row in new_rows:
        split_row = [val for val in row.split(',') if val.strip()]
        result.append(split_row)
    return result

def transpose_matrix(matrix):
    """
    Transposes a matrix (list of rows) to return its columns.

    Args:
        matrix (List[List[Any]]): The input matrix.

    Returns:
        List[List[Any]]: List of columns, where each column is a list of values.
    """
    if not matrix:
        return []
    num_cols = len(matrix[0])
    return [[row[col] for row in matrix] for col in range(num_cols)]

def apply_operator(row):
    """
    Applies an operator ('+' or '*') to a list of operands represented as strings.

    The function expects a list where the last element is an operator ('+' or '*'),
    and the preceding elements are operands (strings of equal length). It constructs
    new numbers by concatenating the i-th character of each operand, then applies
    the specified operator to these numbers.

    For example:
        row = ['123', '456', '+']
        - Constructs ['14', '25', '36']
        - Returns sum: 14 + 25 + 36 = 75

    Args:
        row (list): List of operands (as strings) followed by an operator.

    Returns:
        int: The result of applying the operator to the constructed numbers.
        None: If the input list has fewer than 2 elements.

    Raises:
        ValueError: If the operator is not '+' or '*'.
    """
    if len(row) < 2:
        return None
    *operands, operator = row
    oper = [''.join([str(op)[i] for op in operands]) for i in range(len(operands[0]))]
    if operator.strip() == '+':
        return sum(int(x) for x in oper)
    elif operator.strip() == '*':
        result = 1
        for op in oper:
            result *= int(op)
        return result
    else:
        raise ValueError(f"Unknown operator: {operator}")

def sum_of_columns(row):
    """
    Sums the values in a row. If the row has fewer than 2 elements, returns the first element.

    Args:
        row (List[int]): List of integers.

    Returns:
        int: The sum of the row or the first element if row has fewer than 2 elements.
    """
    if len(row) < 2:
        return row[0]
    return sum(row)


if __name__ == "__main__":
    # Read the input file as a matrix of rows
    data = read_space_separated_values_as_matrix('day_6/input.txt')

    # Transpose the matrix to get columns
    columns = transpose_matrix(data)

    # Apply the operator to each column and collect the results
    results = [apply_operator(col) for col in columns]

    # Sum the results from all columns
    sum_results = sum_of_columns(results)
    
    # Print the grand total
    print(f"Grand total: {sum_results}")


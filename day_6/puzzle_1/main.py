def read_space_separated_values_as_matrix(filename):
    """
    Reads a space-separated values file and returns its contents as a list of rows.
    Each row is a list containing integers (if possible) or strings.
    Skips empty lines.

    Args:
        filename (str): Path to the input file.

    Returns:
        List[List[Union[int, str]]]: List of rows from the file.
    """
    result = []
    with open(filename, 'r') as f:
        for line in f:
            if line.strip():  # skip empty lines
                row = [int(x) if x.isdigit() else x for x in line.strip().split()]
                result.append(row)
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
    Applies an operator ('+' or '*') to the operands in the row.
    The operator is expected to be the last element of the row.

    Args:
        row (List[Any]): List containing operands followed by an operator.

    Returns:
        int or None: The result of applying the operator, or None if insufficient operands.

    Raises:
        ValueError: If the operator is unknown.
    """
    if len(row) < 2:
        return None
    *operands, operator = row
    if operator == '+':
        return sum(operands)
    elif operator == '*':
        result = 1
        for op in operands:
            result *= op
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
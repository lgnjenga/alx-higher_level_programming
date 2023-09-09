#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of the matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list,
        a list of lists, or contains non-integer/non-float elements.
        ValueError: If m_a or m_b is empty,
        or if they can't be multiplied due to incompatible dimensions.

    """

    # Validate input matrices
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list and m_b must be a list")

    if not all(
            isinstance(row, list) for row in m_a) or not all(
                    isinstance(row, list) for row in m_b):
        raise TypeError("m_a and m_b must be a list of lists")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty and m_b can't be empty")

    if not all(isinstance(
        val, (int, float)) for row in m_a for val in row) or not all(
                isinstance(val, (int, float)) for row in m_b for val in row):
        raise TypeError("m_a and m_b should contain only integers or floats")

    # Check if the matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result


# Example usage
if __name__ == "__main__":
    m1 = [[1, 2], [3, 4]]
    m2 = [[1, 2], [3, 4]]
    result = matrix_mul(m1, m2)
    for row in result:
        print(row)

    m3 = [[1, 2]]
    m4 = [[3, 4], [5, 6]]
    result2 = matrix_mul(m3, m4)
    for row in result2:
        print(row)

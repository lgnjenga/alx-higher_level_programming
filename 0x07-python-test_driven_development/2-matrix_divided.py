#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor 'div',
    rounding to 2 decimal places.

    Args:
        matrix (list of lists): The input matrix containing integers or floats.
        div (int or float): The divisor for the division operation.

    Returns:
        list of lists: A new matrix with elements divided by 'div'
        and rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   or if the rows of the matrix have different sizes,
                   or if 'div' is not a number (integer or float).
        ZeroDivisionError: If 'div' is equal to 0.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(
            isinstance(row, list) and all(
                isinstance(elem, (int, float)) for elem in row
                ) for row in matrix):
        raise TypeError(
                "matrix must be a matrix(list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    result = [[round(elem / div, 2) for elem in row] for row in matrix]

    return result


# Example usage:
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)

#!/usr/bin/python3
"""Module to generate Pascal's triangle."""


def pascal_triangle(n):
    """Generate Pascal's triangle with n rows.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    
    for i in range(n):
        # Start with a row of 1's
        row = [1] * (i + 1)
        
        # Each element (except the first and last) is the sum of the two elements above it
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        triangle.append(row)
    
    return triangle

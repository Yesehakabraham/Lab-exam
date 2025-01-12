import numpy as np

def compute_cross_product(vec1, vec2):
    """
    Computes the cross product of two 3-dimensional vectors.

    Parameters:
    vec1 (array-like): The first vector.
    vec2 (array-like): The second vector.

    Returns:
    numpy.ndarray: The cross product of vec1 and vec2.
    """
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    
    # Ensure that both vectors are 3-dimensional
    if vec1.shape != (3,) or vec2.shape != (3,):
        raise ValueError("Both input vectors must be 3-dimensional.")
    
    return np.cross(vec1, vec2)

# Example usage:
# vec1 = [1, 2, 3]
# vec2 = [4, 5, 6]
# result = compute_cross_product(vec1, vec2)
# print(result)  # Output: [-3  6 -3]
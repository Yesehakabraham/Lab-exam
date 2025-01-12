import numpy as np

def reconstruct_matrix(U, S, V):
    """
    Reconstructs a matrix from its SVD components.

    Parameters:
    U (numpy.ndarray): The left singular vectors matrix.
    S (numpy.ndarray): The diagonal matrix of singular values.
    V (numpy.ndarray): The right singular vectors matrix.

    Returns:
    numpy.ndarray: The reconstructed original matrix.
    """
    # Ensure S is a 2D diagonal matrix
    if S.ndim == 1:
        S = np.diag(S)
    
    # Reconstruct the matrix
    A_reconstructed = np.dot(U, np.dot(S, V))
    return A_reconstructed

# Example usage:
# U = np.array([[1, 0], [0, 1], [0, 0]])
# S = np.array([5, 0])
# V = np.array([[1, 0], [0, 1]])
# reconstructed_matrix = reconstruct_matrix(U, S, V)
# print(reconstructed_matrix)
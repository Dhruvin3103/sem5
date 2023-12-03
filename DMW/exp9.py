import numpy as np

def hits_algorithm(adjacency_matrix, max_iter=100, tol=1e-6):
    """
    Compute hub and authority scores using the HITS algorithm.

    Parameters:
    - adjacency_matrix: The adjacency matrix of the directed graph.
    - max_iter: Maximum number of iterations.
    - tol: Tolerance to determine convergence.

    Returns:
    - hub_scores: Array of hub scores for each node.
    - authority_scores: Array of authority scores for each node.
    """

    num_nodes = len(adjacency_matrix)
    hub_scores = np.ones(num_nodes)
    authority_scores = np.ones(num_nodes)

    for _ in range(max_iter):
        # Update authority scores
        new_authority_scores = np.dot(adjacency_matrix.T, hub_scores)
        # Update hub scores
        new_hub_scores = np.dot(adjacency_matrix, new_authority_scores)

        # Normalize scores
        new_authority_scores /= np.linalg.norm(new_authority_scores, 2)
        new_hub_scores /= np.linalg.norm(new_hub_scores, 2)

        # Check for convergence
        if np.sum(np.abs(new_authority_scores - authority_scores)) < tol and \
           np.sum(np.abs(new_hub_scores - hub_scores)) < tol:
            break

        authority_scores = new_authority_scores
        hub_scores = new_hub_scores

    return hub_scores, authority_scores

# Example graph represented by an adjacency matrix
# Node order: A, B, C, D
graph_matrix = np.array([
    [0, 0, 0, 1, 0, 0, 0, 0],  # A -> D
    [0, 0, 1, 0, 1, 0, 0, 0],  # B -> E, C
    [1, 0, 0, 0, 0, 0, 0, 0],  # C -> A
    [0, 0, 1, 0, 0, 0, 0, 0],  # D -> C
    [0, 1, 1, 1, 0, 1, 0, 0],  # E -> B, C, D, F
    [0, 0, 1, 0, 0, 0, 0, 1],  # F -> C, H
    [1, 0, 0, 0, 0, 0, 1, 0],  # G -> A, C
    [1, 0, 0, 0, 0, 0, 0, 0],  # H -> A
])

hub_scores, authority_scores = hits_algorithm(graph_matrix)

# Print results
print("Hub Scores:", hub_scores)
print("Authority Scores:", authority_scores)

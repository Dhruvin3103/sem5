import numpy as np

def page_rank_algorithm(graph, damping_factor):
    nodes = list(graph.keys())
    num_nodes = len(nodes)
    outgoing = {node: 0 for node in nodes}
    incoming_nodes = {node: [] for node in nodes}
    coefficients = {node: [0] * num_nodes for node in nodes}
    for i, node in enumerate(nodes):
        for neighbor in graph[node]:
            outgoing[node] += 1
    for i, node in enumerate(nodes):
        for neighbor in graph[node]:
            incoming_nodes[neighbor].append(node)
    for i, node in enumerate(nodes):
        for j, other_node in enumerate(nodes):
            if other_node in incoming_nodes[node]:
                coefficients[node][j] = damping_factor * (1.0 / outgoing[other_node])
            elif node == other_node:
                coefficients[node][j] = -1
    coefficients_list = [coefficients[node] for node in nodes]
    constant_matrix = [damping_factor - 1] * num_nodes
    pageranks = np.linalg.solve(np.array(coefficients_list), np.array(constant_matrix))
    print()
    for i, rank in enumerate(pageranks):
        print('Page Rank of {} is {:.4f}'.format(nodes[i], rank))

def main(graph):
    d = float(input('Enter the damping factor: '))
    page_rank_algorithm(graph, d)

graph = {'A': ['B', 'C'],'B': ['C'],'C': ['A'],'D': ['C']}
main(graph)
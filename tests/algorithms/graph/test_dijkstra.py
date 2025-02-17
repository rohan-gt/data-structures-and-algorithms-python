import pytest

from algorithms.graph.dijkstra import dijkstra


def test_dijkstra():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'D': 2, 'E': 5},
        'C': {'A': 4, 'F': 3},
        'D': {'B': 2},
        'E': {'B': 5, 'F': 1},
        'F': {'C': 3, 'E': 1}
    }
    distances = dijkstra(graph, 'A')
    assert distances == {'A': 0, 'B': 1, 'C': 4, 'D': 3, 'E': 6, 'F': 5}
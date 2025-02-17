import pytest

from algorithms.graph.bfs import bfs


def test_bfs(capsys):
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    bfs(graph, 'A')
    captured = capsys.readouterr()
    assert captured.out == "A B C D E F "
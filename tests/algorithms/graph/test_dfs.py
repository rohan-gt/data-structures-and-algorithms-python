import pytest

from algorithms.graph.dfs import dfs


def test_dfs(capsys):
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    dfs(graph, 'A')
    captured = capsys.readouterr()
    assert captured.out == "A B D E F C "
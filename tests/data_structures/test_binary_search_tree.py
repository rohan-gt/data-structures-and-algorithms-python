from data_structures.binary_search_tree import BinarySearchTree


def test_bst_operations() -> None:
    """
    Test basic operations of the BinarySearchTree class.
    """
    bst = BinarySearchTree()

    # Test traversals and search on an empty tree
    assert bst.inorder_traversal() == []
    assert bst.search(1) is False

    # Insert elements into the binary search tree
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    # Test traversals and search on a non-empty tree
    assert bst.inorder_traversal() == [2, 3, 4, 5, 6, 7, 8]
    assert bst.search(4) is True
    assert bst.search(10) is False

    # Test deletion of elements
    bst.delete(3)
    assert bst.inorder_traversal() == [2, 4, 5, 6, 7, 8]

    bst.delete(5)
    assert bst.inorder_traversal() == [2, 4, 6, 7, 8]

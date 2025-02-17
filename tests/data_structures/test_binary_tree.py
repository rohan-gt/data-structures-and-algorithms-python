from data_structures.binary_tree import BinaryTree


def test_binary_tree_operations() -> None:
    """
    Test basic operations of the BinaryTree class.
    """
    bt = BinaryTree()

    # Test traversals and height on an empty tree
    assert bt.inorder_traversal() == []
    assert bt.preorder_traversal() == []
    assert bt.postorder_traversal() == []
    assert bt.level_order_traversal() == []
    assert bt.height() == -1

    # Insert elements into the binary tree
    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)

    # Test traversals and height on a non-empty tree
    assert bt.inorder_traversal() == [4, 2, 5, 1, 3]
    assert bt.preorder_traversal() == [1, 2, 4, 5, 3]
    assert bt.postorder_traversal() == [4, 5, 2, 3, 1]
    assert bt.level_order_traversal() == [1, 2, 3, 4, 5]
    assert bt.height() == 2

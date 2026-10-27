"""Build a binary tree without recursion (variant 3)."""

from collections import deque
from typing import Callable, Optional


def gen_bin_tree(
    height: int = 4,
    root: int = 3,
    left_leaf: Optional[Callable[[int], int]] = None,
    right_leaf: Optional[Callable[[int], int]] = None,
) -> dict:
    """Return a binary tree with ``height`` levels.

    Each node is a dictionary with keys ``value``, ``left`` and ``right``.
    The left and right values are child nodes, or ``None`` on the last level.
    Variant 3 uses left = parent + 2 and right = parent * 3 by default.

    Args:
        height: Number of levels; must be at least 1.
        root: Value of the root node.
        left_leaf: Function computing a left child's value.
        right_leaf: Function computing a right child's value.

    Raises:
        ValueError: If ``height`` is less than 1.
    """
    if height < 1:
        raise ValueError("height must be at least 1")

    if left_leaf is None:
        left_leaf = lambda value: value + 2
    if right_leaf is None:
        right_leaf = lambda value: value * 3

    tree = {"value": root, "left": None, "right": None}
    queue = deque([(tree, 1)])

    while queue:
        node, level = queue.popleft()
        if level < height:
            node["left"] = {"value": left_leaf(node["value"]), "left": None, "right": None}
            node["right"] = {"value": right_leaf(node["value"]), "left": None, "right": None}
            queue.append((node["left"], level + 1))
            queue.append((node["right"], level + 1))

    return tree


def tree_as_dict_of_lists(tree: dict) -> dict[str, list]:
    """Show an alternative tree storage: paths mapped to child values.

    The empty path is the root. ``L`` and ``R`` describe turns from the root.
    Paths distinguish nodes even when different nodes have the same value.
    """
    result = {}
    queue = deque([(tree, "")])

    while queue:
        node, path = queue.popleft()
        children = []
        for side, letter in (("left", "L"), ("right", "R")):
            child = node[side]
            if child is not None:
                children.append(child["value"])
                queue.append((child, path + letter))
        result[path] = [node["value"], children]

    return result


if __name__ == "__main__":
    example = gen_bin_tree()
    print("Root:", example["value"])
    print("Left child:", example["left"]["value"])
    print("Right child:", example["right"]["value"])
    print("Alternative storage:", tree_as_dict_of_lists(example))

"""Tests for the iterative binary tree builder."""

import unittest

from binary_tree import gen_bin_tree, tree_as_dict_of_lists


class TestBinaryTree(unittest.TestCase):
    """Check default values, overrides, structure and error handling."""

    def test_variant_3_defaults(self):
        tree = gen_bin_tree()
        self.assertEqual(tree["value"], 3)
        self.assertEqual(tree["left"]["value"], 5)
        self.assertEqual(tree["right"]["value"], 9)
        self.assertEqual(tree["left"]["left"]["value"], 7)
        self.assertEqual(tree["left"]["right"]["value"], 15)

    def test_height_four_has_four_levels(self):
        queue = [(gen_bin_tree(), 1)]
        deepest_level = 0
        node_count = 0
        while queue:
            node, level = queue.pop(0)
            node_count += 1
            deepest_level = max(deepest_level, level)
            for side in ("left", "right"):
                if node[side] is not None:
                    queue.append((node[side], level + 1))
        self.assertEqual(deepest_level, 4)
        self.assertEqual(node_count, 15)

    def test_height_one_has_only_root(self):
        self.assertEqual(
            gen_bin_tree(height=1),
            {"value": 3, "left": None, "right": None},
        )

    def test_all_parameters_can_be_changed(self):
        tree = gen_bin_tree(
            height=2,
            root=10,
            left_leaf=lambda value: value - 1,
            right_leaf=lambda value: value + 1,
        )
        self.assertEqual(tree["left"]["value"], 9)
        self.assertEqual(tree["right"]["value"], 11)

    def test_one_default_function_can_be_kept(self):
        tree = gen_bin_tree(height=2, root=4, left_leaf=lambda value: value * 2)
        self.assertEqual(tree["left"]["value"], 8)
        self.assertEqual(tree["right"]["value"], 12)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            gen_bin_tree(height=0)

    def test_alternative_storage(self):
        result = tree_as_dict_of_lists(gen_bin_tree(height=2))
        self.assertEqual(result[""], [3, [5, 9]])
        self.assertEqual(result["L"], [5, []])
        self.assertEqual(result["R"], [9, []])


if __name__ == "__main__":
    unittest.main()

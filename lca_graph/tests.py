#!/usr/bin/env python

from lca_graph.main import Node, find_lca
import unittest


class LCAFinderTestCase(unittest.TestCase):
    def setUp(self):
        super(LCAFinderTestCase, self).setUp()

        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)
        self.root.left.left.left = Node(8)
        self.root.left.left.right = Node(9)

    def test_find_lca(self):
        self.assertEqual(find_lca(self.root, 3, 5).key, 1)
        self.assertEqual(find_lca(self.root, 7, 8).key, 1)
        self.assertEqual(find_lca(self.root, 6, 7).key, 3)

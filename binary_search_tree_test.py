import unittest
from binary_search_tree import *

class TestLab5(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    
    def test_insert1(self):
        bst = BinarySearchTree()    
        bst.insert(1, 1)
        self.assertEqual(bst.root.data, 1)
        bst.insert(2, 2)
        self.assertEqual(bst.root.right,TreeNode(2, 2, None, None))
        bst.insert(.5, .5)
        self.assertEqual(bst.root.left, TreeNode(.5, .5, None, None))
        bst.insert(1.5, 1.5)
        self.assertEqual(bst.root.right.left, TreeNode(1.5, 1.5, None, None))


    def test_findmax_1(self):
        bst = BinarySearchTree()
        bst.insert(20, 20)
        bst.insert(10, 10)
        bst.insert(30, 30)
        bst.insert(13, 13)
        bst.insert(7, 7)
        bst.insert(21, 21)
        bst.insert(35, 35)
        bst.insert(2, 2)
        bst.insert(8, 8)
        self.assertEqual(bst.find_max(), (35, 35))


    def test_findmin_1(self):
        bst = BinarySearchTree()
        bst.insert(20, 20)
        bst.insert(10, 10)
        bst.insert(30, 30)
        bst.insert(13, 13)
        bst.insert(7, 7)
        bst.insert(21, 21)
        bst.insert(35, 35)
        bst.insert(2, 2)
        bst.insert(8, 8)
        self.assertEqual(bst.find_min(), (2, 2))    

    def test_search1(self):
        bst = BinarySearchTree()
        bst.insert(20, 20)
        bst.insert(10, 10)
        bst.insert(30, 30)
        bst.insert(13, 13)
        bst.insert(7, 7)
        bst.insert(21, 21)
        bst.insert(35, 35)
        bst.insert(2, 2)
        bst.insert(8, 8)
        self.assertTrue(bst.search(7))    

    def test_search2(self):
        bst = BinarySearchTree()
        bst.insert(20, 20)
        bst.insert(10, 10)
        bst.insert(30, 30)
        bst.insert(13, 13)
        bst.insert(7, 7)
        bst.insert(21, 21)
        bst.insert(35, 35)
        bst.insert(2, 2)
        bst.insert(8, 8)
        self.assertFalse(bst.search(34)) 

    def test_height1(self):
        bst = BinarySearchTree()
        bst.insert(20, 20)
        bst.insert(10, 10)
        bst.insert(30, 30)
        bst.insert(13, 13)
        bst.insert(7, 7)
        bst.insert(21, 21)
        bst.insert(35, 35)
        bst.insert(2, 2)
        bst.insert(8, 8)
        self.assertEqual(bst.tree_height(), 3) 

    def test_preorder1(self):
        bst = BinarySearchTree()
        bst.insert(20, 20)
        bst.insert(10, 10)
        bst.insert(30, 30)
        bst.insert(13, 13)
        bst.insert(7, 7)
        bst.insert(21, 21)
        bst.insert(35, 35)
        bst.insert(2, 2)
        bst.insert(8, 8)
        self.assertEqual(bst.preorder_list(),[20, 10, 7, 2, 8, 13, 30, 21, 35] ) 

    def test_inorder1(self):
        bst = BinarySearchTree()
        bst.insert(20, 20)
        bst.insert(10, 10)
        bst.insert(30, 30)
        bst.insert(13, 13)
        bst.insert(7, 7)
        bst.insert(21, 21)
        bst.insert(35, 35)
        bst.insert(2, 2)
        bst.insert(8, 8)
        self.assertEqual(bst.inorder_list(),[2, 7, 8, 10, 13, 20, 21, 30, 35] ) 

    def test_levelorder1(self):
        bst = BinarySearchTree()
        bst.insert(20, 20)
        bst.insert(10, 10)
        bst.insert(30, 30)
        bst.insert(13, 13)
        bst.insert(7, 7)
        bst.insert(21, 21)
        bst.insert(35, 35)
        bst.insert(2, 2)
        bst.insert(8, 8)
        self.assertEqual(bst.level_order_list(),[20, 10, 30, 7, 13, 21, 35, 2, 8] ) 


    
    
if __name__ == '__main__': 
    unittest.main()

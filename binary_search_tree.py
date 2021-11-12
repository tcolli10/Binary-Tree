from queue_array import Queue

# from _typeshed import Self


class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def hasleft(self):
        return self.left
    
    def hasright(self):
        return self.right

    def __eq__(self, o: object) -> bool:
        return self.key == o.key and self.data == o.data and self.left == o.left and self.right == o.right

class BinarySearchTree:

    def __init__(self): 
        # Returns empty BST
        self.root = None
        self.num_items = 0

    def is_empty(self): 
        # returns True if tree is empty, else False
        if self.num_items == 0:
            return True
        else:
            return False

    def search(self, key): 
        # returns True if key is in a node of the tree, else False
        if self.is_empty():
            return False
        else:
            return self.search_middle(key, self.root)


    def search_middle(self, key, current_node):
        if key < current_node.key:
            if current_node.hasleft():
                return self.search_middle(key, current_node.left)
            else:
                return False
        elif key > current_node.key:
            if current_node.hasright():
                return self.search_middle(key, current_node.right)
            else: 
                return False
        else:
            return True

    

    def insert(self, key, data=None): 
        # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        if self.is_empty():
            self.root = TreeNode(key, data)
            self.num_items += 1
        else:
            self.insert_middle(key, data, self.root)

    def insert_middle(self, key, data, current_node):
        if key > current_node.key:
            if current_node.hasright():
                self.insert_middle(key, data, current_node.right)
            else:
                current_node.right = TreeNode(key, data)
                self.num_items += 1
        elif key < current_node.key:
            if current_node.hasleft():
                self.insert_middle(key, data, current_node.left)
            else:
                current_node.left = TreeNode(key, data)
                self.num_items += 1

    def find_min(self): 
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        else:
            current = self.root
            while current.hasleft():
                current = current.left
            return (current.key, current.data)
                

    def find_max(self): 
        # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        else:
            current = self.root
            while current.hasright():
                current = current.right
            return (current.key, current.data)

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.is_empty():
            return None
        else:
            return self.height(self.root)

    def height(self, current_node):
        if current_node is None:
            return -1
        else:
            left_height = self.height(current_node.left)
            rigt_height = self.height(current_node.right)
            return max(left_height, rigt_height) + 1

        
    def inorder_list(self): 
        # return Python list of BST keys representing in-order traversal of BST
        # DON'T use a default list parameter
        if self.root:
            return self.inorder(self.root, [])

    def inorder(self, current_node, traversal):
        if current_node.left is not None:
            traversal = self.inorder(current_node.left, traversal)
        traversal += [current_node.key]
        if current_node.right is not None:
            traversal = self.inorder(current_node.right, traversal)
        return traversal

    def preorder_list(self):  
        # return Python list of BST keys representing pre-order traversal of BST
        # DON'T use a default list parameter
        if self.root:
            return self.preorder(self.root, [])

    def preorder(self, current_node, traversal):
        traversal += [current_node.key]
        if current_node.left is not None:
            traversal = self.preorder(current_node.left, traversal)
        if current_node.right is not None:
            traversal = self.preorder(current_node.right, traversal)
        return traversal
        
        
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        # DON'T attempt to use recursion
        q = Queue(25000) # Don't change this!
        q.enqueue(self.root)
        answer = []
        
        while q.size() > 0:
            size = q.size()
            current_list = []
            top = q.headcheck()
            if size > 0:
                if top.hasleft():
                    q.enqueue(top.left)
                    size += 1
                if top.hasright():
                    q.enqueue(top.right)
                    size += 1                     
                removed = q.dequeue()
                current_list.append(removed.key)
                size -= 1
            answer += (current_list)
        return answer

        

# bst = BinarySearchTree() 
# bst.insert(20, 20)
# bst.insert(10, 10)
# bst.insert(30, 30)
# bst.insert(13, 13)
# bst.tree_height()


bst = BinarySearchTree()
bst.insert(20, 20)
bst.insert(10, 10)
bst.insert(30, 30)
bst.insert(13, 13)
bst.level_order_list()
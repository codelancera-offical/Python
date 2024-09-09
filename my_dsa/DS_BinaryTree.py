from my_dsa.DS_Queue import *

class BinaryTree():
    
    def __init__(self, root_obj):
        self._key = root_obj
        self._left_child = None
        self._right_child = None

    # Basic operations
    def get_root_obj(self):
        return self._key

    def set_root_obj(self, obj) -> bool:
        self._key = obj
        return True

    def get_left_child(self):
        return self._left_child
    
    def set_left_child(self, new_node):
        self._left_child = new_node

    def get_right_child(self):
        return self._right_child
    
    def set_right_child(self, new_node):
        self._right_child = new_node

    def insert_left(self, obj):
        if self._left_child is None:
            self._left_child = BinaryTree(obj)
        else:
            new_child = BinaryTree(obj)
            new_child._left_child = self._left_child  # insert a node and push the existing child down one level in the tree.
            self._left_child = new_child

    def insert_right(self, obj):
        if self._right_child is None:
            self._right_child = BinaryTree(obj)
        else:
            new_child = BinaryTree(obj)
            new_child._right_child = self._right_child
            self._right_child = new_child

    key = property(get_root_obj, set_root_obj)
    right_child = property(get_right_child, set_right_child)
    left_child = property(get_left_child, set_left_child)

    # Algorithms
    def traverse(self, order='level'):
        if order == 'level':
            q = Queue()
            key_list = []
            q.enqueue(self)

            while not q.is_empty():
                node = q.dequeue()
                if node != None:
                    key_list.append(node.key)
                    q.enqueue(node.left_child)
                    q.enqueue(node.right_child)
            
            return key_list
        
        elif order == "pre":
            def preorder(node) -> list:
                if node is None:
                    return []
                return [node.key] + preorder(node.left_child) + preorder(node.right_child)
            
            return preorder(self)
        
        elif order == "post":
            def postorder(node) -> list:
                if node is None:
                    return []
                return postorder(node.left_child) + postorder(node.right_child) + [node.key]
            
            
            return postorder(self)
        
        elif order == "in":
            def inorder(node) -> list:
                if node is None:
                    return []
                return inorder(node.left_child) + [node.key] + inorder(node.right_child)
            
            return inorder(self)

                



    

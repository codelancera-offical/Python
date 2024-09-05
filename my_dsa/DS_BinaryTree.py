class BinaryTree():
    
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None


    def get_root_obj(self):
        return self.key

    def set_root_obj(self, obj) -> bool:
        self.key = obj
        return True

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def insert_left(self, obj):
        if self.left_child is None:
            self.left_child = BinaryTree(obj)
        else:
            new_child = BinaryTree(obj)
            new_child.left_child = self.left_child  # insert a node and push the existing child down one level in the tree.
            self.left_child = new_child


    def insert_right(self, obj):
        if self.right_child is None:
            self.right_child = BinaryTree(obj)
        else:
            new_child = BinaryTree(obj)
            new_child.right_child = self.right_child
            self.left_child = new_child

    


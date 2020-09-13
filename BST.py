class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BST():
    def __init__(self, value):
        self.head = Node(value)
        self.head.left = None
        self.head.right = None
    
    def insert(self, value):
        current_node = self.head
        while True:
            if value < current_node.value:
                if current_node.left != None:
                    current_node = current_node.left
                else:
                    current_node.left = Node(value)
                    return
            else:
                if current_node.right != None:
                    current_node = current_node.right
                else:
                    current_node.right = Node(value)
                    return

    def bsf(self):
        node_queue = [self.head]
        result = []
        while node_queue:
            current_node = node_queue.pop(0)
            if current_node.left:
                node_queue.append(current_node.left)
            if current_node.right:
                node_queue.append(current_node.right)
            result.append(current_node.value)
        return result

    def dsf(self):
        result = []
        self.__dsf_rec(self.head, result)
        return result

    def __dsf_rec(self, current_node, result):
        result.append(current_node.value)        
        if current_node.left != None:
            self.__dsf_rec(current_node.left, result)
        if current_node.right != None:
            self.__dsf_rec(current_node.right, result)


xx = BST(12)
for i in [8, 14, 4, 10, 13, 15, 1, 17, 20]:
    xx.insert(i)
# print(xx.head.value)
# print(xx.head.left.value)
# print(xx.head.right.value)
print("BSF: ", xx.bsf())
print("DSF: ", xx.dsf())
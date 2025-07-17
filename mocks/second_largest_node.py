class ListNode:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None

class List:
    def __init__(self):
        self.root = None
# takes in number, asked to find second largest in tree if it exists else
# return None
def findSecondLargest(self, num):
    current = self.root
    result = -1
    while(current):
        if(current.key<num):
            result = current.key
            current = current.right
        else:
            current = current.left
    return result


def insert(self, num):
    if self.root is None:
        self.root = ListNode(num)
        return
    currentNode = self.root
    newNode = self.num
    while(currentNode):
        if newNode.key < currentNode.key:
            if currentNode.left is None:
                currentNode.left = newNode
                newNode.parent = currentNode
            else:
                currentNode = currentNode.left
        else:
            if currentNode.right is None:
                currentNode.right = newNode
                newNode.parent = currentNode
            else:
                currentNode = currentNode.right

            
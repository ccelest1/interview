from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        newNode = Node(val)
        if not self.root:
            self.root = newNode
            return self

        def inserted(val, current=self.root):
            if val == current.val:
                current.count += 1
                return self
            else:
                if val > current.val:
                    if current.right:
                        inserted(val, current.right)
                    else:
                        current.right = newNode
                elif val < current.val:
                    if current.left:
                        inserted(val, current.left)
                    else:
                        current.left = newNode
            return self

        return inserted(val)

    def delete(self, val):
        if not self.root:
            return

        def deleteNode(val, current):
            # if no current
            if not current:
                return
            # if val is less than current
            if val > current.val:
                current.right = deleteNode(current.right)
            if val < current.val:
                current.left = deleteNode(current.left)

            if val == current.val:
                if current.count > 1:
                    current.count -= 1
                    return
                elif not current.right and not current.left:
                    return None
                elif not current.right or not current.left:
                    if current.right:
                        child = current.right
                    else:
                        child = current.left
                    return child
                elif current.left and current.right:
                    minR = current.right
                    while minR.left:
                        minR = minR.left
                    current.value = minR.value
                    current.count = minR.count
                    return deleteNode(minR.value, current.right)

        self.root = deleteNode(val, self.root)
        return self

    def search(self, val):
        # ask if root
        if not self.root:
            return

        # helper
        def search_forNode(val, current=self.root):
            if val == current.val:
                return current
            elif val > current.val:
                return search_forNode(current.right)
            elif val < current.val:
                return search_forNode(current.left)

        # invoke helper with search value
        return search_forNode(val)

    def bfs(self):
        q = deque()
        nodes = []
        current = self.root
        q.append(current)

        def bfs_traverse(queue):
            if not queue:
                return
            currentNode = queue.popleft()
            nodes.push(currentNode)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        bfs_traverse(q)
        return nodes

    def dfs_pre(self):
        nodes = []
        current = self.root

        def dfsp_traverse(current):
            if not current:
                return nodes
            nodes.push(current.value)
            if current.left:
                dfsp_traverse(current.left)
            if current.right:
                dfsp_traverse(current.right)

        dfsp_traverse(current)
        return nodes

    def dfs_in(self):
        pass

    def dfs_post(self):
        pass


Btree = BST()
print(Btree.root)
Btree.insert(0)
print(Btree.root.val)
Btree.insert(1)
print(Btree.root.right.val)
Btree.insert(-1)
print(Btree.root.left.val)

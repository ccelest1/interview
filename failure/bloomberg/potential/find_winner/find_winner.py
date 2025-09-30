"""

        There are n friends that are playing a game
        Friends sit in circle numbered from 1 to n in clockwise order
        Moving clockwise from ith friend brings you to (i+1th) friend for 1<= i < n and moving clockwise from nth friend brings you to 1st friend

        Rules:
         1. start at 1st friend
         2. count next k friends in clockwise direction including friend I started @ -> counting wraps around circle and may include fiends more than once
         3. last friend counted leaves circle and loses game
         4. if there is more than 1 friend in circle, go to step 2 starting from friend immediately clockwise or friend who just lost and repeat
         5. else, lsat friend in circle wins game

         Given number of friends `n` and integer `k` return winner of game

         n%k -> remainder of spots
         ex: if k%n = friend position, nodes where we Node(val, prev, next)
         Example with 5 friends (1->5), Node(1) -> Node(1).prev = Node(5), Node(1).next = Node(2) -> ... -> node(5), Node(5).prev = Node(4), Node(5).nex = Node(1)

            class Node:
                def __init__(self, val, next=None, prev=None):
                    self.val = val
                    self.next = next
                    self.prev = prev

            class CircleLL:
                def __init__(self, first=None, length):
                    self.first = first
                    self.last = self.first
                    self.friends = friends

            class Solution:
                def findWinner(self, n:int, k:int) -> int:

                    def CircleDoubleLL(members):
                        currentCircle = CircleLL()
                        currentCircle.friends = members
                        if not currentCircle.first: currentCircle.first = Node(1)
                        currentNode = currentCircle.first
                        for member in range(len(members)):
                            newNode = Node(members[member])
                            if member is not len(members):
                                currentNode.next = newNode
                                currentNode = newNode
                            else:
                                currentNode.next = currentCircle.first


                    def NodeDeletion(self, Node, )
                        if not Node.prev and not Node.next:
                            return None

                    CircleDoubleLL(n)

"""


class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class CircleLL:
    def __init__(self, first=None):
        self.first = first
        self.last = self.first
        self.friends = None


class Solution:
    def findWinner(self, n: int, k: int) -> int:

        def CircleDoubleLL(members):
            currentCircle = CircleLL()
            currentCircle.friends = members
            if not currentCircle.first:
                currentCircle.first = Node(1)
            currentNode = currentCircle.first
            for member in range(len(members)):
                newNode = Node(members[member])
                if member is not len(members):
                    currentNode.next = newNode
                    currentNode = newNode
                else:
                    currentNode.next = currentCircle.first

        FriendsCircle = CircleDoubleLL(n)

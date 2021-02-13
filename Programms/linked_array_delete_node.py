class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        
        if self.nodeCount == 1 :
            curr = self.head
            self.head = None   # 빈 linkedlist 된 것 head 및 tail이 none인 것으로 설명!
            self.tail = None
        elif pos == 1:
            curr = self.head
            self.head = self.head.next
        else:
            prev = self.getAt(pos - 1)
            curr = prev.next
            if pos == self.nodeCount:
                prev.next = None  # 이걸 지정해줘야 tail 된것 완벽히 반영된 것!
                self.tail = prev
            else:
                prev.next = curr.next
        self.nodeCount += (-1)
        return curr.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0
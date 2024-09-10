class Node:
    def __init__(self, val=None, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head: 'Node') -> 'Node':
    if not head:
        return None

    dummy = Node(0)
    dummy.next = head
    prev = dummy

    stack = []
    curr = head

    while curr:
        if curr.child:
            if curr.next:
                stack.append(curr.next)

            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None

        prev = curr
        curr = curr.next

        if not curr and stack:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev

    dummy.next.prev = None
    return dummy.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.child = Node(4)
head.next.child.next = Node(5)
head.next.next.next = Node(6)
head.next.next.next.child = Node(7)

flat_head = flatten(head)

curr = flat_head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next

print("None")
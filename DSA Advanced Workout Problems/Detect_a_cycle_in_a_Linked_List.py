class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):

    slow = head
    fast = head

    while fast != None and fast.next != None:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Create nodes
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

# Create a cycle
head.next.next.next.next = head.next

print(has_cycle(head))
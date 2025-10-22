class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next  # referencia al siguiente nodo
        self.prev = prev

    def __str__(self):
        return f"Node({self.data!r})"
    


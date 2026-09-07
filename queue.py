class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            print(f"Enqueued: {data}")
            return

        self.rear.next = new_node
        self.rear = new_node
        print(f"enqueued: {data}")

    def dequeue(self):
        if self.is_empty():
            print("queue underflow!")
            return None

        dequeued_data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        return dequeued_data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def display(self):
        curr = self.front
        elements =[]
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print("queue (front -> rear): " + "->" .join(elements))

if __name__ == "__main__":
    queue = queue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    queue.display()
    print("dequeued:", queue.dequeue())
    queue.display()
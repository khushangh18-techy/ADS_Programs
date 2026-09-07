class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class FoodQueue:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def reverse_list(self, head_node):
        """Reverses a singly linked list and returns the new head."""
        prev = None
        curr = head_node
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def distribute_food(self):
        if not self.head or not self.head.next:
            print("Queue processing complete.")
            return

        # 1. Find the middle using Slow & Fast pointers
        slow = self.head
        fast = self.head
        prev_slow = None

        while fast and fast.next:
            fast = fast.next.next
            prev_slow = slow
            slow = slow.next

        # 2. Split into two halves
        prev_slow.next = None  # Cut the first half
        first_half = self.head
        second_half = slow

        # 3. Reverse the second half
        second_half = self.reverse_list(second_half)

        # 4. Process/Display distribution from both trucks simultaneously
        print("\n--- Food Distribution Started ---")
        p1 = first_half
        p2 = second_half
        truck_1_count = 1
        truck_2_count = 1

        while p1 or p2:
            if p1:
                print(f"Truck 1 (Front) serves Person: {p1.data}")
                p1 = p1.next
            if p2:
                print(f"Truck 2 (Back)  serves Person: {p2.data}")
                p2 = p2.next


# --- Test Execution
queue = FoodQueue()

# Queue of 6 people: Person 1 to Person 6
for person in range(1, 11):
    queue.append(f"Person {person}")

queue.distribute_food()

#1
#Give a python code to generate  a Stack class with push, pop, peek, and is_empty methods.
#Sample Input Code:
#class Stack:
#pass
#Expected Output:A functional stack implementation with all required methods and docstrings
class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """
        Remove and return the item at the top of the stack.
        Raises an exception if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """
        Return the item at the top of the stack without removing it.
        Raises an exception if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        return len(self.items) == 0


# Example usage:
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())       # Output: 3
    print(s.pop())        # Output: 3
    print(s.is_empty())   # Output: False
    print(s.pop())        # Output: 2
    print(s.pop())        # Output: 1
    print(s.is_empty())   # Output: True





#2
#give a python code  to implement a Queue using Python lists.
#Sample Input Code:
#class Queue:#pass
#Expected Output:
#FIFO-based queue class with enqueue, dequeue, peek, and size methods.
class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the item at the front of the queue.
        Raises an exception if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        """
        Return the item at the front of the queue without removing it.
        Raises an exception if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self.items) == 0
# Example usage:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.peek())       # Output: 1
    print(q.dequeue())    # Output: 1
    print(q.size())       # Output: 2
    print(q.dequeue())    # Output: 2
    print(q.dequeue())    # Output: 3
    print(q.is_empty())   # Output: True






#3
# give a python codeto generate a Singly Linked List with insert and display methods.
#Sample Input Code:
#class Node:pass
#class LinkedList:pass
#Expected Output:A working linked list implementation with clear method documentation.
class Node:
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def insert(self, data):
        """Insert a new node with the given data at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        """Display the contents of the linked list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    linked_list.display()  # Output: 10 -> 20 -> 30 -> None
    



#4
# give a python codeto generate a Singly Linked List with insert and display methods.
#Sample Input Code:
#class Node:pass
#class LinkedList:pass
#Expected Output:A working linked list implementation with clear method documentation.
class Node:
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def insert(self, data):
        """Insert a new node with the given data at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        """Display the contents of the linked list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    linked_list.display()  # Output: 10 -> 20 -> 30 -> None
    



#5
#give a python  to implement a hash table with basic insert, search, and delete methods.
#Sample Input Code:
#class HashTable:
#pass
#Expected Output:Collision handling using chaining, with well-commented methods.
class HashTable:
    def __init__(self, size=10):
        """Initialize the hash table with a specified size."""
        self.size = size
        self.table = [[] for _ in range(size)]  # Create a list of empty lists for chaining

    def _hash(self, key):
        """Generate a hash for the given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        # Check if the key already exists and update it
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update existing key
                return
        # If the key does not exist, add a new key-value pair
        self.table[index].append((key, value))

    def search(self, key):
        """Search for a value by its key in the hash table."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v  # Return the value if the key is found
        return None  # Return None if the key is not found

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  # Remove the key-value pair
                return True  # Return True if deletion was successful
        return False  # Return False if the key was not found
# Example usage:
if __name__ == "__main__":
    ht = HashTable()
    ht.insert("name", "Alice")
    ht.insert("age", 30)
    print(ht.search("name"))  # Output: Alice
    print(ht.search("age"))   # Output: 30
    print(ht.delete("name"))  # Output: True
    print(ht.search("name"))  # Output: None
    print(ht.delete("name"))  # Output: False
    print(ht.delete("age"))   # Output: True
    print(ht.search("age"))   # Output: None
    



#6
#give a python code to implement a graph using an adjacency list.
#Sample Input Code:
#class Graph:
#pass
#Expected Output:Graph with methods to add vertices, add edges, and display connections.
class Graph:
    def __init__(self):
        """Initialize an empty graph using an adjacency list."""
        self.graph = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Add an edge between two vertices in the graph."""
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph

    def display(self):
        """Display the adjacency list of the graph."""
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {', '.join(edges)}")
# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.display()
    # Output:
    # A: B, C
    # B: A, D
    # C: A, D
    # D: B, C
    

#7
#give a python code to implement a priority queue using Python’s heapq module.
#Sample Input Code:
#class PriorityQueue:
#pass
#Expected Output:Implementation with enqueue (priority), dequeue (highest priority),and display methods.
import heapq
class PriorityQueue:
    def __init__(self):
        """Initialize an empty priority queue."""
        self.elements = []

    def enqueue(self, item, priority):
        """Add an item to the priority queue with the given priority."""
        heapq.heappush(self.elements, (priority, item))

    def dequeue(self):
        """
        Remove and return the item with the highest priority (lowest priority number).
        Raises an exception if the priority queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty priority queue")
        return heapq.heappop(self.elements)[1]

    def peek(self):
        """
        Return the item with the highest priority without removing it.
        Raises an exception if the priority queue is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        return self.elements[0][1]

    def size(self):
        """Return the number of items in the priority queue."""
        return len(self.elements)

    def is_empty(self):
        """Return True if the priority queue is empty, False otherwise."""
        return len(self.elements) == 0

    def display(self):
        """Display the contents of the priority queue."""
        for priority, item in sorted(self.elements):
            print(f"Priority: {priority}, Item: {item}")
# Example usage:
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue("Task 1", priority=3)
    pq.enqueue("Task 2", priority=1)
    pq.enqueue("Task 3", priority=2)
    pq.display()
    # Output:
    # Priority: 1, Item: Task 2
    # Priority: 2, Item: Task 3
    # Priority: 3, Item: Task 1
    print(pq.dequeue())  # Output: Task 2
    print(pq.peek())     # Output: Task 3





#8
#generate a python code  to implement a double-ended queue usingcollections.deque.
#Sample Input Code:
#class DequeDS:
#pass
#Expected Output:Insert and remove from both ends with docstrings.
from collections import deque
class DequeDS:
    def __init__(self):
        """Initialize an empty double-ended queue."""
        self.deque = deque()

    def add_front(self, item):
        """Add an item to the front of the deque."""
        self.deque.appendleft(item)

    def add_rear(self, item):
        """Add an item to the rear of the deque."""
        self.deque.append(item)

    def remove_front(self):
        """
        Remove and return the item at the front of the deque.
        Raises an exception if the deque is empty.
        """
        if self.is_empty():
            raise IndexError("remove from empty deque")
        return self.deque.popleft()

    def remove_rear(self):
        """
        Remove and return the item at the rear of the deque.
        Raises an exception if the deque is empty.
        """
        if self.is_empty():
            raise IndexError("remove from empty deque")
        return self.deque.pop()

    def peek_front(self):
        """
        Return the item at the front of the deque without removing it.
        Raises an exception if the deque is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty deque")
        return self.deque[0]

    def peek_rear(self):
        """
        Return the item at the rear of the deque without removing it.
        Raises an exception if the deque is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty deque")
        return self.deque[-1]

    def is_empty(self):
        """Return True if the deque is empty, False otherwise."""
        return len(self.deque) == 0
# Example usage:
if __name__ == "__main__":
    d = DequeDS()
    d.add_rear(1)
    d.add_rear(2)
    d.add_front(0)
    print(d.peek_front())  # Output: 0
    print(d.peek_rear())   # Output: 2
    print(d.remove_front()) # Output: 0
    print(d.remove_rear())  # Output: 2
    print(d.is_empty())     # Output: False
    print(d.remove_front()) # Output: 1
    print(d.is_empty())     # Output: True
    



#9
#generate a pyhton code with the scenario:Your college wants to develop a Campus Resource Management Systemthat handles:
#1. Student Attendance Tracking – Daily log of studentsentering/exiting the campus.
#2. Event Registration System – Manage participants in events with quick search and removal.
#3. Library Book Borrowing – Keep track of available books and theirdue dates.
#4. Bus Scheduling System – Maintain bus routes and stopconnections.
#5. Cafeteria Order Queue – Serve students in the order they arrive. 
# Student Task:For each feature, select the most appropriate data structure fromthe list below:Stack,Queue,Priority Queue.Linked List.Binary Search Tree (BST),Graph,Hash Table,Deque
#• Justify your choice in 2–3 sentences per feature.
#• Implement one selected feature as a working Python program with AI-assisted code generation.
#Expected Output:• A table mapping feature → chosen data structure → justification.,A functional Python program implementing the chosen feature with comments and docstrings.
#give a python codeto implement the Cafeteria Order Queue using a Queue data structure.
from collections import deque

class CafeteriaQueue:
    """
    A class to represent the cafeteria order queue.
    Students are served in the order they arrive (FIFO).
    """

    def __init__(self):
        """Initialize an empty queue using deque."""
        self.queue = deque()

    def add_order(self, student_name):
        """
        Add a student's order to the queue.
        
        Args:
            student_name (str): Name of the student placing the order.
        """
        self.queue.append(student_name)
        print(f"Order added for {student_name}")

    def serve_order(self):
        """
        Serve the next student in line.
        
        Returns:
            str: Name of the student whose order is served.
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("No orders to serve!")
        student = self.queue.popleft()
        print(f"Order served for {student}")
        return student

    def peek_next(self):
        """
        View the next student to be served without removing them.
        
        Returns:
            str: Name of the student at the front of the queue.
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("No orders in queue!")
        return self.queue[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0


# Example usage:
if __name__ == "__main__":
    cafeteria = CafeteriaQueue()
    cafeteria.add_order("Alice")
    cafeteria.add_order("Bob")
    cafeteria.add_order("Charlie")

    print("Next to be served:", cafeteria.peek_next())  # Output: Alice
    cafeteria.serve_order()  # Serves Alice
    cafeteria.serve_order()  # Serves Bob
    print("Is queue empty?", cafeteria.is_empty())      # Output: False
    cafeteria.serve_order()  # Serves Charlie
    print("Is queue empty?", cafeteria.is_empty())      # Output: True




#10
# generate a python code for the Smart E-Commerce Platform – Data Structure Challenge
#An e-commerce company wants to build a Smart Online Shopping System with:
#1. Shopping Cart Management – Add and remove products dynamically.
#2. Order Processing System – Orders processed in the order they are placed.
#3. Top-Selling Products Tracker – Products ranked by sales count.
#4. Product Search Engine – Fast lookup of products using product ID.
#5. Delivery Route Planning – Connect warehouses and delivery locations.
#Student Task:• For each feature, select the most appropriate data structure from the list below:
#Stack
#Queue
#Priority Queue
#Linked List
#Binary Search Tree (BST)
#Graph
#Hash Table
#Deque
# Justify your choice in 2–3 sentences per feature.
#Implement one selected feature as a working Python program with AI-assisted code generation.
#Expected Output:• A table mapping feature → chosen data structure → justification.
#• A functional Python program implementing the chosen feature with comments and docstrings
#give a python code  to implement the Top-Selling Products Tracker using a Priority Queue data structure.
import heapq
class TopSellingProductsTracker:
    """
    A class to track top-selling products using a priority queue.
    Products are ranked by their sales count, with the highest sales having the highest priority.
    """

    def __init__(self):
        """Initialize an empty priority queue and a dictionary to store product sales."""
        self.product_sales = {}
        self.priority_queue = []

    def record_sale(self, product_id):
        """
        Record a sale for a product and update the priority queue.
        
        Args:
            product_id (str): The ID of the product sold.
        """
        # Update sales count
        if product_id in self.product_sales:
            self.product_sales[product_id] += 1
        else:
            self.product_sales[product_id] = 1
        
        # Update the priority queue
        heapq.heappush(self.priority_queue, (-self.product_sales[product_id], product_id))

    def get_top_selling_products(self, n=5):
        """
        Get the top N selling products.
        
        Args:
            n (int): The number of top-selling products to return. Default is 5.
        
        Returns:
            List of tuples: A list of (product_id, sales_count) for the top N products.
        """
        top_products = []
        seen = set()
        
        while self.priority_queue and len(top_products) < n:
            sales_count, product_id = heapq.heappop(self.priority_queue)
            if product_id not in seen:
                seen.add(product_id)
                top_products.append((product_id, -sales_count))
        
        return top_products
# Example usage:
if __name__ == "__main__":
    tracker = TopSellingProductsTracker()
    tracker.record_sale("product_1")
    tracker.record_sale("product_2")
    tracker.record_sale("product_1")
    tracker.record_sale("product_3")
    tracker.record_sale("product_2")
    tracker.record_sale("product_2")
    
    print(tracker.get_top_selling_products())  # Output: [('product_2', 3), ('product_1', 2), ('product_3', 1)]


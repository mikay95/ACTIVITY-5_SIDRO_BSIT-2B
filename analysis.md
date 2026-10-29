# Module 5 Analysis Questions

### Question 1: Why does a linked-list stack push and pop at the head instead of the tail?
In a singly linked list, inserting or deleting at the **head** only requires updating a couple of pointer references (`node.next = self.top` and `self.top = node`), which executes in strict $O(1)$ constant time. Conversely, if operations were performed at the **tail**, popping would require traversing the entire linked list to update the second-to-last node's `next` pointer to `None`, degrading the performance of `pop()` to $O(n)$ linear time.

### Question 2: Why must an array-based queue be circular?
In a naive array implementation of a queue, calling `dequeue()` advances the `front` index forward. Over time, empty space accumulates at the beginning of the array while the `rear` index reaches the end, falsely reporting a queue overflow despite available space. Alternative approaches, such as shifting all remaining elements to index 0 after every `dequeue()`, result in inefficient $O(n)$ operations. A circular queue uses modulo arithmetic (`(index + 1) % capacity`) to wrap indices around to index 0, allowing front slots to be reused efficiently while maintaining $O(1)$ constant time for both `enqueue()` and `dequeue()`.

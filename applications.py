from structures import LinkedStack, LinkedQueue

def check_balanced_parentheses(expr: str) -> bool:
    """6a. Checks whether parentheses, brackets, and braces in a string are balanced."""
    stack = LinkedStack()
    matching_map = {')': '(', ']': '[', '}': '{'}

    for char in expr:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != matching_map[char]:
                return False

    return stack.is_empty()


class PrintJob:
    def __init__(self, job_id, page_count):
        self.job_id = job_id
        self.page_count = page_count

    def __repr__(self):
        return f"Job[{self.job_id} ({self.page_count} pages)]"


def simulate_print_queue():
    """6b. Simulates a print queue processing jobs in FIFO order."""
    queue = LinkedQueue()
    
    # Enqueue print jobs
    jobs = [PrintJob("Doc_1", 5), PrintJob("Doc_2", 12), PrintJob("Doc_3", 3)]
    print("--- Enqueuing Print Jobs ---")
    for order, job in enumerate(jobs, start=1):
        queue.enqueue(job)
        print(f"Enqueued: {job} | Position in wait line: {order}")

    print("\n--- Processing Print Jobs (FIFO Order) ---")
    wait_order = 1
    while not queue.is_empty():
        job = queue.dequeue()
        print(f"Processing Wait #{wait_order}: Printing {job}...")
        wait_order += 1


if __name__ == "__main__":
    print("=== 6a. Balanced Parentheses Test ===")
    test_strings = ["({[]})", "({[})", "((()))", "(()"]
    for s in test_strings:
        result = check_balanced_parentheses(s)
        print(f"Expression: {s:<10} | Balanced: {result}")

    print("\n=== 6b. Print Queue Simulation ===")
    simulate_print_queue()

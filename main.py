from structures import ArrayStack, LinkedStack, ArrayQueue, LinkedQueue

def run_menu():
    print("=== Data Structure Demonstration Program ===")
    print("1. ArrayStack")
    print("2. LinkedStack")
    print("3. ArrayQueue (Circular)")
    print("4. LinkedQueue")
    choice = input("Select implementation (1-4): ").strip()

    ds = None
    if choice == "1":
        cap = int(input("Enter ArrayStack capacity: "))
        ds = ArrayStack(cap)
    elif choice == "2":
        ds = LinkedStack()
    elif choice == "3":
        cap = int(input("Enter ArrayQueue capacity: "))
        ds = ArrayQueue(cap)
    elif choice == "4":
        ds = LinkedQueue()
    else:
        print("Invalid choice.")
        return

    is_stack = choice in ["1", "2"]

    while True:
        print(f"\nCurrent State: {ds.display()}")
        if is_stack:
            print("1. Push  2. Pop  3. Peek  4. Exit")
        else:
            print("1. Enqueue  2. Dequeue  3. Peek Front  4. Exit")
            
        op = input("Choose operation (1-4): ").strip()
        try:
            if op == "1":
                val = input("Enter value: ")
                if is_stack:
                    ds.push(val)
                else:
                    ds.enqueue(val)
            elif op == "2":
                removed = ds.pop() if is_stack else ds.dequeue()
                print(f"--> Removed item: {removed}")
            elif op == "3":
                top_val = ds.peek() if is_stack else ds.peek_front()
                print(f"--> Front/Top item: {top_val}")
            elif op == "4":
                break
            else:
                print("Invalid option.")
        except (IndexError, OverflowError) as e:
            print(f"ERROR: {e}")

if __name__ == "__main__":
    run_menu()

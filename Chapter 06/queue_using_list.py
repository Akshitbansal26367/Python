l1 = []
print(f"1.Enqueue {'':<8} 2.Dequeue {'':<8} 3.Display First Element {'':<8} 4.Display Last Element {'':<8} 5.Display "
      f"Queue {'':<8} 6.Exit")
while True:
    c = int(input("\nEnter the choice : "))
    if c == 1:
        n = input("Enter value to be pushed: ")
        l1.append(n)
    elif c == 2:
        if len(l1) == 0:
            print("Queue is Empty")
        else:
            del l1[0]
    elif c == 3:
        if len(l1) == 0:
            print("Queue is Empty")
        else:
            print("First Queue Element is", l1[0])
    elif c == 4:
        if len(l1) == 0:
            print("Queue is Empty")
        else:
            print("Last Queue Element is", l1[-1])
    elif c == 5:
        print("The Queue is", l1)
    elif c == 6:
        break
    else:
        print("Invalid Output")

l1 = []
print(f"1.Push {'':<8} 2.Pop {'':<8} 3.Peek {'':<8} 4.Display Stack {'':<8} 5.Exit")
while True:
    c = int(input("\nEnter the choice : "))
    if c == 1:
        n = input("Enter value to be pushed: ")
        l1.append(n)
    elif c == 2:
        if len(l1) == 0:
            print("Stack is Empty")
        else:
            l1.pop()
    elif c == 3:
        if len(l1) == 0:
            print("Stack is Empty")
        else:
            print("Top Element is", l1[-1])
    elif c == 4:
        print("The list is", l1)
    elif c == 5:
        break
    else:
        print("Invalid Output")

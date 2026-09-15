import udf

while True:
    print("*" * 40)
    print("1. odd even")
    print("2. max of two")
    print("3. max of three")
    print("4. prime")
    print("5. fibonacci")
    print("6. exit")
    print("*" * 40)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number: "))
        udf.oddeven(n)

    elif choice == 2:
        n1 = int(input("Enter number: "))
        n2 = int(input("Enter number: "))
        udf.maxoftwo(n1, n2)

    elif choice == 3:
        n1 = int(input("Enter number: "))
        n2 = int(input("Enter number: "))
        n3 = int(input("Enter number: "))
        udf.maxofthree(n1, n2, n3)

    elif choice == 4:
        n = int(input("Enter number: "))
        udf.prime(n)

    elif choice == 5:
        n = int(input("Enter number: "))
        udf.fibonacci(n)

    elif choice == 6:
        print("Thank you for using our services")
        break

    else:
        print("Invalid choice. Please try again.")

    print("*" * 40)

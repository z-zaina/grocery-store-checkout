milk_price = 3
bread_price = 2
eggs_price = 4

total = 0

while True:
    print("\nGROCERY STORE")
    print("1 - Milk ($3)")
    print("2 - Bread ($2)")
    print("3 - Eggs ($4)")
    print("4 - Checkout")

    choice = input("Select Item: ")

    if choice == "1":
        total = total + milk_price
        print("Milk Added!")

    elif choice == "2":
        total = total + bread_price
        print("Bread Added!")

    elif choice == "3":
        total = total + eggs_price
        print("Eggs Added!")

    elif choice == "4":
        print("\nCHECKOUT")
        print("Total Cost: $", total)

        if total >= 20:
            discount = total * 0.10
            total = total - discount
            print("10% Discount Applied!")

        print("Final Total: $", total)
        print("Thank You For Shopping!")
        break

    else:
        print("Invalid Selection!")

def main():
    print("A survey of lunch menu")
    menu_items = ["Pizza", "Hot Dog", "Ham", "Cheese"]
    votes = [[0, 0], [0, 0], [0, 0], [0, 0]]

    while True:
        for i in range(len(menu_items)):
            ans = input(f"Do you like {menu_items[i]} (y/n)? ")
            if ans.lower() == "y":
                votes[i][0] += 1
            else:
                votes[i][1] += 1

        cont = input("Do you have another student (y/n)? ")
        if cont.lower() == "n":
            break

    # Print the results in a tabular format
    print("Survey Results:")
    print("-" * 25)
    print("{:<10} {:<10} {:<10}".format("Item", "Like", "Dislike"))
    print("-" * 25)
    for i in range(len(menu_items)):
        print("{:<10} {:<10} {:<10}".format(menu_items[i], votes[i][0], votes[i][1]))
    print("-" * 25)

if __name__ == "__main__":
    main()
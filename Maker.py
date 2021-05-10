items = []

def itemEntry(Number_of_items : int, List : list):
    for x in range(Number_of_items):
        item = str(input("Enter item: "))
        List.append(item)

def MakeList():
    listTitle = str(input("Title of list: "))
    numofitems = int(input("Number of items: "))
    itemEntry(numofitems, items)

    f = open(listTitle + ".txt", "w")
    for i in range(numofitems):
        f.write("- " + items[i] + "\n")

def Add_To_List():
    nameOfList = str(input("Name of list to add: "))
    Num_of_items = int(input("Number of items to add: "))
    itemEntry(Num_of_items, items)

    add = open(nameOfList + ".txt", "a+")
    for i in range(Num_of_items):
        add.write("- " + items[i] + "\n")

print("To add items to a list, type 1 and to make a new list, type 2.")
choice = int(input("1/2: "))
if choice == 1:
    Add_To_List()

elif choice == 2:
    MakeList()

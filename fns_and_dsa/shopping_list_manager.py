Shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Prompt for and add an item
            item = input ("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been aded to your shopping list." )
            
        elif choice == '2':
            # Prompt for and remove an item
            item=input ("Enter item to be removed: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed.")
            else:
                print(f"'{item}' is not in your shopping list")  
            
            
        elif choice == '3':
            # Display the shopping list
            
            print (shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
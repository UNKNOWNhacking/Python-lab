class Library:
    def __init__(self):
        self.items = []

    def add_item(self, title, author):
        unique_id = len(self.items) + 1
        item = {
            'id': unique_id,
            'title': title,
            'author': author
        }
        self.items.append(item)
        print(f"Item '{title}' by {author} added with ID {unique_id}")

    def remove_item(self, item_id):
        for item in self.items:
            if item['id'] == item_id:
                self.items.remove(item)
                print(f"Item with ID {item_id} removed.")
                return
        print(f"Item with ID {item_id} not found.")

    def display_items(self):
        if not self.items:
            print("The library is empty.")
        else:
            print("Library Items:")
            for item in self.items:
                print(
                    f"ID: {item['id']}, Title: {item['title']}, Author: {item['author']}")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Items")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter item title: ")
            author = input("Enter author: ")
            library.add_item(title, author)
        elif choice == '2':
            item_id = int(input("Enter item ID to remove: "))
            library.remove_item(item_id)
        elif choice == '3':
            library.display_items()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

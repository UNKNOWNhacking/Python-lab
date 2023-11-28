class Car:
    def __init__(self):
        self.components = []

    def add_component(self, component_name, component_type):
        component = (component_name, component_type)
        self.components.append(component)
        print(f"Added {component_type} component: {component_name}")

    def display_components(self):
        if not self.components:
            print("No components added to the car.")
        else:
            print("Car Components:")
            for component in self.components:
                component_name, component_type = component
                print(f"Type: {component_type}, Name: {component_name}")


def main():
    car = Car()

    while True:
        print("\nCar Component Management System")
        print("1. Add Component")
        print("2. Display Components")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            component_name = input("Enter component name: ")
            component_type = input("Enter component type: ")
            car.add_component(component_name, component_type)
        elif choice == '2':
            car.display_components()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

class BuildingConstruction:
    def __init__(self):
        self.materials = []

    def add_material(self, material_name, quantity, unit):
        material = (material_name, quantity, unit)
        self.materials.append(material)
        print(f"Added {quantity} {unit} of {material_name}")

    def display_materials(self):
        if not self.materials:
            print("No materials added for construction.")
        else:
            print("Materials Required for Construction:")
            for material in self.materials:
                material_name, quantity, unit = material
                print(f"{quantity} {unit} of {material_name}")


def main():
    construction = BuildingConstruction()

    while True:
        print("\nBuilding Construction Material Management System")
        print("1. Add Material")
        print("2. Display Materials")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            material_name = input("Enter material name: ")
            quantity = float(input("Enter quantity: "))
            unit = input("Enter unit (e.g., bags, tons, etc.): ")
            construction.add_material(material_name, quantity, unit)
        elif choice == '2':
            construction.display_materials()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

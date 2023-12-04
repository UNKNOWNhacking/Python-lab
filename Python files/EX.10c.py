def get_valid_marks():
    while True:
        try:
            marks = float(input("Enter the marks: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks should be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for marks.")


# Initialize an empty dictionary to store student data
student_data = {}

# Get data for 10 students
for i in range(1, 6):
    print(f"\nEnter details for student {i}:")
    name = input("Enter the name: ")

    # Get and validate marks using the function
    marks = get_valid_marks()

    # Add data to the dictionary
    student_data[name] = marks

# Display the collected data
print("\nStudent data:")
for name, marks in student_data.items():
    print(f"{name}: {marks} marks")

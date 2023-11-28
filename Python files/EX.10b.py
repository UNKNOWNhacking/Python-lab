def get_voter_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 18:
                raise ValueError("You must be 18 or older to vote.")
            return age
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter a valid age as a positive integer.")


# Example usage
try:
    voter_age = get_voter_age()
    print(f"You are eligible to vote. Your age is {voter_age}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

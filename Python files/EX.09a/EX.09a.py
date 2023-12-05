with open("my_file.txt", "r") as first_file, open("my_file_1.txt", "a") as second_file:
    for line in first_file:
        second_file.write(line)

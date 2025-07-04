print("Today's sales report")

with open("my_file.txt", "r") as f:
    while True:
        line = f.readline()
        if line == "":
            break
        print(line, end="")

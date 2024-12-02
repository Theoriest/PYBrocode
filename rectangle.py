columns = int(input("please input the length of the rectangle in cm"))
rows = int(input("please input the width of the rectangle in cm"))
for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows - 1:
            print("-", end="")
        elif rows-1 > i > 0:
            if j == 0 or j == rows - 1:
                print("|", end="")
            else:
                print(" ", end="")
    print()

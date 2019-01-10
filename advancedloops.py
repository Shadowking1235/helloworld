def draw(rows, coloumns):
    for x in range(0, rows):
        if (x % 2 == 0):
            for y in range(1, coloumns + 1):
                if (y % 2 == 1):
                    if (y != coloumns):
                        print(" ", end='')
                    else:
                        print(" ")

                else:
                    print("|", end='')
        else:
            print("------")

draw(5,5)


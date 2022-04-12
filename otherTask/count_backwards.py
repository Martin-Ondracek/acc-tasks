for i in range(100, 0, -1):
    # i % 15 seems faster than 2 conditions
    if (i % 15 == 0):
        print("Testing")
    elif (i % 3 == 0):
        print("Software")
    elif (i % 5 == 0):
        print("Agile")
    else:
        print(i)



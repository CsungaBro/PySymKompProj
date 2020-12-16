# Gets
# Does
# Gives

def fivePrec(array):
    for i in range(len(array)):
        for j in range(len(array)):
            array[i][j] = format(array[i][j], ".5g")

# Gets
# Does
# Gives

def printHelper(text,thing):
    print("")
    print(text)
    print("\n")
    print(thing)
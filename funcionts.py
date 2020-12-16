def fivePrec(array):
    for i in range(len(array)):
        for j in range(len(array)):
            array[i][j] = format(array[i][j], ".5g")
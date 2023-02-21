def example():
    arr = [1, 5, -7, 13, 12, 11, 2, 47, 111, 0, -3, 22]

    cp1 = arr.copy()
    cp2 = arr.copy()

    cp1.sort(reverse=True)
    cp2.sort(key=lambda x: -x)

    print(cp1, cp2, f' equals(cp1, cp2) = {cp1 == cp2}', sep='\n')

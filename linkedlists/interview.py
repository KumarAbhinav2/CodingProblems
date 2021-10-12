

def everyThird(l):
    for i in range(0, len(l), 2):
        print(l[i])
    print([l[i] for i in range(0, len(l), 2)])
    print(l[::2])

everyThird([1, 2, 3, 4, 5,6, 7, 8, 9])

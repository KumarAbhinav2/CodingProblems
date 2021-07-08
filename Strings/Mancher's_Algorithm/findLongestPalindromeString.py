

def divideList(input_lst, n):
    span = len(input_lst)//n
    res = []
    for i in range(span):
        res.append(input_lst[:n])
        input_lst = input_lst[n:]
    return res


input = [1, 2, 3, 4, 5]
n = 2
divideList(input, n)

def runningTime(arr):

    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        shifts = 0
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
            shifts +=1
        print(shifts)
        arr[j+1] = key
    return arr

runningTime([2,1,3,1,2])


def quickSort(arr):
    pivot = arr[0]
    left, right, equal = [], [pivot], []
    for i in arr[1:]:
        if i > pivot:
            right.append(i)
        elif i < pivot:
            left.append(i)
        else:
            equal.append(i)
    print(*left, *equal, *right)

quickSort([4,5,3,7,2])

def countingSort(arr):
    new_arr = []
    frequency_arr = [0]*100
    for i in arr:
        frequency_arr[i] += 1
    while frequency_arr:
        i = 0
        elem = frequency_arr.pop(0)
        while elem:
            new_arr.append(arr[i])
            elem -= 1
        i += 1
    return new_arr

a = ['63', '25', '73', '1', '98', '73', '56', '84', '86', '57', '16', '83', '8', '25', '81', '56', '9', '53', '98',
     '67', '99', '12', '83', '89', '80', '91', '39', '86', '76', '85', '74', '39', '25', '90', '59', '10', '94', '32',
     '44', '3', '89', '30', '27', '79', '46', '96', '27', '32', '18', '21', '92', '69', '81', '40', '40', '34', '68',
     '78', '24', '87', '42', '69', '23', '41', '78', '22', '6', '90', '99', '89', '50', '30', '20', '1', '43', '3',
     '70', '95', '33', '46', '44', '9', '69', '48', '33', '60', '65', '16', '82', '67', '61', '32', '21', '79', '75',
     '75', '13', '87', '70', '33']

countingSort(a)
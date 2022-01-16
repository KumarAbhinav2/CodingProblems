def check(arr, n):
    # To store the number of modifications
    # required to make the array
    # strictly increasing
    modify = 0

    # Check whether the first element needs
    # to be modify or not
    if (arr[0] > arr[1]):
        arr[0] = arr[1] // 2
        modify += 1

    # Loop from 2nd element to the 2nd last element
    for i in range(1, n - 1):

        # Check whether arr[i] needs to be modified
        if ((arr[i - 1] < arr[i] and arr[i + 1] < arr[i])
                or (arr[i - 1] > arr[i] and arr[i + 1] > arr[i])):

            # Modifying arr[i]
            arr[i] = (arr[i - 1] + arr[i + 1]) // 2

            # Check if arr[i] is equal to any of
            # arr[i-1] or arr[i+1]
            if (arr[i] == arr[i - 1] or arr[i] == arr[i + 1]):
                return False

            modify += 1

    # Check whether the last element needs
    # to be modify or not
    if (arr[n - 1] < arr[n - 2]):
        modify += 1

    # If more than 1 modification is required
    if (modify > 1):
        return False

    return True


# Driver code
if __name__ == "__main__":
    arr = [1,1,1]
    n = len(arr)

    if (check(arr, n)):
        print("Yes")
    else:
        print("No")
def linsearch(arr, n, target):
    right = n
    left = 0

    while left < right:
        # comparing with every element with target number
        if arr[left] == target:
            # if found return index number
            return left
        left += 1
    # if not found return -1
    return -1


if __name__ == "__main__":
    n = int(input("Enter the size of array: "))
    arr = [0] * n
    for i in range(n):
        print("Enter data for index ", str(i), " :", end=" ")
        arr[i] = int(input())

    target = int(input("Enter the number you want to search: "))
    res = linsearch(arr, n, target)
    if res == -1:
        print("Element is not found in array.")
    else:
        print("Element is found at index ", str(res))

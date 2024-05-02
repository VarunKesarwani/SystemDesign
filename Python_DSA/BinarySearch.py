"""
Enter the sorted array to find the number in this example.
If array is not sorted result will not be accurate.
"""


def binarysearch(arr, n, target):
    left = 0
    right = n
    mid = left + (right-left)//2

    while left <= right:
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            # if target is higher searching in one half only
            # searching area reduced to half
            right = mid - 1
        elif arr[mid] < target:
            # if target is lower searching in another half only
            # searching area reduced to another half.
            left = mid + 1
    return -1


if __name__ == "__main__":
    n = int(input("Enter the size of array: "))
    arr = [0] * n
    for i in range(n):
        print("Enter data for index ", str(i), " :", end=" ")
        arr[i] = int(input())

    target = int(input("Enter the number you want to search: "))
    res = binarysearch(arr, n, target)
    if res == -1:
        print("Element is not found in array.")
    else:
        print("Element is found at index ", str(res))

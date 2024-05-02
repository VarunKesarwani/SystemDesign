"""
Enter the size of array: 5
Input : [1, 2, 3, 0, -2]
Output: [-2, 0, 1, 2, 3]
"""

# insertion sort for implementation
def insertion_sort(arr):
    # traversal of the array from index 1 to len(arr)
    for i in range(1, len(arr)):
        # key value to perform comparison with next elements of array
        key = arr[i]
        j = i-1
        # move all the elements which are greater than key value
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key


if __name__ == "__main__":
    arr = []
    n = int(input("Enter the size of array: "))
    # accept input only for valid values of n
    if n > 0:
        for i in range(n):
            print("Enter the value at index ", i, end=" : ")
            a = int(input())
            arr.append(a)

        insertion_sort(arr)
        print(arr)
    else:
        print("Enter valid value for array size.")
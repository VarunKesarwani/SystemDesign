"""
Enter the size of array: 5
Input : [1, 2, 3, 0, -2]
Output: [-2, 0, 1, 2, 3]
"""
# conquering function  after dividing the problems into sub-problems.
# this function will do the comparison and merge sorted arrays
def merge(arr, left, mid_idx, right):

    n1 = mid_idx-left+1
    n2 = right-mid_idx
    # temp arrays to store the values
    left_arr = [0] * (n1)
    right_arr = [0] * (n2)

    for i in range(0, n1):
        left_arr[i] = arr[left+i]

    for j in range(0, n2):
        right_arr[j] = arr[mid_idx+1+j]

    i = 0  # index of first sub array
    j = 0  # index of second sub array
    k = left  # initial index of merged sub-array

    # do the comparison till sub-arrays are exhausted
    while i < n1 and j < n2:
        # condition to store the value in the output array
        # if true place element from left sub-array
        if left_arr[i] <= right_arr[j]:

            arr[k] = left_arr[i]
            i += 1
        # if false place element from right sub-array
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    # if right array is exhausted move all the elements from left array
    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    # if left array is exhausted move all the elements from right array
    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        # find the middle element to divide the problem into two half
        mid_idx = (left+(right-1))//2
        # one half of sub-problem from left to mid index
        merge_sort(arr, left, mid_idx)
        # second half from mid index to right
        # conquering the array elements
        merge_sort(arr, mid_idx+1, right)
        merge(arr, left, mid_idx, right)


if __name__ == "__main__":
    arr = []
    # enter the size of array
    n = int(input("Enter the size of array: "))

    if n > 0:
        for i in range(n):
            print("Enter the value at index ", i, end=" : ")
            a = int(input())
            arr.append(a)
        merge_sort(arr, 0, n-1)
        print(arr)
    else:
        print("Enter valid number of array size.")
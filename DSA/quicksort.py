"""
Enter the size of array: 5
Input : [1, 2, 3, 0, -2]
Output: [-2, 0, 1, 2, 3]
"""
# function to divide the array between to part
# this will place the element where all the right will be greater
# all the left elements will be smaller

def part_element(arr, left, right):
    # smaller element index
    i = left-1
    # pivot
    pivot_ele = arr[right]

    for j in range(left, right):
        # if pivot is greater than current then
        if arr[j] <= pivot_ele:
            # increment the index and swap with smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    #
    arr[i+1], arr[right] = arr[right], arr[i+1]

    return i+1

# main function arr--> input array
# left --> start index
# right --> ending index


def quick_sort(arr, left, right):
    if len(arr) == 1:
        return arr
    if left < right:
        # partition index for after this arr{partition_idx}
        # will be at right place
        partition_idx = part_element(arr, left, right)
        # separately sort elements recursively
        quick_sort(arr, left, partition_idx-1)
        quick_sort(arr, partition_idx+1, right)


if __name__ == "__main__":
    arr = []
    n = int(input("Enter the size of array: "))
    # accept only valid values of n
    if n > 0:
        for i in range(n):
            print("Enter the value at index ", i, end=" : ")
            a = int(input())
            arr.append(a)

        quick_sort(arr, 0, n-1)

        print(arr)
    else:
        print("Enter valid number of array size.")
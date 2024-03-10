"""
Enter the size of array: 5
Input : [1, 2, 3, 0, -2]
Output: [-2, 0, 1, 2, 3]
"""
# main function for sorting
def selection_sort(arr, n):
    for i in range(n):
        # find the smallest element in the unsorted array
        smallest_val_idx=i
        for j in range(i+1, n):
            if arr[smallest_val_idx] > arr[j]:
                smallest_val_idx = j
        # swap the found element with first eleemnt
        arr[i], arr[smallest_val_idx] = arr[smallest_val_idx], arr[i]
    # return sorted array
    return arr


if __name__ == "__main__":
    number_arr = []
    n = int(input("Enter the size of array: "))
    if n > 0:
        for i in range(n):
            print("Enter the value at index ", i, end=" : ")
            a = int(input())
            number_arr.append(a)

        a = selection_sort(number_arr, n)

        print(a)
    else:
        print("Enter valid values of array.")


"""
Enter the size of array: 5
Input : [1, 2, 3, 0, -2]
Output: [-2, 0, 1, 2, 3]
"""

# function to sort number in increasing order

def bubble_sort(arr, n):
    # outer loop to go from (0 to n-1)
    for i in range(n-1):
        # inner loop which will place the largest number at the end of the array
        for j in range(n-i-1):
            # comparing arr[j] to arr[j+1] to perform the swap according to the condition
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    number_arr = []
    n = int(input("Enter the size of array: "))
    if n < 1:
        print("No sorting Needed. Please enter valid value of n.")
    else:
        for i in range(n):
            print("Enter the value at index ", i, end=" : ")
            a = int(input())
            # appending number in the input array.
            number_arr.append(a)
            # calling bubble sort function to do the sorting
            a = bubble_sort(number_arr, n)
            print(a)

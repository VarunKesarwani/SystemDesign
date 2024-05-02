"""
Enter number of elements in array: 5
Input : [2, 11, 2, 3, 4]
Median :  3.0
"""
def find_median(number, n):
    # sort the array by using in-built function
    arr = sorted(number)
    # check if number of elements in array is even or odd
    if n % 2 != 0:
        return float(arr[n//2])
    else:
        return float((arr[int((n-1)//2)]+arr[n//2])/2.0)


if __name__ == "__main__":
    number = []
    n = int(input("Enter number of elements in array: "))
    if n < 1:
        print("Enter valid value of n.")
    else:
        for i in range(n):
            print("Enter value at index ", i, ": ", end=" ")
            a = int(input())
            number.append(a)
        # function called to find the median value of sorted array
        val = find_median(number, n)
        print("Median of given array is : ", val)


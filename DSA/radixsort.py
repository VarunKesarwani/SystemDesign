# main function to implement the radix sort
"""
Enter the size of array: 8
Input : [170, 45, 75, 90, 802, 24, 2, 66]
Output: [2, 24, 45, 66, 75, 90, 170, 802]
"""
def radix_sort(arr):
    RADIX = 10
    max_len = False
    tmp, place = -1 , 1

    while not max_len:
        max_len = True
        # allocating buckets based on the radix value
        buckets = [list() for _ in range(RADIX)]
        for i in arr:
            # calculating tmp value
            tmp = i // place
            # insert element of arr in the bucket based on index calculated
            buckets[tmp % RADIX].append(i)

            if max_len and tmp > 0:
                max_len = False

        a = 0
        for b in range(RADIX):
            # place the bucket value based on the radix value calculated in earlier step
            buck = buckets[b]
            for i in buck:
                arr[a] = i
                a += 1
        # move to next digit
        place *= RADIX
    # Return the sorted array
    return arr


if __name__ == "__main__":
    arr = []
    n = int(input("Enter the size of array: "))
    # accept only if size greater than 0
    if n > 0:
        for i in range(n):
            print("Enter the value at index ", i, end=" : ")
            a = int(input())
            if a >= 0:
                arr.append(a)
            else:
                print("Enter positive number as entry. ")
        print("Sorted array is:")
        print(radix_sort(arr))
    else:
        print("Enter valid number of array size.")
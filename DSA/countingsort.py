"""
Enter the size of array: 7
Input : [1, 4, 1, 2, 7, 5, 2]
Output: [1, 1, 2, 2, 4, 7, 5]
"""
# this algorithm works well for positive number only

def count_sort(arr, max_val):

    counts = [0] * (max_val+1)
    for item in arr:
        counts[item] += 1
    num_item_before = 0

    for i, count in enumerate(counts):
        counts[i] = num_item_before
        num_item_before += count

    sorted_list = [None] * len(arr)
    for item in arr:
        sorted_list[counts[item]] = item
        counts[item] += 1

    return sorted_list


if __name__ == "__main__":
    arr = []
    n = int(input("Enter the size of array: "))
    # accept input only when array size is greater than 0
    if n > 0:
        for i in range(n):
            print("Enter the value at index ", i, end=" : ")
            a = int(input())
            if a >= 0:
                arr.append(a)
            else:
                print("Enter positive number as entry. ")
                while True:
                    a = int(input())
                    if a >= 0:
                        arr.append(a)
                        break
                    else:
                        continue

        max_ele = max(arr)
        # calling the function to implement count sort
        sorted_arr = count_sort(arr, max_ele)
        print(sorted_arr)
    else:
        print("Enter valid number of array size.")
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        half = len(arr) // 2
        return sorted_merge_arrays(
            merge_sort(arr[:half]),
            merge_sort(arr[half:])
        )


def sorted_merge_arrays(arr1, arr2):
    rez = []
    i = 0
    j = 0
    while True:
        if i == len(arr1):
            return rez + arr2[j:]
        if j == len(arr2):
            return rez + arr1[i:]
        if arr1[i] < arr2[j]:
            rez.append(arr1[i])
            i += 1
        else:
            rez.append(arr2[j])
            j += 1
        
    return rez


def main():
    # print(
    #     sorted_merge_arrays(
    #         [1, 3, 28, 99],
    #         [4, 5, 6, 29]
    #     )
    # )
    print(
        merge_sort([11, 18, 5, 4, 12, 15, 1, 13, 8, 16])
    )


if __name__ == "__main__":
    main()
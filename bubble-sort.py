
def bubble_sort(arr):
    print(arr)
    while True:
        changed = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                x = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = x
                changed = True
        if not changed: # break out of loop if nothing is switched
            break
    print(arr)


def main():
    bubble_sort(
        [2, 4, 6, 8, 1, 3, 5, 11]
    )
    bubble_sort([-3, 95, -4, 20, 5, 6, 8])


if __name__ == "__main__":
    main()
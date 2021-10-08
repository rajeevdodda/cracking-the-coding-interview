# https://www.techiedelight.com/find-minimum-number-merge-operations-make-array-palindrome/

# Find the minimum number of merge operations to make an array palindrome


def merge(array: list):
    i, j, count = 0, len(array) - 1, 0

    while i < j:
        if array[i] == array[j]:
            i += 1
            j -= 1
        elif array[i] < array[j]:
            array[i + 1] += array[i]
            count += 1
            i += 1
        else:
            array[j - 1] += array[j]
            count += 1
            j -= 1
    print(count)


merge([6, 1, 3, 7])
merge([6, 1, 4, 3, 1, 7])
merge([1, 2, 3, 3, 2, 1])

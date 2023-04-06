def first_bad_pair(sequence):
    """Return the first index of a pair of elements where the earlier
    element is not less than the later elements. If no such pair
    exists, return -1."""
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1

def almostIncreasingSequence(sequence):
    j = first_bad_pair(sequence)
    print(j)
    if j == -1:
        return True  # List is increasing
    if first_bad_pair(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True  # Deleting earlier element makes increasing
    if first_bad_pair(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True  # Deleting later element makes increasing
    return False  # Deleting either does not make increasing




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s=[10, 1, 2, 3, 4, 5]
    print(almostIncreasingSequence(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

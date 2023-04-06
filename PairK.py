def solution(a, k):
    freq = [0] * k
    n = len(a)

    # Count occurrences of all remainders
    for i in range(n):
        freq[a[i] % k] += 1

    # If both pairs are divisible by 'k'
    sum = freq[0] * (freq[0] - 1) / 2

    # count for all i and (k-i)
    # freq pairs
    i = 1
    while (i <= k // 2 and i != (k - i)):
        sum += freq[i] * freq[k - i]
        i += 1

    # If k is even
    if (k % 2 == 0):
        sum += (freq[k // 2] * (freq[k // 2] - 1) / 2)

    return int(sum)


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    print(solution(a, 3))





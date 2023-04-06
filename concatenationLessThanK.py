def solution(a,b,k):
    num = 0
    for i in range(len(a)):
        j = len(a)-1-i
        x = str(a[i])+str(b[j])
        if int(x)<k:
            num += 1
    return num

if __name__ == '__main__':
    a = [16, 1, 4, 2, 14]
    b = [7, 11, 2, 0, 15]
    print(solution(a,b,743))
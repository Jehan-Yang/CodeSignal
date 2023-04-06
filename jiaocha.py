def solution(a):
    b = []
    if len(a)%2 == 0:
        for i in range(int(len(a)/2)):
            b.append(a[i])
            b.append(a[len(a)-1-i])
    else:
        for i in range(int(len(a)/2)):
            b.append(a[i])
            b.append(a[len(a)-1-i])
        b.append(a[int(len(a)/2)])

    for i in range(len(b)-1):
        if(b[i]>=b[i+1]):
            return False
    return True


if __name__ == '__main__':
    a = [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]
    print(solution(a))





#竖着加
def solution2(m):
    r = len(m)
    c = len(m[0])
    total=0
    for j in range(c):
        for i in range(r):
            if m[i][j]!=0:
                total+=m[i][j]
            else:
                break
    return total

if __name__ == '__main__':
    matrix = [[0, 1, 1, 2],
              [0, 5, 0, 0],
              [2, 0, 3, 3]]
    print(solution2(matrix))


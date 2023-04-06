def solution(intervals, fees, deliveries):
    row = len(deliveries)
    list = []
    for i in range(len(intervals)):
        time0 = intervals[i]
        if i == len(intervals) - 1:
            time1 = 24
        else:
            time1 = intervals[i + 1]
        num = 0
        for j in range(row):
            if time0 <= deliveries[j][0] < time1:
                num += 1
        if fees[i] == 0:
            match = 0
        else:
            match = num / fees[i]
        list.append(match)

    for j in range(len(list) - 1):
        if list[j] != list[j + 1]:
            return False
    return True
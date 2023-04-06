import re
def solution(order, shoppers):
    distance0 = order[0]
    time = order[1]
    duration = order[2]

    num = len(shoppers)
    result = []
    for i in range(num):
        distance1 = shoppers[i][0]
        speed = shoppers[i][1]
        picking = shoppers[i][2]
        total = (distance0 + distance1) / speed + picking
        if time <= total <= time + duration:
            result.append(True)
        else:
            result.append(False)

    return result

if __name__ == '__main__':
    items = "Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4"
    x = (re.findall(r"\d+\.?\d*", items))
    sum = 0
    for i in x:
        sum += float(i)
    print(sum)
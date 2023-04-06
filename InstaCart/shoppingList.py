import re
def solution(items):
    x = (re.findall(r"\d+\.?\d*", items))
    sum = 0
    for i in x:
        sum += float(i)
    return sum
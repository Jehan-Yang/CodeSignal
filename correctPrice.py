def solution(product_name,product_price,product,price):
    dic = {}
    for i in range(len(product_name)):
        dic[product_name[i]] = product_price[i]

    for i in range(len(product)):
        if dic[product[i]]!=price[i]:
            return False
    return True

if __name__ == '__main__':
    product_name = ["egg", "milk", "water"]
    product_price = [10, 20, 5]
    product = ["egg", "egg", "water", "milk"]
    price = [10, 10, 5, 20]
    print(solution(product_name,product_price,product,price))
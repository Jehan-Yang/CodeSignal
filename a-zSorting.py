def solution(strings):
    letters = [0] * 26

    for i in strings:
        for j in i:
            letters[ord(j) - 97] += 1

    string = ''
    for i in range(len(letters)):
        if (letters[i] != 0):
            for j in range(letters[i]):
                string += chr(i + 97)
    return string

if __name__ == '__main__':
   strings = ['apple', 'banana', 'orange','kiwi']
   print(solution(strings))

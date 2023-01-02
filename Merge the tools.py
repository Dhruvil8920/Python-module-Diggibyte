def merge_the_tools(string, k):
    # your code goes here
    str_size = len(string)

    for i in range(0, str_size, k):
        word = ''

        for char in string[i: i + k]:
            if char not in word:
                word += char

        print(word)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
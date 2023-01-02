if __name__ == '__main__':
    N = int(input())
    a=[]
    for i in range(N):
        stri=input().split(" ")
        if stri[0]=="append":
            a.append(int(stri[1]))
        elif stri[0]=="print":
            print(a)
        elif stri[0]=="insert":
            a.insert(int(stri[1]),int(stri[2]))
        elif stri[0]=="remove":
            a.remove(int(stri[1]))
        elif stri[0]=="sort":
            a.sort()
        elif stri[0]=="pop":
            a.pop()
        elif stri[0]=="reverse":
            a.reverse()

def mutate_string(string, position, character):
    st1=list(string[0:position])
    st2=string[position+1:]
    st3=""
    st1.append(character)
    for i in st1:
        st3+=str(i)
    string=st3+st2
    return string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
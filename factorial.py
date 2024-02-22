l = [5, 7, 7, [2, 3, [3]]]
s = 0
for i in l:
    if type(i) == list:
        for ii in i:
            s += ii
    else:
        s += i
print(s)

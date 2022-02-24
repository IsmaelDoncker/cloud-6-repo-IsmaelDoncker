i = [33,12,11,8,5]
for x in range(len(i)):
    if i[x] == i[len(i)-1]:
        print(i[x] + i[0])
    else:
        print(i[x]+ i[x+1])
# 删除装备词典中带活动的装备(不在装备词典中展示)


filepath = "C:\\Users\\Spring\Desktop\\Script\\etc\\itemdictionary\\(r)itemdictionary.etc"
count = 0
text = ""
deltext = ""
dic = {}
lst1 = []
with open(filepath, 'r', encoding='UTF-8') as file:
    line = file.readline()

    while len(line)>0:
        ishd = line.find("活动")
        if ishd!=-1:
            count = count + 1
            # deltext = deltext+line
            dic[count]=line
            lst1.append(count)
            line = file.readline()
        else :
            # text=text+line
            count = count + 1
            dic[count]=line
            line = file.readline()
    # print(deltext)
    print(dic)

    newdic = {}
    lst = []
    # 遍历字典 后生成新字典
    for x in dic:
        if dic[x].find("活动")!=-1:
            x+=12

        else :
            lst.append(x)
        # print((x, newdic[x]))
    print(lst)

    count111 = 0
    for index in range(len(lst)):
        newdic[count111]=dic[index].strip("\n")

        print(newdic[count111])
        count111 = count111 + 1

    file = open("C:\\Users\\Spring\Desktop\\Script\\etc\\itemdictionary\\(r)itemdictionary.etc1", 'a',
                encoding='utf-8')
    file.write(newdic[count111])
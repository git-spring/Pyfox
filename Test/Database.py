import  re

count = 0
with open('APIsql.txt', 'r',encoding='utf8') as f:

    line = ' '
    set_database = set()
    while line:
        line = f.readline()
        count += 1
        res = line.split(' ')
        for word in res:
            word = str.lower(word)
            if word.find('tra')>=0:
                set_database.add(word)

            # database_table = re.findall(r'^\w+\.[a-zA-Z0-9]\S+', word)
            # if database_table:
            #     for ele in database_table:
            #         ele = str.lower(ele)
            #         set_database.add(ele)

print(set_database)
print(len(set_database))

with open('res.txt','w',encoding='utf8') as f:
    for ele in set_database:
        if 1 :
            f.write(ele)
            f.write('\n')
        # f.write(ele)
        # f.write('\n')
print(count)

s = set()
print(type(s))
num = -1
print(bool(num))



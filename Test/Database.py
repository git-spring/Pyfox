import  re,os

# path = 'F:\\code\\历史账单\\historyBill\\etl\\sql_template\\'
path = 'F:\\Python\\Pyfox\\sql_tem\\'
files = os.listdir(path)
print(files)
print(len(files))
count = 0
set_database = set()
for file in files:

    with open(path+file, 'r',encoding='utf8') as f:
        line = ' '

        while line:
            print(file)
            line = f.readline()
            count += 1
            res = line.split(' ')
            for word in res:
                word = str.lower(word)
                database_table = re.findall(r'^\w+\.\w\S+[a-zA-Z0-9]', word)
                if database_table:
                    for ele in database_table:
                        ele = str.lower(ele)
                        if ele.startswith("ods"):
                            # ele = ele+'\t\t\t\t\t\t------> '+file
                            set_database.add(ele)

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




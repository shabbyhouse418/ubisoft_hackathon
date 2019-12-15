import sqlite3
import math

def getData(filepath):
    data=[]
    conn = sqlite3.connect(filepath,check_same_thread=False)
    c = conn.cursor()
    cursor = c.execute("select * from class")

    for row in cursor:
        data.append(row)

    conn.close()
    return data

def takeSecond(elem):
    return elem[1]

def returnData(filepath,recommandList):
    print(recommandList)
    value=[]
    sum=0
    remainder=0
    for i in recommandList:
        temp=[i[0],math.modf(i[1]/3*5)]
        value.append(temp)
        sum+=temp[1][1]
        remainder+=temp[1][0]
    print(value)
    value.sort(key=takeSecond,reverse=True)

    sum2=0
    lack=40-int(sum)
    for i in range(8):
        a=list(value[i][1])
        a[1]+=int((a[0]/remainder)*lack)
        sum2+=int((a[0]/remainder)*lack)
        value[i][1]=tuple(a)

    print(value)
    for i in range(lack-int(sum2)):
        i=i%8
        a=list(value[i][1])
        a[1]+=1
        value[i][1] = tuple(a)
    
    # for i in range(32-int(sum)):
    #     i=i%8
    #     a=list(value[i][1])
    #     a[1]+=1
    #     value[i][1] = tuple(a)

    value.sort()
    v=[]
    for i in value:
        v.append(i[1][1])

    conn = sqlite3.connect(filepath)
    c = conn.cursor()
    sql = '''update INI_TABLE set 
            CLASS1 = ?,
            CLASS2 = ?,
            CLASS3 = ?,
            CLASS4 = ?,
            CLASS5 = ?,
            CLASS6 = ?,
            CLASS7 = ?,
            CLASS8 = ?'''
    values = (v)
    print(values)

    c.execute(sql,values)
    conn.commit()
    conn.close()
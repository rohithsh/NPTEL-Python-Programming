def fun1(list1):
    res = {}
    for items in list1:
        key,value = items.split("~")
        res[key] = value
    return res
    
def fun2(list1):
    res1,res2 = {},{}
    for items in list1:
        s,b,d = items.split("~")
        res1[b] = s
        if d in res2.keys():
            res2[d].append(b)
        else:
            res2[d] = [b]
    return res1,res2
    
x=input()
result = []
books,borrowers,checkout1,checkout2 = {},{},{},{}
flag1,flag2,flag3 = 0,0,0
while(flag3==0):
    temp1,temp2,temp3 = [],[],[]
    while(flag1==0):
        x = input()
        if(x=="Borrowers"):
            flag1 = 1
            break
        temp1.append(x)
    books = fun1(temp1)
    while(flag2==0):
        x = input()
        if(x=="Checkouts"):
            flag2 = 1
            break
        temp2.append(x)
    borrowers = fun1(temp2)
    while(flag3==0):
        x = input()
        if(x=="EndOfInput"):
            flag3 = 1
            break
        temp3.append(x)
    checkout1,checkout2 = fun2(temp3)
datelist = list(checkout2.keys())
for date in datelist:
    for book in checkout2[date]:
        result.append(date+"~"+borrowers[checkout1[book]]+"~"+book+"~"+books[book])
result.sort()
print(*result,sep="\n")

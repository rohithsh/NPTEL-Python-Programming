def addpoly(p1,p2):
    dict1 = {}
    dict2 = {}
    result = []
    temp_dict = {}
    for items in p1:
        dict1[items[1]] = items[0]
    for items in p2:
        dict2[items[1]] = items[0]
    for keys in list(dict1):
        if keys in list(dict2):
            temp = dict1[keys]+dict2[keys]
            if temp !=0:
                temp_dict[keys] = temp
            del dict1[keys]
            del dict2[keys]
                
    for keys in list(dict1):
        temp_dict[keys] = dict1[keys]
    for keys in list(dict2):
        temp_dict[keys] = dict2[keys]
    for i in list(reversed(sorted(temp_dict.keys()))):
        result.append((temp_dict[i],i))
    return result
  
def multpoly(p1,p2):
    try:
        dict1 = {}
        dict2 = {}
        result = []
        temp_result = []
        temp_dict = {}
        for items in p1:
            dict1[items[1]] = items[0]
        for items in p2:
            dict2[items[1]] = items[0]
        for i in list(dict2):
            for j in list(dict1):
                if not (i==0 or j==0):
                    temp_result.append([(dict2[i]*dict1[j],i+j)]);
                else:
                    temp_result.append([(dict2[i]*dict1[j],max(i,j))])
        i = 0
        while len(temp_result)>2:
           # print(i,len(temp_result))
            temp_result.append(addpoly(temp_result.pop(i),temp_result.pop(i+1)))
            i = i+1
            if i==(len(temp_result)-2):
                i = 0
        #print(temp_result)
        result = addpoly(temp_result[0],temp_result[1])
        return result
    except:
        return []
        
print(multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)]))

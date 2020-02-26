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


addpoly([(4,3),(3,0)],[(-4,3),(2,1)])

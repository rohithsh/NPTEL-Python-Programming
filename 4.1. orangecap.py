def orangecap(dict1):
    players = set()
    keys = []
    result= {}
    for key in dict1:
        keys.append(key)
        items = dict1[key]
        for key in items:
            players.add(key)
            result[key] = 0
    for j in keys:
       for k in dict1[j]:
           for p in players:
               if p==k:
                   result[p] += dict1[j][k]
    Keymax = max(result, key=result.get)
    return (Keymax,result[Keymax])

print(orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'Ashwin':59, 'Pujara':42}}))

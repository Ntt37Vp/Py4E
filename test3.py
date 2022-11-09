c = {'d':3, 'a':10, 'b':1, 'c':22}
tmp = list()

for k,v in c.items():
    tmp.append((v, k))

# print(tmp)
sort_tmp = sorted(tmp, reverse=True)
print(sort_tmp)

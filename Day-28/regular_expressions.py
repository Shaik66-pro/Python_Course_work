import re
pattern = r'[a-zA-Z]'
text = 'Python version 3.14, Windows 10'
res = re.match(pattern,text)
print(res.group() if res else "Patttren not found")


import re
pattern = r'[0-9]'
text = 'Python version 3.14, Windows 10'
res = re.search(pattern,text)
print(res.group() if res else "Patttren not found")


import re
pattern = r'[0-9]'
text = 'Python version 3.14, Windows 10'
res = re.findall(pattern,text)
print(res)


import re
pattern = r'[0-9]'
text = 'Python version 3.14, Windows 10'
res = re.finditer(pattern,text)
#res = re.findall(pattern,text)
#print(res)
for i in res:
    print(i.group(),i.start())



import re
pattern = r'[0-9]'
text = 'Python version 3.14, Windows 10'
res = re.sub(pattern,'*',text)
print(res)



import re
pattern = r'[Vrs,]'
text = 'Python version 3.14, Windows 10'
res = re.split(pattern,text)
print(res)

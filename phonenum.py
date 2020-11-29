import re,pyperclip

paste = pyperclip.paste()

obj = re.compile(r'((\d\d\d)?-\d\d\d-\d\d\d\d)')

found = obj.findall(paste)
#print(found[0])

final = []

for x in found:
    final.append(x[0])
    
print(final)

done = '\n'.join(final)
pyperclip.copy(done)



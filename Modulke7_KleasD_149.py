#Nomor 1
import re
f = open('Indonesia.txt', 'r', encoding='latin1')

teks = f.read()
f.close()
p = r'me\w+'
tampil = re.findall(p, teks)

print(tampil)


#Nomor 2
import re
f = open('Indonesia.txt', 'r', encoding='latin1')

teks = f.read()
f.close()
p = r'di\w+'
tampil = re.findall(p, teks)

print(tampil)

#Nomor 3
import re
f = open('Indonesia.txt', 'r', encoding='latin1')

teks = f.read()
f.close()
p = r'di \w+'
tampil = re.findall(p, teks)

print(tampil)


#Nomor 4
import re
f = open('KEI.htm', 'r', encoding='latin1')

teks = f.read()

strings = re.findall(r'title="([\w+]+)">', teks)
strings= re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>', teks)
a = []
for i in strings:
    a.append((i[0], float(i[1])))

print(a)



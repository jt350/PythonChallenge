import re

seq = re.compile('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]')

mess=open('/Users/johntaylor/Documents/Git/PythonChallenge/mess.txt','r')

mess_contents = mess.read()

mess.close()

answ=re.findall(seq, mess_contents)


print(answ)
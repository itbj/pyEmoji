string_e = 'hello'
print (string_e[0])
string = '汉字'
print (string[0])
#str通过encode()方法可以编码为指定的bytes。
#string_u = string[0].decode('UTF-8')
#print (string_u[0])
string_u='汉字'
print(string_u.encode('UTF-8'))
print (string_u.encode('UTF-16').decode('UTF-16'))
string_u='A'
print(string_u.encode('UTF-8'))
print(string_u.encode('UTF-16'))
print(string_u.encode('UTF-32'))
string_u='あ'
print(string_u.encode('UTF-8'))
print(string_u.encode('UTF-16'))
print(string_u.encode('UTF-32'))
# https://youtu.be/ut74oHojxqo?t=493
s="👍👌"
print (len(s))
print (s[0])
print (s[1])
s=u"👍👌"
print (len(s))
print (s[0])
print (s[1])
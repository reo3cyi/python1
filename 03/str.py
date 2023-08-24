
# data=input('수를 입력하세요:')
# try:
#     assert data=='7'
# except AssertionError as e:
#     print(e)

str=' Hello World Program,Java,nodeJS,c#,python,mysql'
str2='777'
a=str.lstrip()
b=str.strip()
#print(b)

#c=str2.zfill(5)
#print(c)
#d=str2.rjust(10,'0')
#print(d)
# e=str2.ljust(10,'1')
# print(e)
# f=str2.center(10,'#')
# print(f)
# g=str.split(',')
# print(g)
# h=str.split(',',2)
# print(h)

# reverse_str=''
# for a in str:
#     reverse_str=a + reverse_str
# print(reverse_str)

# str_list=list(str)
# str_list.reverse()
# print(str_list)

reverse_str=str[::-1]
print(reverse_str)
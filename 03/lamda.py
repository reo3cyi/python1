# add=lambda a,b : a+b   #익명함수
# result=add(1,2)
# print(result)

# result=(lambda a,b : a+b)(1,2)
# print(result)

# print((lambda a,b : a if a%2==0 else b)(1,3))
# print((lambda a,b : '{}+{}={}'.format(a,b,a+b,))(1,5))

# data=['Python','mySQL','nodeJS','Java','C#']
# data.sort(key=lambda x:len(x))
# print(data)
# data=list(map(lambda x : x*2,range(10)))
# print(data)
# data=list(filter(lambda x: x%2==0,range(10)))
# print(data)
fact=lambda n : 1 if n==1 else n*fact(n-1)
print(fact(5))
a=1000
b=2000
c=a+b
print(c)
print(a,id(a),type(a))
print(b,id(b),type(b))
print(c,id(c),type(c))


a=1000
b=1000
print(a,id(a),type(a))
print(b,id(b),type(b))


a=1000
b=a
a=3000
print(a,id(a),type(a))
print(b,id(b),type(b))


a=1000
b=2000
print(a,id(a),value(a))


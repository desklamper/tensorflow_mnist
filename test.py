import math
sita = math.atan(0.5)
result = (sita+(0.5*math.sin(2*sita))-(math.pi/4))*16
x = input("x = ")
a = (math.pi/2)*(x-1)
b = math.sin(a)
c = abs(b)
d = math.asin(c)
e = 2*d
f = e / math.pi
g = f-1
h = abs(g)

print(h)

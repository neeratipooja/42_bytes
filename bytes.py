'''
DAY:WEDNESDAy
DATE:30th NOV 2022
TOPIC:range
AUTHOR:pooja
'''
y=b'pooja'
print(y,type(y)) #b'pooja' 'bytes
print(list(y)) #[112,111,111,106,97]
print(tuple(y)) #(112,111,111,106,97)
print(set(y)) #112,111,111,106,97
h=b'pooja'
for i in h:
  print(i) #112
           #111
           #111
           #106
           #97
print(ord('p'))      #112
print(chr(106)) #j
h=b'pooja'
print(type(h)) #bytes     
# h[0]=90 #type error(byte is immutable)#no modification
v=b'[1,2,3]'
print(list(v)) #[91,49,44,50,44,51,93]
print(ord('[')) #91
print(ord(',')) #44
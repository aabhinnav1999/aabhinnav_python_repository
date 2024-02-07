Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=[10,10.05,True,15+2j,'PYSPIDERS',['10string','QSPIDERS'],('Ram','Sam'),{10,20,30},{"Hello":['venu','kashi']}]
#1
x[4]
'PYSPIDERS'
x[5][3:5+1:1]
[]
x[5]
['10string', 'QSPIDERS']
x[5][3]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x[5][3]
IndexError: list index out of range
x[5][3:5]
[]
x[5](3:5+1:1)
SyntaxError: invalid syntax
x[5]
['10string', 'QSPIDERS']
x[5][3::1]
[]
x[5][0][3:5+1:1]
'tri'
x[5][0]
'10string'
#2
x[5][0][2:4+1:1]
'str'
#3
x[4][2:5+1:1]
'SPID'
x[4][2:6+1:1]
'SPIDE'
#4
x[5][1][0:4+1:2]
'QPD'
x[6]
('Ram', 'Sam')
x[7]
{10, 20, 30}
#5
x[6][::-1]
('Sam', 'Ram')
x[7][::-1]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x[7][::-1]
TypeError: 'set' object is not subscriptable
#6
x[-1]['Hello']
['venu', 'kashi']
#7
x[-1]['Hello'][0]
'venu'
x=[10,10.05,True,15+2j,'PYSPIDERS',['10string','QSPIDERS'],('Ram','Sam'),{10,20,30},{"Hello":['venu','kashi']}]
#8
x[-1]['Hello'][::-1]
['kashi', 'venu']
x[4][-1:-7:-2]
'SEI'
#9
x[4][-1:-7-1:-2]
'SEIS'
x[5][2:6+1:2]
[]
#10
x[5][0][2:6+1:2]
'srn'
#11
SyntaxError: invalid syntax
#12
x[-6:-10:-1]
[(15+2j), True, 10.05, 10]
#13
x[5][0][::-1]
'gnirts01'
#14
x[-3][0][1]
'a'
#15
x[-3][1][0:2:2]
'S'
x[-3][1][0:2+1:2]
'Sm'
#16
x[0:2+1:1]
[10, 10.05, True]

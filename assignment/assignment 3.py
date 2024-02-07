Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={100:(10,"python",'helloworld',('django framework',),
{'bat':['c programming','java','c++', 'r language']},(10,20)),
'apple':{'venugopal','pooja','kasinath'}
,'Z':'pyspiders'}
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d[100]
(10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
d[100][3]
('django framework',)
#1
d[100][3][0:15+1:1]
('django framework',)
d[100][3][0:14+1:1]
('django framework',)
d[100][3][0:13+1:1]
('django framework',)
d[100][3][0]
'django framework'
#2
d[100][3][0][0::4]
'dgrw'
d[100][3][0::2]
('django framework',)
d[100][3][0][0::2]
'dag rmwr'
d[100][3][::-2]
('django framework',)
d[100][3][0][0::-2]
'd'
#3
d[100][3][0][::-2]
'koeafonj'
#4
d[100]
(10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
(10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
(10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
d[100][-2]
{'bat': ['c programming', 'java', 'c++', 'r language']}
d[100][-2]['bat']
['c programming', 'java', 'c++', 'r language']
d[100][-2]['bat'][::-1]
['r language', 'c++', 'java', 'c programming']
['r language', 'c++', 'java', 'c programming']
['r language', 'c++', 'java', 'c programming']
#5
d[100][-2]['bat'][::-3]
['r language', 'c programming']
#6
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d[100]
(10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
d['apple']
{'pooja', 'kasinath', 'venugopal'}
d[-2]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    d[-2]
KeyError: -2
d[1]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    d[1]
KeyError: 1
d[::1]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d[::1]
TypeError: unhashable type: 'slice'
type(d)
<class 'dict'>
d.keys()
dict_keys([100, 'apple', 'Z'])
a1=list(a.keys())
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a1=list(a.keys())
NameError: name 'a' is not defined
a1=list(d.keys())
a1
[100, 'apple', 'Z']
a1[::-1]
['Z', 'apple', 100]
#8
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d[100][]2[::-1]
SyntaxError: invalid syntax
d[100][2][::-1]
'dlrowolleh'
#9
d[100]
(10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
d[100]['bat']
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d[100]['bat']
TypeError: tuple indices must be integers or slices, not str
d[100][4]
{'bat': ['c programming', 'java', 'c++', 'r language']}
d[100][4][bat]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    d[100][4][bat]
NameError: name 'bat' is not defined
d[100][4]['bat']
['c programming', 'java', 'c++', 'r language']
d[100][4]['bat'][:-11-1:-1]
['r language', 'c++', 'java', 'c programming']
d[100][4]['bat'][0][:-11-1:-1]
'gnimmargorp'
d[100][4]['bat'][0][:-11-1:-3]
'gmrr'
#10
d[100][4]['bat'][0][::-3]
'gmrrc'
#11
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d['apple']
{'pooja', 'kasinath', 'venugopal'}
d['apple'][1][::-1]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    d['apple'][1][::-1]
TypeError: 'set' object is not subscriptable
#12
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d[100][4]['bat']
['c programming', 'java', 'c++', 'r language']
d[100][4]['bat'][-1:-3-1:-1]
['r language', 'c++', 'java']
d[100][4]['bat'][-2:-3-1:-1][-2]
'c++'
d[100][4]['bat'][-2:-3-1:-1]
['c++', 'java']
d[100][4]['bat'][-2:-3-1:-1][::-1]
['java', 'c++']
d[100][4]['bat'][-2:-3-1:-1][-2][::-1]
'++c'
#13
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
a2=list(d.values())
a2
[(10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), {'pooja', 'kasinath', 'venugopal'}, 'pyspiders']
a2[-2]
{'pooja', 'kasinath', 'venugopal'}
a2[-2][0]
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a2[-2][0]
TypeError: 'set' object is not subscriptable
#14
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
z=list(d.items())
z
[(100, (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))), ('apple', {'pooja', 'kasinath', 'venugopal'}), ('Z', 'pyspiders')]
z[-2]
('apple', {'pooja', 'kasinath', 'venugopal'})
z[-2][-1]
{'pooja', 'kasinath', 'venugopal'}
z[-2][-1][0]
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    z[-2][-1][0]
TypeError: 'set' object is not subscriptable
#15
z[-2][-1][::-1]
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    z[-2][-1][::-1]
TypeError: 'set' object is not subscriptable
#16
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d[100][5]
(10, 20)
float(d[100][5])
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    float(d[100][5])
TypeError: float() argument must be a string or a real number, not 'tuple'
float((10, 20))
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    float((10, 20))
TypeError: float() argument must be a string or a real number, not 'tuple'
#17
z
[(100, (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))), ('apple', {'pooja', 'kasinath', 'venugopal'}), ('Z', 'pyspiders')]
z[1]
('apple', {'pooja', 'kasinath', 'venugopal'})
z[0]
(100, (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)))
z[0][1]
(10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
z[0][1][2]
'helloworld'
tuple(z[0][1][2])
('h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd')
tuple(z[0][1])
(10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
#18
z
[(100, (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))), ('apple', {'pooja', 'kasinath', 'venugopal'}), ('Z', 'pyspiders')]
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
a1
[100, 'apple', 'Z']
#19
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d[100]
(10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
d[100][4]
{'bat': ['c programming', 'java', 'c++', 'r language']}
d[100][5]
(10, 20)
complex(d[100][5])
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    complex(d[100][5])
TypeError: complex() first argument must be a string or a number, not 'tuple'
#20
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d[z]
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    d[z]
TypeError: unhashable type: 'list'
d['z']
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    d['z']
KeyError: 'z'
d['Z']
'pyspiders'
#21
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d[100]
(10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
d[100][3]
('django framework',)
list(d[100][3])
['django framework']
list(['django framework'])
['django framework']
d[100][3]
('django framework',)
d[100][3]=['django','framework']
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    d[100][3]=['django','framework']
TypeError: 'tuple' object does not support item assignment
d[100][3]=list()
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    d[100][3]=list()
TypeError: 'tuple' object does not support item assignment
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
string(100)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    string(100)
NameError: name 'string' is not defined
str(100)
'100'
list(100)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    list(100)
TypeError: 'int' object is not iterable
list('100')
['1', '0', '0']
tuple('100')
('1', '0', '0')
#24
d[apple]
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    d[apple]
NameError: name 'apple' is not defined. Did you mean: 'tuple'?
d['apple']
{'pooja', 'kasinath', 'venugopal'}
d=list(d)
d
[100, 'apple', 'Z']
d
[100, 'apple', 'Z']
z
[(100, (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))), ('apple', {'pooja', 'kasinath', 'venugopal'}), ('Z', 'pyspiders')]
z[-1]
('Z', 'pyspiders')
z[-2]
('apple', {'pooja', 'kasinath', 'venugopal'})
z[-2]={'apple' : 'venu','pooja','kasi'}
SyntaxError: ':' expected after dictionary key
z[-2]={'apple': 'venu','pooja','kasi'}
SyntaxError: ':' expected after dictionary key
z[-2]={'apple': 'venu','pooja','kasi'}
SyntaxError: ':' expected after dictionary key
z[-2]={'apple':'venu','pooja','kasi'}
SyntaxError: ':' expected after dictionary key
z[-2]={'apple':'venu','pooja','kasi'}
SyntaxError: ':' expected after dictionary key
z[-2]={'apple':{'venu','pooj','kasi'}}
z[-2]
{'apple': {'kasi', 'pooj', 'venu'}}
z[-2][::-1]
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    z[-2][::-1]
TypeError: unhashable type: 'slice'
z[-2]['apple']
{'kasi', 'pooj', 'venu'}
z[-2]['apple']={'venu','pooj','kasi'}
z
[(100, (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))), {'apple': {'kasi', 'pooj', 'venu'}}, ('Z', 'pyspiders')]
#25
d
[100, 'apple', 'Z']
d={100:(10,"python",'helloworld',('django framework',),
{'bat':['c programming','java','c++', 'r language']},(10,20)),
'apple':{'venugopal','pooja','kasinath'}
,'Z':'pyspiders'}
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d[100]
(10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
d[100][4]
{'bat': ['c programming', 'java', 'c++', 'r language']}
KeyboardInterrupt
d[100][4]['bat']
['c programming', 'java', 'c++', 'r language']
d[100][4]['bat'][::-2]
['r language', 'java']
#26
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d[100]
(10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
d[100]=list(100)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    d[100]=list(100)
TypeError: 'int' object is not iterable
d[100][3]
('django framework',)
d[100][3]=('django framework','krowemarf ognajd')
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    d[100][3]=('django framework','krowemarf ognajd')
TypeError: 'tuple' object does not support item assignment
d[100][3]=list(('django framework','krowemarf ognajd'))
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    d[100][3]=list(('django framework','krowemarf ognajd'))
TypeError: 'tuple' object does not support item assignment
list(('django framework','krowemarf ognajd'))
['django framework', 'krowemarf ognajd']
z
[(100, (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))), {'apple': {'kasi', 'pooj', 'venu'}}, ('Z', 'pyspiders')]
z[1]
{'apple': {'kasi', 'pooj', 'venu'}}
z[0]
(100, (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)))
y=list(z[0])
y
[100, (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))]
z[0]
(100, (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)))
z[0]=y
z
[[100, (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))], {'apple': {'kasi', 'pooj', 'venu'}}, ('Z', 'pyspiders')]
z[0]
[100, (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))]
z[0][1]
(10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
y=list(z[0][1])
y
[10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)]
z[0][1]=y
z
[[100, [10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)]], {'apple': {'kasi', 'pooj', 'venu'}}, ('Z', 'pyspiders')]
z[0][1]
[10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)]
z[0][1][3]
('django framework',)
y=list(z[0][1][3])
y
['django framework']
type(y)
<class 'list'>
y=['django framework','krowemarf ognajd']
y
['django framework', 'krowemarf ognajd']
z[0][1][3]=y
z
[[100, [10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)]], {'apple': {'kasi', 'pooj', 'venu'}}, ('Z', 'pyspiders')]
z[0]
[100, [10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)]]
z[0][1]
[10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)]
y=tuple(z[0][1])
y
(10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
z[0][1]=y
z
[[100, (10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))], {'apple': {'kasi', 'pooj', 'venu'}}, ('Z', 'pyspiders')]
z[1]
{'apple': {'kasi', 'pooj', 'venu'}}
z[0]
[100, (10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))]
z[0][1]
(10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
y=z[0][1]
y
(10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d[100]
(10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
d[100]=y
d
{100: (10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
#27
d
{100: (10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d[100]
(10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20))
d[100]['bat']
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    d[100]['bat']
TypeError: tuple indices must be integers or slices, not str
d[100][-2]
{'bat': ['c programming', 'java', 'c++', 'r language']}
d[100][-2]['bat']
['c programming', 'java', 'c++', 'r language']
d[100][-2]['bat'][::-1]
['r language', 'c++', 'java', 'c programming']
z=d[100][-2]['bat'][::-1]
z
['r language', 'c++', 'java', 'c programming']
z=d[100][-2]['bat']
z
['c programming', 'java', 'c++', 'r language']
d
{100: (10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['c programming', 'java', 'c++', 'r language']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
z=d[100][-2]['bat'][::-1]
z
['r language', 'c++', 'java', 'c programming']
d[100][-2]['bat']
['c programming', 'java', 'c++', 'r language']
d[100][-2]['bat']=z
d
{100: (10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['r language', 'c++', 'java', 'c programming']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
#28
d
{100: (10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['r language', 'c++', 'java', 'c programming']}, (10, 20)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
d[100]
(10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['r language', 'c++', 'java', 'c programming']}, (10, 20))
d[100][-1]
(10, 20)
z=d[100][-1]
z
(10, 20)
z=list(z)
z
[10, 20]
z[0]=10+0j
z
[(10+0j), 20]
z[1]=float(z[1])
z
[(10+0j), 20.0]
d[100][-1]=z
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    d[100][-1]=z
TypeError: 'tuple' object does not support item assignment
z
[(10+0j), 20.0]
y=list(d[100])
y
[10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['r language', 'c++', 'java', 'c programming']}, (10, 20)]
y[-1]
(10, 20)
y[-1]=z
y
[10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['r language', 'c++', 'java', 'c programming']}, [(10+0j), 20.0]]
z
[(10+0j), 20.0]
z=tuple(z)
z
((10+0j), 20.0)
y[-1]=z
y
[10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['r language', 'c++', 'java', 'c programming']}, ((10+0j), 20.0)]
y=tuple(y)
y
(10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['r language', 'c++', 'java', 'c programming']}, ((10+0j), 20.0))
d[100]=y
d
{100: (10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['r language', 'c++', 'java', 'c programming']}, ((10+0j), 20.0)), 'apple': {'pooja', 'kasinath', 'venugopal'}, 'Z': 'pyspiders'}
#29
d['apple']
{'pooja', 'kasinath', 'venugopal'}
z=list(d['apple'])
z
['pooja', 'kasinath', 'venugopal']
z[-1]
'venugopal'
z[-1]=z[-1][::-1]
z
['pooja', 'kasinath', 'lapogunev']
z[1]
'kasinath'
z[1]=z[1][::-1]
z
['pooja', 'htanisak', 'lapogunev']
z=set(z)
z
{'lapogunev', 'pooja', 'htanisak'}
d['apple']=z
d
{100: (10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['r language', 'c++', 'java', 'c programming']}, ((10+0j), 20.0)), 'apple': {'lapogunev', 'pooja', 'htanisak'}, 'Z': 'pyspiders'}
#30
z=list(d)
d
{100: (10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['r language', 'c++', 'java', 'c programming']}, ((10+0j), 20.0)), 'apple': {'lapogunev', 'pooja', 'htanisak'}, 'Z': 'pyspiders'}
z
[100, 'apple', 'Z']
z=list(d.items())
z
[(100, (10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['r language', 'c++', 'java', 'c programming']}, ((10+0j), 20.0))), ('apple', {'lapogunev', 'pooja', 'htanisak'}), ('Z', 'pyspiders')]
z[::-1]
[('Z', 'pyspiders'), ('apple', {'lapogunev', 'pooja', 'htanisak'}), (100, (10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['r language', 'c++', 'java', 'c programming']}, ((10+0j), 20.0)))]
z[::-1][::-1]
[(100, (10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['r language', 'c++', 'java', 'c programming']}, ((10+0j), 20.0))), ('apple', {'lapogunev', 'pooja', 'htanisak'}), ('Z', 'pyspiders')]
z[::-1]
[('Z', 'pyspiders'), ('apple', {'lapogunev', 'pooja', 'htanisak'}), (100, (10, 'python', 'helloworld', ['django framework', 'krowemarf ognajd'], {'bat': ['r language', 'c++', 'java', 'c programming']}, ((10+0j), 20.0)))]

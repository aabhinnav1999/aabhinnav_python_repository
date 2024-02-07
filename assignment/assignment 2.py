Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={'a':{'10':(10,"girish",'helloworld','i love india',{'d':['python','django','java'],(10,):{'venugopal','kashi'}})}}
#1
d['a'][10]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    d['a'][10]
KeyError: 10
d['a']['10']
(10, 'girish', 'helloworld', 'i love india', {'d': ['python', 'django', 'java'], (10,): {'venugopal', 'kashi'}})
d['a']['10'][1]
'girish'
#2
d['a']['10'][1][::-1]
'hsirig'
#3
d['a']['10'][1][-2:-6-1:-2]
'srg'
#4
d['a']['10'][1][0:5+1:2]
'grs'
d['a']['10'][1][0:1+1:1]
'gi'
#5
d['a']['10'][1][0:1+1:1]
'gi'
#6
d['a']['10'][1][-1:-3-1:-2]
'hi'
d={'a':{'10':(10,"girish",'helloworld','i love india',{'d':['python','django','java'],(10,):{'venugopal','kashi'}})}}
d['a']['10']
(10, 'girish', 'helloworld', 'i love india', {'d': ['python', 'django', 'java'], (10,): {'venugopal', 'kashi'}})
#7
d['a']['10'][-2][0:4+1]
'i lov'
d['a']['10'][2][0:4+1]
'hello'
#8
d['a']['10'][-2][5:9+1]
'e ind'
d['a']['10'][2][5:9+1]
'world'
#9
d['a']['10'][2]
'helloworld'
#10
d['a']['10'][2][::-1]
'dlrowolleh'
#11
d['a']['10'][2][-1:-10-1:-]
SyntaxError: invalid syntax
d['a']['10'][2][-1:-10-1:-2]
'drwle'
#12
d['a']['10'][2][0:8+1:2]
'hlool'
#13
d['a']['10'][2][0:8+1:3]
'hlo'
d['a']['10'][2][0:8+1:4]
'hol'
#14
d['a']['10'][2][-1:-8-1:-4]
'dw'
d['a']['10'][2][-1:-9-1:-4]
'dwe'
#15
d['a']['10']
(10, 'girish', 'helloworld', 'i love india', {'d': ['python', 'django', 'java'], (10,): {'venugopal', 'kashi'}})
d['a']['10'][3]
'i love india'
#16
d['a']['10'][3][-1]
'a'
d['a']['10'][3][7::1]
'india'
#17
d['a']['10'][3][2::1]
'love india'
#18
d['a']['10'][3][::-1]
'aidni evol i'
#19
d['a']['10'][3][-1:-7-1:-1]
'aidni e'
d['a']['10'][3][-1:-7-1:-2]
'adie'
d['a']['10'][3][-1:-9-1:-1]
'aidni evo'
d['a']['10'][3][-1:-9-1:-2]
'adieo'
#20
d['a']['10'][4]['d']
['python', 'django', 'java']
d['a']['10'][4]['d'][0][::-1]
'nohtyp'
#21
d['a']['10'][4]['d'][1][::-1]
'ognajd'
#22
d['a']['10'][4]['d'][2][0:1+1]
'ja'
#23
d['a']['10'][4]['d'][2][::-1]
'avaj'
#24
d['a']['10'][4]['d']
['python', 'django', 'java']
#25
d['a']['10'][4]['d'][::-1]
['java', 'django', 'python']
#26
d['a']['10'][4]['d'][0::2]
['python', 'java']
#27
d['a']['10'][4]['d'][-1::-2]
['java', 'python']
d['a']['10']
(10, 'girish', 'helloworld', 'i love india', {'d': ['python', 'django', 'java'], (10,): {'venugopal', 'kashi'}})
#28
d['a']['10'][-1]
{'d': ['python', 'django', 'java'], (10,): {'venugopal', 'kashi'}}
d['a']['10'][-1][(10,)]
{'venugopal', 'kashi'}
d['a']['10'][-1][(10,)][-1]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    d['a']['10'][-1][(10,)][-1]
TypeError: 'set' object is not subscriptable
#29 #30 #31
#32
d['a']['10'][0:3+1]
(10, 'girish', 'helloworld', 'i love india')
#33
d['a']['10'][-2::-1]
('i love india', 'helloworld', 'girish', 10)
#34
d['a']['10'][0:2+1:2]
(10, 'helloworld')
#35
d['a']['10'][1:2+1]
('girish', 'helloworld')
d['a']['10']
(10, 'girish', 'helloworld', 'i love india', {'d': ['python', 'django', 'java'], (10,): {'venugopal', 'kashi'}})
#36
d['a']['10'][-2::-2]
('i love india', 'girish')
d['a']['10'][-2::-3]
('i love india', 10)
#37
d['a']['10'][-3::-2]
('helloworld', 10)
#38
d['a']['10'][0]['d'][0]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    d['a']['10'][0]['d'][0]
TypeError: 'int' object is not subscriptable
#39
TypeError: invalid syntax
#40
d['a']['10'][-1][(10,)][0]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    d['a']['10'][-1][(10,)][0]
TypeError: 'set' object is not subscriptable

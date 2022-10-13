Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("============================Task1 22/08/2022======================================")
============================Task1 22/08/2022======================================
print("============================additions======================================")
============================additions======================================
a=5
b=10;
c=a+b;
print (c)
15
print("============================Substractions======================================")
============================Substractions======================================
a=5;
b=10;
c=a-b;
print (c);
-5
print("============================multiplications======================================")
============================multiplications======================================
a=5;
b=10;
c=a*b;
print(c)
50
print("============================Division======================================")
============================Division======================================

a=5;
b=10;
c=b/a;
print(c);
2.0
print("============================Task1 22/08/2022======================================")

============================Task1 22/08/2022======================================
KeyboardInterrupt
print("============================Task1 22/08/2022======================================")
print("============================Remainder======================================")
============================Remainder======================================
a=5;
b=10;
c=b%a;
print(c);
0
print("============================single variable && multiple value======================================")
============================single variable && multiple value======================================
a=5,10,15,20,25;
b=25,20,15,10,5;
c=a+b;
print (c);
(5, 10, 15, 20, 25, 25, 20, 15, 10, 5)
print("============================single value && multple variable======================================")
============================single value && multple variable======================================
a,b,=5;
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a,b,=5;
TypeError: cannot unpack non-iterable int object
a=b=5;
c=a+b;
print("c")
c
print(c);
10
a=b=c=d=10;
x=a+b;
y=a+b+c+d;
z=a-b-c-d;
p=y/x;
q=z/p;
r=p%q;
print(x+y+z+p+q+r);
24.0
print(x);
20
print(y);
40
print(z);
-20
print(p);
2.0
print(q);
-10.0
print(r);
-8.0
print("============================String used single value && multiple variable======================================")
============================String used single value && multiple variable======================================
stdnme,classattender,tasker="Vignesh";
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    stdnme,classattender,tasker="Vignesh";
ValueError: too many values to unpack (expected 3)
stdnme=classattender=tasker="Vignesh N";
Companynme=trainernme="Mr.Python";
print(stdnme+companynme);
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    print(stdnme+companynme);
NameError: name 'companynme' is not defined. Did you mean: 'Companynme'?
print(stdnme+Companynme);
Vignesh NMr.Python
print (tasker+trainernme);
Vignesh NMr.Python
print (classattender+"\n"stdnme);
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print (classattender+"\n"stdnme);

SyntaxError: invalid syntax. Perhaps you forgot a comma?
print (classattender+"\n"+Companynme);
Vignesh N
Mr.Python

print("============================String used multilple value && single variable======================================")
============================String used multilple value && single variable======================================
name="vignesh","Narayanan"
taskerDate="22/08/2022","Day 1"
print("Day 1 Task Completed "+name+taskerDate);
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print("Day 1 Task Completed "+name+taskerDate);
TypeError: can only concatenate str (not "tuple") to str
name="vignesh"="Narayanan";
SyntaxError: cannot assign to literal
print(name+taskerDate);
('vignesh', 'Narayanan', '22/08/2022', 'Day 1')
print(taskerDate+"\n"+name);
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print(taskerDate+"\n"+name);
TypeError: can only concatenate tuple (not "str") to tuple
print(taskerDate+name);
('22/08/2022', 'Day 1', 'vignesh', 'Narayanan')
print("##############################################DAY 1 TaskCompleted#######################################################################")
##############################################DAY 1 TaskCompleted#######################################################################

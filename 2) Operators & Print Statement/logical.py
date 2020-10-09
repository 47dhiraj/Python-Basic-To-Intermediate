Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = (True or (False or True and True))
>>> (True or (False or True and True))
True
>>> a = (True or (False or True and True))
>>> print(a)
True
>>> 
(False or True and True))
SyntaxError: invalid syntax
>>> (False or True and True)
True
>>> 

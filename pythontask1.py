Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> math.pi
3.141592653589793
>>> def circle_area(r):
	r= float(input('Enter the radius of the circle:'))
	area=math.pi*(r**2)
	return area

>>> circle_area(8)
Enter the radius of the circle:6
113.09733552923255
>>> 
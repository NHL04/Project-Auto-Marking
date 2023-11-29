#!/usr/bin/python3

import math

# your code for class Shape  -- Q.4(f)
class Shape:
	def __init__(self,name):
		self.name=name
	def str(self):
		return(self.name+"(area = "+str(self.area()) +" , circumference = "+str(self.circumference())+" )")
	
# your code for class Triangle -- Q.4(a)
class Triangle(Shape):
	def __init__(self,b,h,name="Triangle"):
		Shape.__init__(self,name)
		self.base=b
		self.height=h
	def area(self):
		return (1/2.0)*b*h

# code for RegularPolygon is provided below for your use.
class RegularPolygon(Shape):
  def __init__(self, n, l, name="Regular Polygon"):
    if(n < 3):
      raise ValueError("Polygons can't have less than 3 sides.")
    Shape.__init__(self, name)
    self.num_of_sides = n
    self.length = l

  def area(self):
    theta = 2 * math.pi / self.num_of_sides
    phi = (self.num_of_sides - 2) * math.pi / (2 * self.num_of_sides)
    b = self.length
    h = (b * math.tan(phi)) / 2
    area_triangle = 0.5 * b * h
    return self.num_of_sides * area_triangle

  def circumference(self):
    return self.num_of_sides * self.length

  def get_side(self):
    return self.length

# your code for class Square -- Q.4(c)
class Square(RegularPolygon):
	def __init__(self,l,name="Square"):
		RegularPolygon.__init__(self,4,l,name)

# your code for class EquilateralTriangle -- Q.4(c)
class EquilateralTriangle(RegularPolygon):
	def __init__(self,l,name="EquilateralTriangle"):
		RegularPolygon.__init__(self,3,l,name)

# your code for class Pentagon -- Q.4(d) and Q.4(e)
class Pentagon(RegularPolygon):
	def __init__(self,l,name="Pentagon"):
		RegularPolygon.__init__(self,5,l,name)
		self.triangle=EquilateralTriangle(l)
		self.square=Square(l)
	def area(self):
		return self.triangle.area()+self.square.area()
	def circumference(self):
		return self.get_side()*5
if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)

  print("t1 = ", t1.str())
  print("s1 = ", s1.str())
  print("p1 = ", p1.str())

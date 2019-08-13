from Polygon import Polygon
from Rectangle import Rectangle

mypolygon=Polygon()
myrectangle=Rectangle()

print ("perimeter of mypolygon is ...")
print (mypolygon.perimeter())

print ("perimeter of myrectangle is ...")
print (myrectangle.perimeter())

mypolygon=myrectangle
print ("perimeter of mypolygon is ...")
print (mypolygon.perimeter())

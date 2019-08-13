from Point import Point

mypoint=Point(5.0,6.0)
print(mypoint)

print ("Translating MyPoint by (2.0,3.0) ...")
mypoint.translate(2.0,3.0)
print(mypoint)

print ("Translating MyPoint by (-2.0,-3.0) ...")
mypoint.translate(-2.0,-3.0)
print(mypoint)

print ("Scaling MyPoint by (1/2,1/2) ...")
mypoint.scale(0.5,0.5)
print(mypoint)

print ("Scaling MyPoint by (1/2,1/2) ...")
mypoint.scale(2.0,2.0)
print(mypoint)

print ("Rotating MyPoint by 60 degrees ...")
mypoint.rotate(60.0)
print(mypoint)

print ("Rotating MyPoint by -60 degrees ...")
mypoint.rotate(-60.0)
print(mypoint)

print("----")
print("Testing the distance function")

#That is, the following is a test of a distance function
#that computes distance from mypoint to a another point

mysecondpoint=Point(7.0,9.0)

print("mypoint is ",end="")
print(mypoint)

print("mysecondpoint is ",end="")
print(mysecondpoint)

print("Distance from mypoint to mysecondpoint is: ", \
      mypoint.distance(mysecondpoint))

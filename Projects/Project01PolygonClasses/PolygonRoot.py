from Polygon import Polygon

mypolygon=Polygon()

print ("the four vertices of the 'hard-coded' mypolygon...")
print(mypolygon)

print ("translating mypolygon by (2.0,3.0)...")
Polygon.translate(mypolygon,2.0,3.0)
print(mypolygon)

print ("translating mypolygon by (-2.0,-3.0)...")
Polygon.translate(mypolygon,-2.0,-3.0)
print(mypolygon)

print ("scaling mypolygon by (0.5,0.5)...")
Polygon.scale(mypolygon,0.5,0.5)
print(mypolygon)

print ("scaling mypolygon by (2.0,2.0)...")
Polygon.scale(mypolygon,2.0,2.0)
print(mypolygon)

print ("rotating mypolygon by 60 degrees...)")
Polygon.rotate(mypolygon,60)
print(mypolygon)

print ("rotating mypolygon by -60 degrees...")
Polygon.rotate(mypolygon,-60)
print(mypolygon)

print("perimeter of mypolygon is ...")
print(mypolygon.perimeter())



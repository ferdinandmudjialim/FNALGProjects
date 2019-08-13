from Rectangle import Rectangle

myrectangle=Rectangle()

print ()
print ("the four vertices of the 'hard-coded' myrectangle are ...")
print(myrectangle)
print ("the manually computed length of myrectangle is ... 6")
print ("the manually computed width of myrectangle is ... 4")
print ()

print ("translating myrectangle by (2.0,3.0)...")
Rectangle.translate(myrectangle,2.0,3.0)
print(myrectangle)

print ("translating myrectangle by (-2.0,-3.0)...")
Rectangle.translate(myrectangle,-2.0,-3.0)
print(myrectangle)

print ("scaling myrectangle by (0.5,0.5)...")
Rectangle.scale(myrectangle,0.5,0.5)
print(myrectangle)

print ("scaling myrectangle by (2.0,2.0)...")
Rectangle.scale(myrectangle,2.0,2.0)
print(myrectangle)

print ("rotating myrectangle by 60 degrees...)")
Rectangle.rotate(myrectangle,60)
print(myrectangle)

print ("rotating myrectangle by -60 degrees...")
Rectangle.rotate(myrectangle,-60)
print(myrectangle)

print ("perimeter of myrectangle is ...")
print (myrectangle.perimeter())

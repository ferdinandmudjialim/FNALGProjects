# Name: Ferdinand Mudjialim
# Project 1
# Description: reads input from a text file and constructs either a polygon
# or rectangle object. Then, each object returns its vertices, perimeter,
# and area.
from Polygon import Polygon
from Rectangle import Rectangle

fp = open("project01data.txt")
line = fp.readline()
while line != "":
    polygonheader = line.split()  # this is the line with the identifier
    polytype = polygonheader[0]
    polynum = int(polygonheader[1])
    # It is assumed that the polygons are either "polygon" or "rectangle"
    # print("Reading vertices for a %s with %d vertices..."
    #       % ("polygon" if polytype == "P" else "rectangle", polynum))

    # Construct a list of points to be used in constructing the polygon
    points = []
    for i in range(polynum):
        vertices = fp.readline().split()
        points.append([float(vertices[0]), float(vertices[1])])
        # print("Vertex %d has coordinates at (%.2f, %.2f)"
        #       % (i, float(vertices[0]), float(vertices[1])))

    # Construct a polygon/rect and return its vertices, perimeter, and area
    if polytype == "P":
        someshape = Polygon(points)
    else:
        someshape = Rectangle(points)
    print(someshape)
    print("Perimeter:", someshape.perimeter())
    print("Area:", someshape.area())
    print('--------------------------')
    line = fp.readline()


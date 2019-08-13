# Name: Ferdinand Mudjialim
# Lab 3
# Description: reads input from a text file and echo checks (prints) data for
# polygons with a variable number of vertices
fp = open("input.txt")
line = fp.readline()
while line != "":
    polygonheader = line.split()
    polytype = polygonheader[0]
    polynum = int(polygonheader[1])
    # It is assumed that the polygons are either "polygon" or "rectangle"
    print("Reading vertices for a %s with %d vertices..."
          % ("polygon" if polytype == "P" else "rectangle", polynum))

    for i in range(polynum):
        vertices = fp.readline().split()
        print("Vertex %d has coordinates at (%.2f, %.2f)"
              % (i, float(vertices[0]), float(vertices[1])))
    line = fp.readline()

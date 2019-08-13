from Polygon import Polygon
from Point import Point

class Rectangle(Polygon):
    def __init__(self, pointlist):
        super(Rectangle, self).__init__(pointlist)

        # self.vertices = []
        # for coordinate in pointlist:
        #     self.vertices.append(Point(coordinate[0], coordinate[1]))

        distance1 = self.vertices[0].distance(self.vertices[1])
        distance2 = self.vertices[2].distance(self.vertices[3])
        if distance1 >= distance2:
            self.length = distance1
            self.width = distance2
        else:
            self.length = distance2
            self.width = distance1

    def perimeter(self):
        print ("Using Rectangle's perimeter routine")
        return "{:.2f}".format(2*self.length+2*self.width)

    def area(self):
        return "{:.2f}".format(self.length*self.width)

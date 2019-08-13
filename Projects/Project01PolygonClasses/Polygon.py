import math
import itertools
from Point import Point

class Polygon(object):
    def __init__(self, pointlist):
        self.rawpoints = pointlist
        self.vertices = []
        for coordinate in pointlist:
            self.vertices.append(Point(coordinate[0], coordinate[1]))

    def translate(self,a=0.0,b=0.0):
        for p in self.vertices:
            Point.translate(p,a,b)

    def scale(self,sx=0.0,sy=0.0):
        for p in self.vertices:
            Point.scale(p,sx,sy)

    def rotate(self,theta_in_degrees=0.0):
        for p in self.vertices:
            Point.rotate(p,theta_in_degrees)

    def __str__(self):
        s=""
        for p in self.vertices:
          # s=s+" "+str(p.x)+" "+str(p.y)+"\n"
            s=s+" "+"{:.2f}".format(p.x)+"  "+"{:.2f}".format(p.y)+"\n"
        return s

#using itertools.cycle
    def perimeter(self):
        """ convert a list of points into a list of distances """
        print ("Using Polygon's perimeter routine")
        distances = []
        circular_buffer = itertools.cycle(self.vertices)
        previous_point = next(circular_buffer)
        for i in range(len(self.vertices)):
            point = next(circular_buffer)
            d = point.distance(previous_point)
            distances.append(d)
            previous_point = point
        return "{:.2f}".format(sum(distances))

    def area(self):
        #[[x1, y1], [x2, y2]] x1 * y2
        print("Using Polygon's area routine")
        newrawpoints = self.rawpoints
        newrawpoints.append(self.rawpoints[0])
        firstsum, secondsum = 0.0, 0.0
        for i in range(1, len(newrawpoints)):
            firstsum += newrawpoints[i-1][0] * newrawpoints[i][1]
            secondsum -= newrawpoints[i-1][1] * newrawpoints[i][0]
        return "{:.2f}".format(abs((firstsum + secondsum) / 2.0))
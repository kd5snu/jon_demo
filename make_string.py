#!/usr/bin/python
import decimal
import json

decimal.getcontext().prec = 4
decimal.getcontext().rounding = decimal.ROUND_DOWN

density = 144
length = 3.0

def write_file(points):
    # Open the point cloud file
    file = open('test1.json', 'wa')

    # Write in opening bracket then newline
    file.write("[\n")

    # Add in each line of the array, sans the last one

    for line in xrange(len(points)-1):
        file.write( "  {" + '"point": [{x}, {y}, {z}]'.format(
            x=points[line][0],
            y=points[line][1],
            z=points[line][2]) + "},\n" )

    file.write( "  {" + '"point": [{x}, {y}, {z}]'.format(
        x=points[len(points)-1][0],
        y=points[len(points)-1][1],
        z=points[len(points)-1][2]) + "}\n" )
    file.write("]\n")

    file.close()

def make_point_cloud(density, length):
    for line in xrange(density * int(length)):
        point = decimal.Decimal(line*((1.0/(density))))
        points[line][0] = float(round(point, 3))
    return points

points = [[0 for j in range(3)] for i in range(density * int(length))]

points = make_point_cloud(density, length)

for line in points:
    print line
write_file( points )

from collections import namedtuple
#namedtuple

# Basic example
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)     # instantiate with positional or keyword arguments
t = (1, 2)
p2 = Point._make(t)

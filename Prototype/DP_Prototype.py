import sys

from Flyweight.DP_Flyweight import Point

point1 = Point(1, 2, 3, "white")
point2 = eval("{}({}, {}, {}, '{}')".format("Point", 20, 30, 40, "c9a0"))
point3 = getattr(sys.modules[__name__], "Point")(20, 50, 60, "miao") # vado a prendere dal dizionario dei nomi la classe Point e quindi vado ad istanziare un nuovo oggetto


# ipotizziamo che la classe point abbia già degli attributi ben definiti che sono x, y, z e color; quindi andiamo a definire __slots__ così formato
class Point:
    # grazie a slots nessun Point ha il suo dict privato e quindi nessun attributo può essere aggiunto
    __slots__ = ["x", "y", "z", "color"]

    def __init__(self, x = 0, y = 0, z = 0, color = None):
        self.x = x
        self.y = y
        self.z = z
        self.color = color


def main():
    y = Point(10, 20, 30, "white")
    print(y.__slots__) # it works!
    print(y.__dict__) # point non ha alcun attributo dict

if __name__ == "__main__" :
    main()

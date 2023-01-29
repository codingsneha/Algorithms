def TOH(n, x, y, z):
    if (n == 1):
        print ("Move disk 1 from source", x, "to desination", z)
        return
    TOH(n - 1, x, y, z)
    print("Move disk", n, "from source", x, "to destnation", z)
    TOH(n - 1, y, z, x)

n = 2
TOH(n, 'A', 'B', 'C')
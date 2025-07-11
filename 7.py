points = [(1,3), (2, 6), (3, 9)]
if len(points) < 2:
    print("Yes, the points form a straight line.")
else:
    (x0, y0), (x1, y1) = points[0], points[1]
    dx = x1 - x0
    dy = y1 - y0

    for i in range(2, len(points)):
        x, y = points[i]
        if dy * (x - x0) != dx * (y - y0):
            print("No, the points do not form a straight line.")
            break
        print("Yes, the points form a straight line.") 
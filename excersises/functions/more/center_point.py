def center_point(x1, y1, x2, y2):
    root1 = (x1 ** 2) + (y1 ** 2)
    root2 = (x2 ** 2) + (y2 ** 2)
    if root1 > root2:
        return x2, y2
    elif root1 < root2:
        return x1, y1
    else:
        return x1, y1


y1 = float(input())
z1 = float(input())
y2 = float(input())
z2 = float(input())

print(center_point(int(y1), int(z1), int(y2), int(z2)))

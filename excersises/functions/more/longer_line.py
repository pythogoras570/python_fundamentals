def center_point(x1, y1, x2, y2, x3, y3, x4, y4):
    root1 = (x1 ** 2) + (y1 ** 2)
    root2 = (x2 ** 2) + (y2 ** 2)
    root3 = (x3 ** 2) + (y3 ** 2)
    root4 = (x4 ** 2) + (y4 ** 2)
    if (root1 + root2) > (root3 + root4):
        return f'({x2}, {y2})({x1}, {y1})'
    elif (root1 + root2) < (root3 + root4):
        return f'({x4}, {y4})({x3}, {y3})'
    else:
        return f'({x2}, {y2})({x1}, {y1})'


y1 = float(input())
z1 = float(input())
y2 = float(input())
z2 = float(input())
y3 = float(input())
z3 = float(input())
y4 = float(input())
z4 = float(input())

print(center_point(int(y1), int(z1), int(y2), int(z2), int(y3), int(z3), int(y4), int(z4)))

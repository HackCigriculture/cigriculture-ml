import json

with open('data/78mm.json', 'r') as _78mm:
    polygons78 = json.load(_78mm)["features"][0]["geometry"]["geometries"]
with open('data/100mm.json', 'r') as _100mm:
    polygons100 = json.load(_100mm)["features"][0]["geometry"]["geometries"]
with open('data/130mm.json', 'r') as _130mm:
    polygons130 = json.load(_130mm)["features"][0]["geometry"]["geometries"]


def dot(x1, y1, x2, y2):
    return x1*y1+x2*y2


def det(x1, y1, x2, y2):
    return x1*y2-x2*y1


def dett(x0, y0, x1, y1, x2, y2):
    z = det(x1-x0, y1-y0, x2-x0, y2-y0)
    return -1 if z < 0 else z > 0
'''
inline DB ang(cPo p0,cPo p1){return acos(dot(p0,p1)/p0.len()/p1.len());}
def ang(x1, y1, x2, y2):
    return 
def arg(x1, y1, x2, y2):
    DB a=ang(x,y);return~dett(x,y)?a:2*PI-a;}
    return
'''


def intersect(lx1, ly1, lx2, ly2, rx1, ry1, rx2, ry2):
    return 1 if (dett(lx1, ly1, lx2, ly2, rx1, ry1) * dett(lx1, ly1, lx2, ly2, rx2, ry2) <= 0 and
                 dett(rx1, ry1, rx2, ry2, lx1, ly1) * dett(rx1, ry1, rx2, ry2, lx2, ly2) <= 0) else 0


def within(p, x, y):
    z = 0
    for i in range(0, len(p)-1):
        if x == p[i][0] and y == p[i][1]:
            continue
        if x == p[i+1][0] and y == p[i+1][1]:
            continue
        z += intersect(x, y, -3232, -4344, p[i][0], p[i][1], p[i+1][0], p[i+1][1])
    return 1 if z % 2 == 1 else 0


def _check(p, d, x, y):
    for i in range(0, len(p)):
        if within(p[i]["coordinates"][0], x, y):
            return [d, i]
    return []


def check(x, y):
    res = _check(polygons78, 78, x, y)
    if len(res) > 0:
        return 0.078
    res = _check(polygons100, 100, x, y)
    if len(res) > 0:
        return 0.1
    res = _check(polygons130, 130, x, y)
    if len(res) > 0:
        return 0.13
    return 1.0

# init()
# #display()
# #x, y = 121.555764, 24.9833
#
# x, y = 121.565764, 24.9830
# res = check(x, y)
# print res
# if (len(res) > 0):
#     if (res[0] == 78):
#         print_polygon(polygons78[res[1]]["coordinates"][0], 'Red')
#     if (res[0] == 100):
#         print_polygon(polygons78[res[1]]["coordinates"][0], 'Orange')
#     if (res[0] == 130):
#         print_polygon(polygons78[res[1]]["coordinates"][0], 'Yellow')
#     plt.plot(x, y, marker='*')
#     ax.grid()
#     ax.axis('equal')
#     plt.show()

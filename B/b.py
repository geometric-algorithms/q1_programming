import matplotlib.pyplot as plt
import sys

def bisect_left(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def insort(a, x):
    i = bisect_left(a, x)
    a.insert(i, x)

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def build_hull(points):
    points = sorted(set(points))
    n=len(points)
    if n<=1:
        return points[:]
    
    #constructing upper hull 
    upper_hull=[]
    for p in points:
        while len(upper_hull) >=2 and cross(upper_hull[-2] , upper_hull[-1] , p) > 0 :
            upper_hull.pop()
        upper_hull.append(p)
    

    #constructing lower hull
    lower_hull=[]
    for p in reversed(points):
        while len(lower_hull) >= 2 and cross(lower_hull[-2] , lower_hull[-1] , p) >= 0 : 
            lower_hull.pop()
        lower_hull.append(p)
    

    #combine lower hull and upper hull where the points are in counter clock wise order
    hull=list(reversed(upper_hull)) + list(reversed(lower_hull))[1:-1]

    return hull


class SegmentTreeNode:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.left = None
        self.right = None
        self.points = []
        self.hull = []


class DynamicConvexHull:
    def __init__(self, XMIN=-10**6, XMAX=10**6):
        self.root = self._build_tree(XMIN, XMAX)

    def _build_tree(self, l, r):
        node = SegmentTreeNode(l, r)
        if r - l > 1:
            m = (l + r) // 2
            node.left = self._build_tree(l, m)
            node.right = self._build_tree(m, r)
        return node

    def insert(self, point):
        self._insert(self.root, point)

    def _insert(self, node, point):
        if node.l <= point[0] < node.r:
            insort(node.points, point)
            node.hull = build_hull(node.points)
            if node.left:
                self._insert(node.left, point)
                self._insert(node.right, point)

    def delete(self, point):
        self._delete(self.root, point)

    def _delete(self, node, point):
        if node.l <= point[0] < node.r:
            idx = bisect_left(node.points, point)
            if idx < len(node.points) and node.points[idx] == point:
                node.points.pop(idx)
                node.hull = build_hull(node.points)
            if node.left:
                self._delete(node.left, point)
                self._delete(node.right, point)

    def get_hull(self):
        return self.root.hull

    def point_on_hull(self, q):
        hull = self.get_hull()
        if q in hull:
            return True
        for i in range(len(hull)):
            a, b = hull[i], hull[(i + 1) % len(hull)]
            if abs(cross(a, q, b)) < 1e-9 and min(a[0], b[0]) <= q[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= q[1] <= max(a[1], b[1]):
                return True
        return False

    def plot_and_print_hull(self):
        hull = self.get_hull()
        pts = sorted(set(self._collect_points(self.root)))

        if not pts:
            print("No points in the structure.")
            return

        print("Convex Hull Points:")
        for p in hull:
            print(p)

        plt.figure(figsize=(8, 6))
        xs, ys = zip(*pts)
        plt.scatter(xs, ys, color='blue', label='Points')

        if len(hull) > 1:
            hx, hy = zip(*(hull + [hull[0]]))
            plt.plot(hx, hy, 'r-', linewidth=2, label='Convex Hull')
        elif hull:
            plt.scatter([hull[0][0]], [hull[0][1]], color='red', s=100, label='Convex Hull')

        for (x, y) in pts:
            plt.annotate(f'({x:.1f},{y:.1f})', (x, y), textcoords="offset points", xytext=(0, 5), ha='center')

        plt.title("Dynamic Convex Hull")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)
        plt.axis('equal')
        plt.show(block=True)

    def _collect_points(self, node):
        if not node:
            return []
        pts = node.points[:]
        if node.left:
            pts += self._collect_points(node.left)
            pts += self._collect_points(node.right)
        return pts


#Menu
if __name__ == '__main__':
    dch = DynamicConvexHull()
    args=sys.argv[1:]
    coordinates=[float(arg) for arg in args]
    points=[]
    for i in range(0,len(coordinates),2):
        points.append([coordinates[i],coordinates[i+1]])


    #insert
    for pt in points:
        dch.insert((pt[0],pt[1]))
    
    while True:
        print("\nOptions:")
        print("1) Insert point")
        print("2) Delete point")
        print("3) Query if point on hull")
        print("4) Print & Plot convex hull")
        print("5) Exit")
        cmd = input("Enter choice: ")
        if cmd == '1':
            x, y = map(float, input("Enter x y: ").split())
            dch.insert((x, y))
            print(f"Inserted ({x}, {y})")
        elif cmd == '2':
            x, y = map(float, input("Enter x y: ").split())
            dch.delete((x, y))
            print(f"Deleted ({x}, {y})")
        elif cmd == '3':
            x, y = map(float, input("Enter x y: ").split())
            print(f"On hull: {dch.point_on_hull((x, y))}")
        elif cmd == '4':
            dch.plot_and_print_hull()
        elif cmd == '5':
            break
        else:
            print("Invalid choice.")


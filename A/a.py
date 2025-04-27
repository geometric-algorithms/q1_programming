import math
import matplotlib.pyplot as plt
import sys
def draw_points(points,color_t):
    x, y = zip(*points)  # Unpack the tuple array into x and y coordinates
    plt.scatter(x, y, color=color_t)
    plt.axis('equal')       # Ensures equal aspect ratio
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    #plt.legend()
    plt.tight_layout()

def draw_polygon(points,color_t):
    x, y = zip(*points)  # Unpack the tuple array into x and y coordinates
    x = list(x) + [x[0]]  # Close the polygon (add the first point at the end)
    y = list(y) + [y[0]]  # Close the polygon (add the first point at the end)
    plt.plot(x, y, color=color_t, marker='o' )

def find_angle(a, b, c):
    ba_x, ba_y = a[0] - b[0], a[1] - b[1]
    bc_x, bc_y = c[0] - b[0], c[1] - b[1]
    dot_product = ba_x * bc_x + ba_y * bc_y
    mag_ba, mag_bc = math.hypot(ba_x, ba_y), math.hypot(bc_x, bc_y)
    if mag_ba == 0 or mag_bc == 0:
        return 0
    cos_theta = max(-1, min(1, dot_product / (mag_ba * mag_bc)))
    return math.degrees(math.acos(cos_theta))

# > ccw or left
# < CW or right
def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def is_tangent(p, prev, curr, nex, upper=True):
    c1, c2 = cross(p, curr, prev), cross(p, curr, nex)
    return (c1 >= 0 and c2 >= 0) if upper else (c1 <= 0 and c2 <= 0)

def binary_search(polygon, point, upper=True):
    n = len(polygon)
    lo, hi = 0, n - 1
    best = None

    while lo <= hi:
        mid = (lo + hi) // 2
        prev = polygon[(mid - 1 + n) % n]
        curr = polygon[mid]
        nex = polygon[(mid + 1) % n]

        if is_tangent(point, prev, curr, nex, upper):
            return curr  

        if upper:
            if cross(point, curr, nex) < 0:
                lo = mid + 1
            else:
                hi = mid - 1
        else:
            if cross(point, curr, nex) > 0:
                lo = mid + 1
            else:
                hi = mid - 1

    return polygon[lo % n] 


def graham_scan(P):
    points = sorted(P, key=lambda p: (p[0], p[1]))
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



def chan_hull(P, m):
    group_hulls=[]
    index_maps=[]
    groups=[]
    color_tuples = [     (1, 0, 0),      (0, 1, 0),       (0, 0, 1),       (1, 1, 0),       (1, 0, 1),       (0, 1, 1),           (0.5, 0.5, 0.5),     (1, 0.5, 0),         (0.5, 0, 0.5),        (0, 0, 0.5),     (0, 0, 1),     (0, 0.5, 0),     (0, 0.5, 0.5),     (0, 0.5, 1),     (0, 1, 0.5),          (0.5, 0, 0),     (0.5, 0, 0.5),     (0.5, 0, 1),     (0.5, 0.5, 0),     (0.5, 0.5, 1),     (0.5, 1, 0),     (0.5, 1, 0.5),     (0.5, 1, 1),          (1, 0, 0.5),     (1, 0.5, 0),     (1, 0.5, 0.5),     (1, 0.5, 1),     (1, 1, 0.5) ] 

    n = len(P)
    g = (n + m - 1) // m
    for i in range(g):
        groups.append(P[i * m:min((i + 1) * m, n)])
        draw_points(groups[i],color_tuples[i])
    plt.pause(1)
    for i in range(g):
        graham_hull = graham_scan(P[i * m:min((i + 1) * m, n)]) 
        group_hulls.append(graham_hull)
        index_map = {tuple(p): idx for idx, p in enumerate(graham_hull)}
        index_maps.append(index_map)
        draw_polygon(graham_hull,color_tuples[i])

    plt.pause(1)
    plt.clf()
    plt.pause(1)

    start = max(P, key=lambda p: (p[0], p[1]))

    hull = [start]
    p_prev = (start[0], 50000)

    for j in range(m):
        best_q = None
        best_cross = float('-inf')

        best_can_q=[]
        for group_id,gh in enumerate(group_hulls):
            if not gh:
                continue

            q1 = binary_search(gh, hull[-1], upper=True)
            q2 = binary_search(gh, hull[-1], upper=False)
            nn=len(gh)
            q_idx = index_maps[group_id].get(tuple(hull[-1]), None)
            if(q_idx):
                q1,q2=gh[(q_idx-1)%nn] , gh[(q_idx+1)%nn]
                
            if(find_angle(p_prev,hull[-1],q1)>find_angle(p_prev,hull[-1],q2)):
                q=q1
            else:
                q=q2
            q_can=q            
            
            best_can_q.append(q_can)
        
        q_angle=-5000
        for qq in best_can_q:
            qq1=find_angle(p_prev,hull[-1],qq)
            
            if(qq1>q_angle):
                best_q=qq
                q_angle=qq1
        
        if best_q == start:
            return hull

        if best_q is None:
            return None

        hull.append(best_q)
        p_prev = hull[-2]
    

    return None


def full_chan_hull_2(P):
    n=len(P)
    if(n<=4):
        return graham_scan(P)
    t=0 
    while True:
        m=min(n , 2**(2**t))
        
        result=chan_hull(P,m)
        if result is not None:
            return result
        t=t+1

def main():
    
    args=sys.argv[1:]
    coordinates=[float(arg) for arg in args]
    points=[]
    for i in range(0,len(coordinates),2):
        points.append([coordinates[i],coordinates[i+1]])
    hull = full_chan_hull_2(points)

    print("Convex Hull (CW order):")
    print(hull)

    lines = hull[:]
    if lines and lines[0] != lines[-1]:
        lines.append(lines[0])

    plt.figure(figsize=(6, 6))
    x_points = [p[0] for p in points]
    y_points = [p[1] for p in points]
    plt.scatter(x_points, y_points, c='red', marker='s', label='Points')
    for p in points:
        plt.text(p[0] + 0.1, p[1], f'({p[0]}, {p[1]})', fontsize=9)
    for i in range(len(lines) - 1):
        x_vals = [lines[i][0], lines[i + 1][0]]
        y_vals = [lines[i][1], lines[i + 1][1]]
        plt.plot(x_vals, y_vals, 'g-', linewidth=2, label='Line Segment' if i == 0 else "")
    for (x, y) in lines:
        plt.scatter(x, y, c='blue', marker='o')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Points with Labels and Connected Line Segments")
    plt.xlim(min(x_points + [x for x, _ in lines]) - 1, max(x_points + [x for x, _ in lines]) + 1)
    plt.ylim(min(y_points + [y for _, y in lines]) - 1, max(y_points + [y for _, y in lines]) + 1)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()

import math

n = int(input())

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(pts):
    points = sorted(pts)
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0: lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0: upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def polygon_area(pts):
    area = 0
    for i in range(len(pts)):
        j = (i + 1) % len(pts)
        area += pts[i][0] * pts[j][1] - pts[i][1] * pts[j][0]
    return abs(area) / 2.0

polygons = []
total = 0
for _ in range(n):
    data = list(map(int, input().split()))
    m = data[0]
    pts = []
    for i in range(1, m * 2 + 1, 2):
        pts.append((data[i], data[i + 1]))
    polygons.append(pts)

    total += polygon_area(pts)


def get_y(p1, p2, x):
    if p1[0] == p2[0]: return p1[1]
    return p1[1] + (p2[1] - p1[1]) * (x - p1[0]) / (p2[0] - p1[0])

def seg_intersect_x(a, b, c, d):
    # Returns the X-coordinate of intersection between segment AB and CD
    cp = (b[0]-a[0])*(d[1]-c[1]) - (b[1]-a[1])*(d[0]-c[0])
    if cp == 0: return []
    t = ((c[0]-a[0])*(d[1]-c[1]) - (c[1]-a[1])*(d[0]-c[0])) / cp
    u = ((c[0]-a[0])*(b[1]-a[1]) - (c[1]-a[1])*(b[0]-a[0])) / cp
    if 0 < t < 1 and 0 < u < 1:
        return [a[0] + t * (b[0]-a[0])]
    return []

def polygon_union_area(polygons):
    events_x = []
    segments = []
    
    for poly in polygons:
        n = len(poly)
        for i in range(n):
            p1, p2 = poly[i], poly[(i+1)%n]
            if p1[0] != p2[0]:
                segments.append((p1, p2))
            events_x.append(p1[0])
            
    for i in range(len(segments)):
        for j in range(i + 1, len(segments)):
            events_x.extend(seg_intersect_x(segments[i][0], segments[i][1], 
                                            segments[j][0], segments[j][1]))
                                            
    events_x.sort()
    area = 0
    
    for i in range(len(events_x) - 1):
        x1, x2 = events_x[i], events_x[i+1]
        if x2 - x1 < 1e-9: continue
        mx = (x1 + x2) / 2 
        
        intervals = []
        for poly in polygons:
            y_vals = []
            n = len(poly)
            for j in range(n):
                pA, pB = poly[j], poly[(j+1)%n]
                if min(pA[0], pB[0]) < mx < max(pA[0], pB[0]):
                    y_vals.append(get_y(pA, pB, mx))
                    
            y_vals.sort()
            for j in range(0, len(y_vals), 2):
                intervals.append((y_vals[j], y_vals[j+1]))
                
        if not intervals: continue
        
        intervals.sort()
        merged_len = 0
        curr_start, curr_end = intervals[0]
        for start, end in intervals[1:]:
            if start < curr_end:
                curr_end = max(curr_end, end)
            else:
                merged_len += curr_end - curr_start
                curr_start, curr_end = start, end
        merged_len += curr_end - curr_start
        
        # Add the trapezoidal area of this vertical strip
        area += (x2 - x1) * merged_len
        
    return area

print(total, polygon_union_area(polygons))
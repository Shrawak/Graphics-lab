def get_clipped_lines(p1,p2,view_size):

    x1, y1 = p1
    x2, y2 = p2

    (x_min,y_min,x_max,y_max) = view_size
 
    p1 = x1-x2
    p2 = -p1
    p3 = y1-y2
    p4 = -p3

    q1 = x1-x_min
    q2 = x_max-x1
    q3 = y1-y_min
    q4 = y_max-y1

    umin=0
    umax=1
    parr = [p1,p2,p3,p4]
    qarr = [q1,q2,q3,q4]

    for (p,q) in zip(parr,qarr):
        if p==0 and q<0:
            return None
        elif p==0 and q>=0:
            continue
        elif p<0:
            umin = max(umin,q/p)
        elif p>0:
            umax = min(umax,q/p)


    if umin>umax:
        accept = False

    x1f = x1 + umin*(x2-x1)
    y1f = y1 + umin*(y2-y1)
    x2f = x1 + umax*(x2-x1)
    y2f = y1 + umax*(y2-y1)

    accept = True
 
    if accept:
        return [(x1f,y1f),(x2f,y2f)]
    else:
        return None


def line_clip(lines,window_frame):
    x_max = max([points[0] for points in window_frame])
    x_min = min([points[0] for points in window_frame])
    y_max = max([points[1] for points in window_frame])
    y_min = min([points[1] for points in window_frame])

    view_size = (x_min,y_min,x_max,y_max)
    
    clipped_points = []
    for line in lines:
        p1,p2 = line[0],line[1]
        clipped_point = get_clipped_lines(p1,p2,view_size)
        clipped_points.append(clipped_point)
    
    return clipped_points


if __name__ == "__main__":
    window_frame = [(20,100),(300,100),(300,300),(20,300)]
    lines = [
        [(100,0),(200,300)],
        [(100,0),(50,130)],
        [(0,0),(200,0)],
    ]

    res = line_clip(lines,window_frame)
    print(res)

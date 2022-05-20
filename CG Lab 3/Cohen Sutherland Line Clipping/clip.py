INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000


 
# Compute Region Code
def get_region_code(x, y, view_size):  
    (x_min,y_min,x_max,y_max) = view_size

    code = INSIDE
    if x < x_min:      
        code |= LEFT
    elif x > x_max:    
        code |= RIGHT
    if y < y_min:     
        code |= BOTTOM
    elif y > y_max:  
        code |= TOP
 
    return code
 
 
def get_clipped_lines(p1,p2,view_size):

    x1, y1 = p1
    x2, y2 = p2

    (x_min,y_min,x_max,y_max) = view_size
    code1 = get_region_code(p1[0],p1[1],view_size)
    code2 = get_region_code(p2[0],p2[1],view_size)
    accept = False
 
    while True:
 
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break
 
        else:
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2
 
            if code_out & TOP:
                x = x1 + (x2 - x1) * \
                                (y_max - y1) / (y2 - y1)
                y = y_max
 
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * \
                                (y_min - y1) / (y2 - y1)
                y = y_min
 
            elif code_out & RIGHT:
                 
                y = y1 + (y2 - y1) * \
                                (x_max - x1) / (x2 - x1)
                x = x_max
 
            elif code_out & LEFT:
                 
                y = y1 + (y2 - y1) * \
                                (x_min - x1) / (x2 - x1)
                x = x_min
 
           
            if code_out == code1:
                x1 = x
                y1 = y
                code1 = get_region_code(x1, y1,view_size)
 
            else:
                x2 = x
                y2 = y
                code2 = get_region_code(x2, y2, view_size)
 
    if accept:
        return [(x1,y1),(x2,y2)]
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

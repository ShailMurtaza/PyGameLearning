x_min = -1
x_max = +1
y_min = -1
y_max = +1
z_min = 1e-5
z_max = 20


#FNTBLR
class CODES:
    INSIDE = 0b000000
    TOP = 0b001000
    BOTTOM = 0b000100
    RIGHT = 0b000010
    LEFT = 0b000001
    FAR = 0b100000
    NEAR = 0b010000

def compute_outcode(x, y, z):
    code = CODES.INSIDE
    
    if x < x_min:
        code |= CODES.LEFT
    elif x > x_max:
        code |= CODES.RIGHT
    
    if y < y_min:
        code |= CODES.BOTTOM
    elif y > y_max:
        code |= CODES.TOP
    
    if z < z_min:
        code |= CODES.NEAR
    elif z > z_max:
        code |= CODES.FAR
    
    return code

def cohen_sutherland_clip(P1, P2):
    x1, y1, z1, w1 = P1
    x2, y2, z2, w2 = P2

    outcode_1 = compute_outcode(x1, y1, z1)
    outcode_2 = compute_outcode(x2, y2, z2)

    while True:
        if outcode_1 == 0 and outcode_2 == 0:
            return ((x1, y1, z1, w1), (x2, y2, z2, w2))
        elif outcode_1 & outcode_2 != 0:
            return None
        else:
            outcode = outcode_1 if outcode_1 != 0 else outcode_2
            x, y, z = 0, 0, 0

            if outcode & CODES.TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
                z = z1 + (z2 - z1) * (y_max - y1) / (y2 - y1)
            elif outcode & CODES.BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
                z = z1 + (z2 - z1) * (y_min - y1) / (y2 - y1)
            elif outcode & CODES.RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
                z = z1 + (z2 - z1) * (x_max - x1) / (x2 - x1)
            elif outcode & CODES.LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min
                z = z1 + (z2 - z1) * (x_min - x1) / (x2 - x1)
            elif outcode & CODES.FAR:
                x = x1 + (x2 - x1) * (z_max - z1) / (z2 - z1)
                y = y1 + (y2 - y1) * (z_max - z1) / (z2 - z1)
                z = z_max
            elif outcode & CODES.NEAR:
                x = x1 + (x2 - x1) * (z_min - z1) / (z2 - z1)
                y = y1 + (y2 - y1) * (z_min - z1) / (z2 - z1)
                z = z_min

            if outcode == outcode_1:
                x1, y1, z1 = x, y, z
                outcode_1 = compute_outcode(x1, y1, z1)
            else:
                x2, y2, z2 = x, y, z
                outcode_2 = compute_outcode(x2, y2, z2)

#FNTBLR
class CODES:
    INSIDE = 0b000000
    TOP = 0b001000
    BOTTOM = 0b000100
    RIGHT = 0b000001
    LEFT = 0b000010
    FAR = 0b100000
    NEAR = 0b010000

def compute_outcode(x, y, z, w):
    # print("------------------")
    code = CODES.INSIDE
    
    if x < -w:
        code |= CODES.LEFT
        # print(f"{x, w} Left Out")
    elif x > w:
        code |= CODES.RIGHT
        # print(f"{x, w} Right Out")
    
    if y < -w:
        code |= CODES.BOTTOM
        # print(f"{y, w} Bottom Out")
    elif y > w:
        code |= CODES.TOP
        # print(f"{y, w} Top Out")
    
    if z < -w:
        code |= CODES.NEAR
        # print(f"{z, w} Near Out")
    elif z > w:
        code |= CODES.FAR
        # print(f"{z, w}  Far Out")
    # print("------------------\n")
    return code

def cohen_sutherland_clip(P1, P2):
    x1, y1, z1, w1 = P1
    x2, y2, z2, w2 = P2

    outcode_1 = compute_outcode(x1, y1, z1, w1)
    outcode_2 = compute_outcode(x2, y2, z2, w2)

    while True:
        if outcode_1 == 0 and outcode_2 == 0:
            return ((x1, y1, z1, w1), (x2, y2, z2, w2))
        elif outcode_1 & outcode_2 != 0:
            return None
        else:
            # print("CLIPPING")
            # input("")
            outcode = outcode_1 if outcode_1 != 0 else outcode_2
            x, y, z = 0, 0, 0

            if outcode & CODES.TOP:
                t = (w1 - y1) / (y2 - y1)
                x = x1 + (x2 - x1) * t
                y = w1
                z = z1 + (z2 - z1) * t
            elif outcode & CODES.BOTTOM:
                t = (-w1 - y1) / (y2 - y1)
                x = x1 + (x2 - x1) * t
                y = -w1
                z = z1 + (z2 - z1) * t
            elif outcode & CODES.RIGHT:
                t = (w1 - x1) / (x2 - x1)
                x = w1
                y = y1 + (y2 - y1) * t
                z = z1 + (z2 - z1) * t
            elif outcode & CODES.LEFT:
                t = (-w1 - x1) / (x2 - x1)
                x = -w1
                y = y1 + (y2 - y1) * t
                z = z1 + (z2 - z1) * t
            elif outcode & CODES.FAR:
                t = (w1 - z1) / (z2 - z1)
                x = x1 + (x2 - x1) * t
                y = y1 + (y2 - y1) * t
                z = w1
            elif outcode & CODES.NEAR:
                t = (-w1 - z1) / (z2 - z1)
                x = x1 + (x2 - x1) * t
                y = y1 + (y2 - y1) * t
                z = -w1

            if outcode == outcode_1:
                x1, y1, z1 = x, y, z
                outcode_1 = compute_outcode(x1, y1, z1, w1)
            elif outcode == outcode_2:
                x2, y2, z2 = x, y, z
                outcode_2 = compute_outcode(x2, y2, z2, w2)


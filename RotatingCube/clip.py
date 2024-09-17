# Constants for outcodes
LEFT   = 0b000001  # x < -w
RIGHT  = 0b000010  # x > w
BOTTOM = 0b000100  # y < -w
TOP    = 0b001000  # y > w
NEAR   = 0b010000  # z < -w
FAR    = 0b100000  # z > w

near = 0.1
far = 10

# Function to compute the outcode for a point
def compute_outcode(x, y, z, w):
    outcode = 0
    if x < -w:
        outcode |= LEFT
        # print(f"{x, y, z, w} Left Out")
    elif x > w:
        outcode |= RIGHT
        # print(f"{x, y, z, w} Right Out")
    if y < -w:
        outcode |= BOTTOM
        # print(f"{x, y, z, w} Bottom Out")
    elif y > w:
        outcode |= TOP
        # print(f"{x, y, z, w} Top Out")
    if z < -w:
        outcode |= NEAR
        # print(f"{x, y, z, w} Near Out")
    elif z > w:
        outcode |= FAR
        # print(f"{x, y, z, w} Far Out")
    return outcode

# Cohen-Sutherland 3D line clipping algorithm
def cohen_sutherland_clip(P1, P2):
    x1, y1, z1, w1 = P1
    x2, y2, z2, w2 = P2

    # Compute outcodes for both points
    outcode1 = compute_outcode(x1, y1, z1, w1)
    outcode2 = compute_outcode(x2, y2, z2, w2)
    i = 0
    while True:
        if i == 10:
            exit()
        i += 1
        # print("-----------")
        # Trivial acceptance (both outcodes are zero)
        if outcode1 == 0 and outcode2 == 0:
            # print("Done Clipping")
            # print("-----------\n")
            return ((x1, y1, z1, w1), (x2, y2, z2, w2))
        
        # Trivial rejection (logical AND is not zero)
        if (outcode1 & outcode2) != 0:
            # print("Rejected")
            # print("-----------\n")
            return None
        
        # Choose one point outside the clipping region
        if outcode1 != 0:
            outcode_out = outcode1
        else:
            outcode_out = outcode2

        x, y, z, w = 0, 0, 0, 0
        
        # Clip point against the appropriate plane
        if outcode_out & LEFT:  # Clip against left plane (x = -w)
            t = (-w1 - x1) / ((x2 - x1) + (w2 - w1))
            y = y1 + t * (y2 - y1)
            z = z1 + t * (z2 - z1)
            w = w1 + t * (w2 - w1)
            x = -w

        elif outcode_out & RIGHT:  # Clip against right plane (x = w)
            t = (w1 - x1) / ((x2 - x1) - (w2 - w1))
            y = y1 + t * (y2 - y1)
            z =  z1 + t * (z2 - z1)
            w = w1 + t * (w2 - w1)
            x = w
            # print("Right Clipped: ", x, y, z, w)

        elif outcode_out & BOTTOM:  # Clip against bottom plane (y = -w)
            t = (-w1 - y1) / ((y2 - y1) + (w2 - w1))
            x = x1 + t * (x2 - x1)
            z = z1 + t * (z2 - z1)
            w = w1 + t * (w2 - w1)
            y = -w

        elif outcode_out & TOP:  # Clip against top plane (y = w)
            t = (w1 - y1) / ((y2 - y1) - (w2 - w1))
            x = x1 + t * (x2 - x1)
            z = z1 + t * (z2 - z1)
            w = w1 + t * (w2 - w1)
            y = w

        elif outcode_out & NEAR:  # Clip against near plane (z = -w)
            t = (-w1 - z1) / ((z2 - z1) + (w2 - w1))
            x  =x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            w = w1 + t * (w2 - w1)
            z = -w

        elif outcode_out & FAR:  # Clip against far plane (z = w)
            t = (w1 - z1) / ((z2 - z1) - (w2 - w1))
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            w = w1 + t * (w2 - w1)
            z = w
        # Update the point that was outside and recalculate the outcode
        if outcode_out == outcode1:
            x1, y1, z1, w1 = x, y, z, w
            print("Clipped P1")
            print(f"({x1}, {y1}, {z1}, {w1}), ({x2}, {y2}, {z2}, {w2})")
            print("-----------\n")
            outcode1 = compute_outcode(x1, y1, z1, w1)
        else:
            x2, y2, z2, w2 = x, y, z, w
            print("Clipped P2")
            print(f"({x1}, {y1}, {z1}, {w1}), ({x2}, {y2}, {z2}, {w2})")
            print("-----------\n")
            outcode2 = compute_outcode(x2, y2, z2, w2)

def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    return (x1 < x2 < x1 + w1 or x1 < x2 + w2 < x1 + w1 and y1 < y2 < y1 + h1 or y1 < y2 + h2 < y1 + h1)
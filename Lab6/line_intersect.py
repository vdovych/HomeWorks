def line_intersect(line1, line2):
    '''

    :param line1: ((x1,y1),(x2,y2))
    :param line2: ((x1,y1),(x2,y2)
    :return:
    '''
    k1 = (line1[0][1]-line1[1][1])/(line1[0][0]-line1[1][0])
    k2 = (line2[0][1]-line2[1][1])/(line2[0][0]-line2[1][0])
    b1 = line1[0][1] - k1 * line1[0][1]
    b2 = line2[0][1] - k2 * line2[0][1]
    if k1 == k2:
        if b1 == b2:
            return line1 #Why?
        return None
    xi = (b1-b2)/(k1-k2)
    yi = b1 + k1 * xi
    return xi, yi

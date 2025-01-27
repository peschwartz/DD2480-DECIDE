# util functions go here

# Function to calculate the distance between two points given their x,y coordinates
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Function to calculate the area of a triangle given 3 x,y coordinates
def triangle_area(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

# Function to calculate if the 3 points (tuples) fit in a circle given the radius
def fit_in_circle(p1, p2, p3, radius):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    # calculate the center of the circle
    x_center = (x1 + x2 + x3) / 3
    y_center = (y1 + y2 + y3) / 3

    dist = []
    # calculate the distance between the center and each of the points
    dist.append(distance(x_center, y_center, x1, y1))
    dist.append(distance(x_center, y_center, x2, y2))
    dist.append(distance(x_center, y_center, x3, y3))

    for i in dist:
        # if one of the distances between the center and each of the points is greater than the radius
        # then the points do not fit in the circle and return false
        if i > radius:
            return False
    
    return True

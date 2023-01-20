import math


def get_angle(point_1, point_2):
    return math.atan2(point_2[1] - point_1[1], point_2[0] - point_1[0])

def get_distance(point_1, point_2):
    return math.dist(point_1, point_2)

def get_midpoint(point_1, point_2):
    return [(point_1[0] + point_2[0]) * 0.5, (point_1[1] + point_2[1]) * 0.5]

def clamp(value, minimum, maximum):
    return max(min(value, maximum), minimum)

def get_slope_intercept(line_a):
    slope = (line_a[1][1] - line_a[0][1]) / (line_a[1][0] - line_a[0][0])
    y_intercept = line_a[0][1] - slope * line_a[0][0]
    return slope, y_intercept

# two 2d lines
def get_intersection(line_1, line_2):
    slope_1, y_intercept_1 = get_slope_intercept(line_1)
    slope_2, y_intercept_2 = get_slope_intercept(line_2)
    intersection_x = (y_intercept_2 - y_intercept_1) / (slope_1 - slope_2)
    intersection_y = slope_1 * intersection_x + y_intercept_1
    return intersection_x, intersection_y

def lerp(value_1, value_2, percentage):
    return value_1 + (value_2 - value_1) * percentage

def lerp_2D(point_1, point_2, percentage):
    return [lerp(point_1[0], point_2[0]), lerp(point_1[1], point_2[1])]
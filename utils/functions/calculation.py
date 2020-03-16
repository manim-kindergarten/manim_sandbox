# from @pdcxs

# get_intersect function calculates the intersect position of two lines
# when two lines are paralleled to each other
# it will return `parallel` parameter
# For example: 
# dot = Dot()
# dot.add_updater(lambda m: m.move_to(get_intersect(line1, line2, LEFT * 100))

def get_intersect(line1, line2, parallel):
    p1, p2 = line1.get_start_and_end()
    p3, p4 = line2.get_start_and_end()

    # Line1 is a1*x+b1*y=c1
    a1 = p2[1] - p1[1]
    b1 = p1[0] - p2[0]
    c1 = a1 * p1[0] + b1 * p1[1]

    # Line2 is a2*x+b2*y=c2
    a2 = p4[1] - p3[1]
    b2 = p3[0] - p4[0]
    c2 = a2 * p3[0] + b2 * p3[1]

    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        return parallel
    else:
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        return x * RIGHT + y * UP

# some useful rate functions
import math

def easeOutBounce(t):
    if t < 1 / 2.75:
        return 7.5625 * t * t
    elif t < 2 / 2.75:
        c = t - 1.5/2.75
        return 7.5625 * c * c + 0.75
    elif t < 2.5 / 2.75:
        c = t - 2.25 / 2.75
        return 7.5625 * c * c + .9375
    else:
        c = t - 2.625 / 2.75
        return 7.5625 * c * c + .984375

def easeInBounce(t):
    return 1 - easeOutBounce(1 - t)

def easeInOutBounce(t):
    if t < 0.5:
        return easeInBounce(2 * t)
    else:
        return easeOutBounce(2 * t - 1)
    
# Because easeOutElastic function will return
# value greater than 1
# There has some requirements:
# 1. Cannot be used in MoveAlongPath animation, because
#    points_from_proportion will crash.
# 2. Need to remove all the np.clip functions in
#    manimlib/animation/animation.py, i.e. change
#    the code of get_sub_alpha and interpolate methods
#    from `return np.clip((value - lower), 0, 1)`
#    to `value - lower`
#    and remove `alpha = np.clip(alpha, 0, 1)`, respectively.`

def easeOutElastic(t):
    s, a = 1.70158, 1
    
    if t == 0: return 0
    if t == 1: return 1

    p = 0.3
    if a < 1:
        a, s = 1, p / 4
    else:
        s = p / (2 * math.pi) * math.asin(1 / a)

    return a * pow(2, -10 * t) * math.sin((t - s) * (2 * math.pi) / p) + 1

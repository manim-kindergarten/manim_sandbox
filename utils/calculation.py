# from @pdcxs
# This function calculates the intersect position of two lines
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

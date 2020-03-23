# from @MATHEART_EVER & @我是害羞的向量

# 由MATHEART_EVER和我是害羞的向量制作，使用该类做的视频请注明作者
# 参考链接I：https://zh.wikipedia.org/wiki/%E5%86%85%E5%88%87%E5%9C%86
# 参考链接II: https://www.cnblogs.com/BigBigLiang/p/4789086.html
# 功能：支持求三角形的周长，面积，五心，以及内切圆，外接圆，旁切圆，欧拉圆等
from manimlib.imports import *

class MyTriangle(Polygon):
    def get_side_length(self): # 三角形边长
        A, B, C = Polygon.get_vertices(self)

        a = math.sqrt((B[0]-C[0])**2 + (B[1]-C[1])**2)
        b = math.sqrt((A[0]-C[0])**2 + (A[1]-C[1])**2) 
        c = math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)

        return np.array([a,b,c])

    def get_three_angle(self): #三个角
        a, b, c = self.get_side_length()
        AngleA = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        AngleB = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
        AngleC = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
        return AngleA, AngleB, AngleC

    def get_circumference(self): # 周长
        a, b, c = self.get_side_length()
        return (a + b + c)

    def get_area(self): # 面积
        a, b, c = self.get_side_length()
        p = (a+b+c) / 2
        return math.sqrt(p*(p-a)*(p-b)*(p-c))

    def get_orthocenter(self): # 垂心坐标
        A, B, C = Polygon.get_vertices(self)
        a, b, c = self.get_side_length()
        AngleA, AngleB, AngleC = self.get_three_angle()
        Ax, Ay = A[0], A[1]
        Bx, By = B[0], B[1]
        Cx, Cy = C[0], C[1]

        xup = a / math.cos(AngleA) * Ax + b / math.cos(AngleB) * Bx + c / math.cos(AngleC) * Cx
        yup = a / math.cos(AngleA) * Ay + b / math.cos(AngleB) * By + c/ math.cos(AngleC) * Cy
        down = a / math.cos(AngleA) + b / math.cos(AngleB) + c / math.cos(AngleC)
        return np.array([xup/down,yup/down,0])

    def get_centroid(self): # 重心坐标
        A, B, C = Polygon.get_vertices(self)
        Ax, Ay = A[0], A[1]
        Bx, By = B[0], B[1]
        Cx, Cy = C[0], C[1]
        return np.array([(Ax + Bx + Cx) / 3, (Ay + By + Cy) / 3, 0])

    def get_circumcenter(self): # 外心坐标
        A, B, C = Polygon.get_vertices(self)
        AngleA, AngleB, AngleC = self.get_three_angle()
        Ax, Ay = A[0], A[1]
        Bx, By = B[0], B[1]
        Cx, Cy = C[0], C[1]

        xup = Ax * math.sin(2 * AngleA) + Bx * math.sin(2 * AngleB) + Cx * math.sin(2 * AngleC)
        yup = Ay * math.sin(2 * AngleA) + By * math.sin(2 * AngleB) + Cy * math.sin(2 * AngleC)
        down = math.sin(2 * AngleA) + math.sin(2 * AngleB) + math.sin(2 * AngleC) 
        return np.array([xup/down, yup/down, 0])

    def get_incenter(self): # 内心坐标
        A, B, C = Polygon.get_vertices(self)
        a, b, c = self.get_side_length()
        Ax, Ay = A[0], A[1]
        Bx, By = B[0], B[1]
        Cx, Cy = C[0], C[1]

        x = (a * Ax + b * Bx + c * Cx) / (a + b + c)
        y = (a * Ay + b * By + c * Cy) / (a + b + c)

        return np.array([x, y, 0])

    def get_excenter(self): # 旁心坐标
        A, B, C = Polygon.get_vertices(self)
        a, b, c = self.get_side_length()
        Ax, Ay = A[0], A[1]
        Bx, By = B[0], B[1]
        Cx, Cy = C[0], C[1]

        Ja_x = (-a * Ax + b * Bx + c * Cx) / (-a + b + c)
        Ja_y = (-a * Ay + b * By + c * Cy) / (-a + b + c)
        Jb_x = (a * Ax - b * Bx + c * Cx) / (a - b + c)
        Jb_y = (a * Ay - b * By + c * Cy) / (a - b + c)
        Jc_x = (a * Ax + b * Bx - c * Cx) / (a + b - c)
        Jc_y = (a * Ay + b * By - c * Cy) / (a + b - c)

        return np.array([Ja_x, Ja_y, 0]), np.array([Jb_x, Jb_y, 0]), np.array([Jc_x, Jc_y, 0])

    def get_incircle_radius(self): # 内切圆半径
        a, b, c = self.get_side_length()
        # 1/2 * (a+b+c) * r = S
        # r = S*2/(a+b+c)
        return self.get_area()*2/(a+b+c)

    def get_incircle(self): # 内切圆                 
        return Circle(radius = self.get_incircle_radius()).move_to(self.get_incenter())

    def get_excircle_radius(self): # 旁切圆半径
        S = self.get_area()
        a, b, c = self.get_side_length()
        return 2*S/(-a+b+c), 2*S/(a-b+c), 2*S/(a+b-c)

    def get_excircle(self): # 旁切圆
        radius_ = self.get_excircle_radius()
        J = self.get_excenter()
        return [Circle(radius = radius_[i]).move_to(J[i]) for i in range(3)]

    def get_circumcircle(self): # 外接圆
        A, B, C = Polygon.get_vertices(self)
        Ax, Ay = A[0], A[1]
        circumcenter = self.get_circumcenter()
        circumradius = math.sqrt((Ax-circumcenter[0])**2 + (Ay-circumcenter[1])**2)
        return Circle(radius = circumradius).move_to(circumcenter)

    def get_O9Circle(self): # 九点圆
        A, B, C = Polygon.get_vertices(self)
        Ax, Ay = A[0], A[1]
        Bx, By = B[0], B[1]
        Cx, Cy = C[0], C[1]
        H = self.get_orthocenter()
        Hx, Hy = H[0], H[1]

        M_a = np.array([(Ax+Hx)/2,(Ay+Hy)/2,0])
        M_b = np.array([(Bx+Hx)/2,(By+Hy)/2,0])
        M_c = np.array([(Cx+Hx)/2,(Cy+Hy)/2,0])

        O9Center = MyTriangle(M_a, M_b, M_c).get_circumcenter()
        O9Radius = math.sqrt((O9Center[0] - M_a[0]) ** 2 + (O9Center[1] - M_a[1]) ** 2)
        return Circle(radius = O9Radius).move_to(O9Center)
    
    def get_O9Center(self): # 九点圆圆心
        return self.get_O9Circle().get_center()

    def get_O9Radius(self): # 九点圆半径
        return self.get_O9Circle().radius
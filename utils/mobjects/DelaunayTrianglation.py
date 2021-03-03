# from @有一种悲伤叫颓废

"""
注：
    1. 主要用来求三角剖分和维诺图，算法的思路可以看我的这期视频：https://www.bilibili.com/video/BV1Ck4y1z7VT
    2. 时间复杂度O(nlogn)，一般情况应该够用，如发现bug请联系颓废
    3. 只需导入两个函数：DelaunayTrianglation(求德劳内三角剖分), Voronoi(求维诺图)
"""


import numpy as np
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.constants import PI
from manimlib.utils.config_ops import digest_config
from manimlib.mobject.geometry import Dot, Line, Polygon
from manimlib.scene.scene import Scene
from manimlib.utils.space_ops import normalize
#import time
#import math
#from manimlib.imports import *
#from manim_sandbox.utils.imports import *


# 以下比例建议2不要乱改，精度大，或者小，都有可能出bug
# 小于误差则等
ev = np.exp(1)**PI/1000000000
ev_sq = ev**2

# 无穷大
Infinity = 333

# 判断两个点是否相等，小于误差的平方，则相等，O(1)
def point_is_equal(p, q):
    p, q = np.array(p), np.array(q)
    # 两点距离的平方小于误差的平方，则相等
    if np.dot(q-p, q-p) < ev_sq:
        return True
    return False

# b在向量pq左为正，右为负，O(1)
def cross2(p, q, b):
    '''
    叉积公式
    \begin{align}
    ToLeft(p, q, b)=\begin{vmatrix}
    x_p & y_p & 1\\
    x_q & y_q & 1\\
    x_b & y_b & 1\\
    \end{vmatrix}\end{align}
    '''
    return p[0]*q[1] - p[1]*q[0] + \
           q[0]*b[1] - q[1]*b[0] + \
           b[0]*p[1] - b[1]*p[0]

# 忽略误差，b在向量pq左为正，右为负，O(1)
def ToLeft(p, q, b):
    a = cross2(p, q, b)
    # 小于误差，认为在向量上
    if abs(a) < ev:
        return 0
    # 隐含else abs(a) >= ev:
    return a

# 点d在三角形pqb内，返回True，O(1)
def InTriangle(p, q, b, d):
    tl1 = ToLeft(p, q, d)
    if abs(tl1) < ev:
        tl2 = ToLeft(q, b, d)
        tl3 = ToLeft(b, p, d)
        if tl2 < ev and tl3 < ev or tl2 > -ev and tl3 > -ev:
            return True
        return False
    if tl1 > ev:
        if ToLeft(q, b, d) > -ev and ToLeft(b, p, d) > -ev:
            return True
        return False
    if tl1 < -ev:
        if ToLeft(q, b, d) < ev and ToLeft(b, p, d) < ev:
            return True
        return False

# 点d在三点p,q,b的外接圆内，返回True，O(1)
def InCircle(p, q, b, d):
    '''
    点与三点圆关系
    \begin{align}
    InCircle(p, q, b, d)=\begin{vmatrix}
    x_p & y_p & x_p^2+y_p^2 & 1\\
    x_q & y_q & x_q^2+y_q^2 & 1\\
    x_b & y_b & x_b^2+y_b^2 & 1\\
    x_d & y_d & x_d^2+y_d^2 & 1\\
    \end{vmatrix}\end{align}
    '''
    a13 = p[0]**2+p[1]**2
    a23 = q[0]**2+q[1]**2
    a33 = b[0]**2+b[1]**2
    a43 = d[0]**2+d[1]**2
    det = np.linalg.det([
        [p[0], p[1], a13, 1],
        [q[0], q[1], a23, 1],
        [b[0], b[1], a33, 1],
        [d[0], d[1], a43, 1],
    ])
    if det < -ev:
        return True
    return False

# 三点外接圆圆心，O(1)
def CircumcircleCenter(p, q, b):
    '''
    \begin{align}
    &三点外接圆圆心公式\\
    &x=\frac{1}{2}\begin{vmatrix}
    1 & x_p^2+y_p^2 & y_p\\
    1 & x_q^2+y_q^2 & y_q\\
    1 & x_b^2+y_b^2 & y_b\\
    \end{vmatrix}/\begin{vmatrix}
    1 & x_p & y_p\\
    1 & x_q & y_q\\
    1 & x_b & y_b\\
    \end{vmatrix}\\
    &y=\frac{1}{2}\begin{vmatrix}
    1 & x_p & x_p^2+y_p^2\\
    1 & x_q & x_q^2+y_q^2\\
    1 & x_b & x_b^2+y_b^2\\
    \end{vmatrix}/\begin{vmatrix}
    1 & x_p & y_p\\
    1 & x_q & y_q\\
    1 & x_b & y_b\\
    \end{vmatrix}
    \end{align}
    '''
    a1 = p[0]**2+p[1]**2
    a2 = q[0]**2+q[1]**2
    a3 = b[0]**2+b[1]**2
    det1 = np.linalg.det([
        [1, p[0], p[1]],
        [1, q[0], q[1]],
        [1, b[0], b[1]],
    ])
    if det1 == 0:
        print("三点共线")
        return None
    det2 = np.linalg.det([
        [1, a1, p[1]],
        [1, a2, q[1]],
        [1, a3, b[1]],
    ])
    det3 = np.linalg.det([
        [1, p[0], a1],
        [1, q[0], a2],
        [1, b[0], a3],
    ])
    return np.array([det2/det1, det3/det1, 0])/2

# 面
class Face():
    def __init__(self, halfedge):
        # 标记访问面
        self.Visit = False
        # 属于这个面的一个半边
        self.HalfEdge = halfedge
        # 面对应的桶
        self.Bucket = None
        # 外接圆圆心，求维诺图的时候用到
        self.Center = None

# 顶点
class Vertice():
    def __init__(self, point):
        # 顶点坐标
        self.Point = point
        # 由顶点引出的一条半边
        self.HalfEdge = None

# 半边
class HalfEdge():
    def __init__(self, start, end):
        # 标记访问
        self.Visit = False
        # 边的起点
        self.Start = start
        # 边的终点
        self.End = end
        # 边的孪生兄弟
        self.Twin = None
        # 半边所在的平面
        self.Face = None
        # 边的前驱
        self.Pre = None
        # 边的后继
        self.Suc = None

# 桶
class Bucket():
    def __init__(self, points):
        # 桶装的点
        self.Points = points
        # 桶对应的面
        self.Face = None

# 初始化无穷大的网，O(1)
def InitInfNet(points = None):
    # 初始化无穷远点
    # 逆时针
    infv1 = Vertice(np.array([Infinity, 0, 0]))
    infv2 = Vertice(np.array([0, Infinity, 0]))
    infv3 = Vertice(np.array([-Infinity, -Infinity, 0]))

    # 初始化无穷远半边
    halfedge1 = HalfEdge(infv1, infv2)
    halfedge2 = HalfEdge(infv2, infv3)
    halfedge3 = HalfEdge(infv3, infv1)

    # 初始化点引出的边
    infv1.HalfEdge = halfedge1
    infv2.HalfEdge = halfedge2
    infv3.HalfEdge = halfedge3

    # 初始化无穷大面
    face1 = Face(halfedge1)

    # 初始化无穷半边的前驱，后继，和所在的面
    halfedge1.Pre = halfedge3
    halfedge1.Suc = halfedge2
    halfedge1.Face = face1

    halfedge2.Pre = halfedge1
    halfedge2.Suc = halfedge3
    halfedge2.Face = face1

    halfedge3.Pre = halfedge2
    halfedge3.Suc = halfedge1
    halfedge3.Face = face1

    # 初始化桶，此桶囊括了所有的点
    bucket1 = Bucket(points)
    bucket1.Face = face1

    # 面对应的桶
    face1.Bucket = bucket1

    return face1

# 得到多边形的带符号面积，对于不自交的多边形，正表示逆时针多边形，负表示顺时针多边形，特殊考虑0，O(n)
def get_polygon_directed_area(polygon):
    a = polygon.get_vertices()
    l = len(a)
    return 1 / 2 * sum([a[i][0] * a[(i + 1) % l][1] - a[(i + 1) % l][0] * a[i][1] for i in range(l)])

# 边翻转，O(1)
def EdgeFlipping(halfedge):
    # 记录面的旧visit值
    visitvalue = halfedge.Face.Visit
    # 待翻转边所在的四边形的顶点
    v1 = halfedge.Start
    v2 = halfedge.Twin.Suc.End
    v3 = halfedge.End
    v4 = halfedge.Suc.End
    # 顶点的坐标
    p1 = v1.Point
    p2 = v2.Point
    p3 = v3.Point
    p4 = v4.Point
    # 待翻转边所在的四边形的边，ei由vi引出
    e1 = halfedge.Twin.Suc
    e2 = halfedge.Twin.Pre
    e3 = halfedge.Suc
    e4 = halfedge.Pre
    # 修改顶点引出的边为非翻转的边（待翻转边所在的四边形的边）
    v1.HalfEdge = e1
    v2.HalfEdge = e2
    v3.HalfEdge = e3
    v4.HalfEdge = e4

    # 待翻转边所在的四边形的两个桶中的点
    oldpoints = [*halfedge.Face.Bucket.Points, *halfedge.Twin.Face.Bucket.Points]
    # 重新分桶
    newpoints1, newpoints2 = [], []
    for oldpoint in oldpoints:
        if InTriangle(p1, p2, p4, oldpoint):
            newpoints1.append(oldpoint)
        else:
            newpoints2.append(oldpoint)

    # 重新构造的面，逆时针
    newface1, newface2 = Face(e1), Face(e2)
    newface1.Visit = visitvalue
    newface2.Visit = visitvalue

    # 构造翻转后的边
    e5, e6 = HalfEdge(v2, v4), HalfEdge(v4, v2)
    e5.Twin = e6
    e6.Twin = e5
    e5.Visit = visitvalue
    e6.Visit = visitvalue

    # 构造newface1的边
    e1.Suc = e5
    e5.Suc = e4
    e4.Suc = e1
    e1.Pre = e4
    e4.Pre = e5
    e5.Pre = e1
    # 构造newface2的边
    e2.Suc = e3
    e3.Suc = e6
    e6.Suc = e2
    e2.Pre = e6
    e6.Pre = e3
    e3.Pre = e2

    # 边指向newface1
    e1.Face = newface1
    e4.Face = newface1
    e5.Face = newface1
    # 边指向newface2
    e2.Face = newface2
    e3.Face = newface2
    e6.Face = newface2


    # 构造两个新桶，并维持桶和面的联系
    bucket1 = Bucket(newpoints1)
    bucket2 = Bucket(newpoints2)
    bucket1.Face = newface1
    bucket2.Face = newface2
    newface1.Bucket = bucket1
    newface2.Bucket = bucket2

# 点vo撕裂面face，O(1)
def ClipFace(face, vo, remainedpoints):
    visitvalue = face.Visit
    hf1 = face.HalfEdge
    hf2 = hf1.Suc
    hf3 = hf2.Suc

    # 剪开面
    clipface1 = Face(hf1)
    clipface2 = Face(hf2)
    clipface3 = Face(hf3)
    clipface1.Visit = visitvalue
    clipface2.Visit = visitvalue
    clipface3.Visit = visitvalue

    # face1
    hf1_pre = HalfEdge(vo, hf1.Start)
    hf1_suc = HalfEdge(hf1.End, vo)
    hf1_pre.Visit = visitvalue
    hf1_suc.Visit = visitvalue
    hf1.Pre = hf1_pre
    hf1.Suc = hf1_suc
    hf1_pre.Pre = hf1_suc
    hf1_pre.Suc = hf1
    hf1_suc.Pre = hf1
    hf1_suc.Suc = hf1_pre
    hf1.Face = clipface1
    hf1_pre.Face = clipface1
    hf1_suc.Face = clipface1

    # face2
    hf2_pre = HalfEdge(vo, hf2.Start)
    hf2_suc = HalfEdge(hf2.End, vo)
    hf2_pre.Visit = visitvalue
    hf2_suc.Visit = visitvalue
    hf2.Pre = hf2_pre
    hf2.Suc = hf2_suc
    hf2_pre.Pre = hf2_suc
    hf2_pre.Suc = hf2
    hf2_suc.Pre = hf2
    hf2_suc.Suc = hf2_pre
    hf2.Face = clipface2
    hf2_pre.Face = clipface2
    hf2_suc.Face = clipface2

    # face3
    hf3_pre = HalfEdge(vo, hf3.Start)
    hf3_suc = HalfEdge(hf3.End, vo)
    hf3_pre.Visit = visitvalue
    hf3_suc.Visit = visitvalue
    hf3.Pre = hf3_pre
    hf3.Suc = hf3_suc
    hf3_pre.Pre = hf3_suc
    hf3_pre.Suc = hf3
    hf3_suc.Pre = hf3
    hf3_suc.Suc = hf3_pre
    hf3.Face = clipface3
    hf3_pre.Face = clipface3
    hf3_suc.Face = clipface3

    vo.HalfEdge = hf1_pre

    # twin
    hf1_pre.Twin = hf3_suc
    hf3_suc.Twin = hf1_pre

    hf2_pre.Twin = hf1_suc
    hf1_suc.Twin = hf2_pre

    hf3_pre.Twin = hf2_suc
    hf2_suc.Twin = hf3_pre

    ## 点放入桶
    # 桶所在三角形的顶点
    point = vo.Point
    p1 = hf1.Start.Point
    p2 = hf2.Start.Point
    p3 = hf3.Start.Point

    # 拆分桶
    clipbucketps1, clipbucketps2, clipbucketps3 = [], [], []
    for eachpoint in remainedpoints:
        if InTriangle(p1, p2, point, eachpoint):
            clipbucketps1.append(eachpoint)
        elif InTriangle(p2, p3, point, eachpoint):
            clipbucketps2.append(eachpoint)
        else:
            clipbucketps3.append(eachpoint)

    # 撕裂的平面关联桶
    clipbucket1 = Bucket(clipbucketps1)
    clipbucket2 = Bucket(clipbucketps2)
    clipbucket3 = Bucket(clipbucketps3)
    clipface1.Bucket = clipbucket1
    clipface2.Bucket = clipbucket2
    clipface3.Bucket = clipbucket3
    clipbucket1.Face = clipface1
    clipbucket2.Face = clipface2
    clipbucket3.Face = clipface3

    return clipface1, clipface2, clipface3

# 访问网，O(n)
def VisitNet(face):
    visitvalue = face.Visit
    notvisitvalue = not visitvalue
    faces = [face]
    # 访问过
    face.Visit = notvisitvalue

    delaunaynet = []

    while faces:
        eachface = faces[-1]
        faces.pop(-1)
        # 面所在的三条边
        e1 = eachface.HalfEdge
        e2 = e1.Suc
        e3 = e2.Suc
        ## 将正在访问的面的三个相邻的面加入faces
        eis = [e1, e2, e3]
        for ei in eis:
            # ei的孪生兄弟
            eiTwin = ei.Twin
            # ei未被访问过
            if ei.Visit == visitvalue:
                ls, le = ei.Start.Point, ei.End.Point
                if abs(ls[0]) != Infinity and abs(ls[1]) != Infinity and abs(le[0]) != Infinity and abs(le[1]) != Infinity:
                    delaunaynet.append([ls, le])
                ei.Visit = notvisitvalue
                if eiTwin:
                    faces.append(eiTwin.Face)
                    # 访问过
                    eiTwin.Face.Visit = notvisitvalue
                    eiTwin.Visit = notvisitvalue

    return delaunaynet

# 访问三角形，O(n)
def VisitTriangles(face):
    # 访问网
    visitvalue = face.Visit
    notvisitvalue = not visitvalue
    faces = [face]
    # 访问过
    face.Visit = notvisitvalue

    delaunaynet = VGroup()

    while faces:
        eachface = faces[-1]
        faces.pop(-1)
        # 面所在的三条边
        e1 = eachface.HalfEdge
        e2 = e1.Suc
        e3 = e2.Suc
        # 标记访问过
        e1.Visit = notvisitvalue
        e2.Visit = notvisitvalue
        e3.Visit = notvisitvalue
        # 面对三个点
        p1 = e1.Start.Point
        p2 = e2.Start.Point
        p3 = e3.Start.Point
        delaunaynet.add(Polygon(p1, p2, p3))
        ei = [e1, e2, e3]
        for each in ei:
            et = each.Twin
            if et:
                etf = et.Face
                # 未访问过
                if etf.Visit == visitvalue:
                    # 访问过
                    etf.Visit = notvisitvalue
                    faces.append(etf)

    return delaunaynet

# 访问维诺图，O(n)
def VisitVoronoi(face):
    visitvalue = face.Visit
    notvisitvalue = not visitvalue
    faces = [face]
    # 访问过
    face.Visit = notvisitvalue

    voronoi = []

    while faces:
        eachface = faces[-1]
        faces.pop(-1)
        # 面所在的三条边
        e1 = eachface.HalfEdge
        e2 = e1.Suc
        e3 = e2.Suc
        ## 将正在访问的面的三个相邻的面加入faces
        eis = [e1, e2, e3]
        for ei in eis:
            # ei的孪生兄弟
            eiTwin = ei.Twin
            # ei未被访问过
            if ei.Visit == visitvalue:
                ei.Visit = notvisitvalue
                if eiTwin:
                    ls, le = ei.Start.Point, ei.End.Point
                    if abs(ls[0]) != Infinity and abs(ls[1]) != Infinity and abs(le[0]) != Infinity and abs(le[1]) != Infinity:
                        efc, etfc = ei.Face.Center, eiTwin.Face.Center
                        ese = eiTwin.Suc.End.Point
                        # 边的对点是无穷点
                        if abs(ese[0]) == Infinity or abs(ese[1]) == Infinity:
                            eis, eie = np.array(ei.Start.Point), np.array(ei.End.Point)
                            vertical = np.cross(eie - eis, np.array([0, 0, 1]))
                            vertical = normalize(vertical)
                            vertical = Infinity * vertical
                            newle = efc + vertical
                            voronoi.append([efc, newle])
                        else:
                            voronoi.append([efc, etfc])

                    faces.append(eiTwin.Face)
                    # 访问过
                    eiTwin.Face.Visit = notvisitvalue
                    eiTwin.Visit = notvisitvalue

    return voronoi

# 给网加圆心，O(n)
def InitNetCircumcircleCenter(face):
    # 访问网
    visitvalue = face.Visit
    notvisitvalue = not visitvalue
    faces = [face]
    # 访问过
    face.Visit = notvisitvalue

    #delaunaynet = VGroup()

    while faces:
        eachface = faces[-1]
        faces.pop(-1)
        # 面所在的三条边
        e1 = eachface.HalfEdge
        e2 = e1.Suc
        e3 = e2.Suc
        # 标记访问过
        e1.Visit = notvisitvalue
        e2.Visit = notvisitvalue
        e3.Visit = notvisitvalue
        # 面对三个点
        p1 = e1.Start.Point
        p2 = e2.Start.Point
        p3 = e3.Start.Point
        # 赋值圆心
        if eachface.Center is None:
            eachface.Center = CircumcircleCenter(p1, p2, p3)

        #delaunaynet.add(Polygon(p1, p2, p3))
        eis = [e1, e2, e3]
        for ei in eis:
            eit = ei.Twin
            if eit:
                eitf = eit.Face
                # 未访问过
                if eitf.Visit == visitvalue:
                    # 访问过
                    eitf.Visit = notvisitvalue
                    faces.append(eitf)

# 构造网，O(nlogn)
def ConstructNet(points=None):
    face1 = InitInfNet(points)
    infedge = face1.HalfEdge
    buckets = [face1.Bucket]

    while buckets:
        # 取桶
        bucket = buckets[-1]
        buckets.pop(-1)

        # 取桶的点
        point = bucket.Points[-1]
        bucket.Points.pop(-1)
        vo = Vertice(point)

        # 桶所在三角形的边
        crpface = bucket.Face
        hf1 = crpface.HalfEdge
        hf2 = hf1.Suc
        hf3 = hf2.Suc

        # 撕裂面
        ClipFace(crpface, vo, bucket.Points)
        # 看看是否要边翻转
        edges = [hf1, hf2, hf3]
        while edges:
            eachedge = edges[-1]
            edges.pop(-1)
            eachedgetwin = eachedge.Twin
            if eachedgetwin:
                trip1 = vo.Point
                trip2 = eachedgetwin.Start.Point
                trip3 = eachedgetwin.End.Point
                trip4 = eachedgetwin.Suc.End.Point
                if InCircle(trip1, trip2, trip3, trip4):
                    etfb = eachedgetwin.Face.Bucket
                    if len(etfb.Points) > 0:
                        buckets.remove(etfb)
                    edges.append(eachedgetwin.Pre)
                    edges.append(eachedgetwin.Suc)
                    EdgeFlipping(eachedge)


        # 遍历点周围的所有边，把桶加入
        ringvisit = vo.HalfEdge
        currvisit = ringvisit.Twin.Suc
        while currvisit != ringvisit:
            currbucket = currvisit.Face.Bucket
            if len(currbucket.Points) > 0:
                buckets.append(currbucket)
            currvisit = currvisit.Twin.Suc
        currbucket = currvisit.Face.Bucket
        if len(currbucket.Points) > 0:
            buckets.append(currbucket)

    return infedge.Face

# 得到某点在网中的面
def get_point_posface(point, net):
    # 访问网
    visitvalue = net.Visit
    notvisitvalue = not visitvalue
    faces = [net]
    # 访问过
    net.Visit = notvisitvalue

    # 位置
    #posface = None
    mark = True

    while faces:
        eachface = faces[-1]
        faces.pop(-1)
        # 面所在的三条边
        e1 = eachface.HalfEdge
        e2 = e1.Suc
        e3 = e2.Suc
        # 标记访问过
        e1.Visit = notvisitvalue
        e2.Visit = notvisitvalue
        e3.Visit = notvisitvalue
        # 面对三个点
        p1 = e1.Start.Point
        p2 = e2.Start.Point
        p3 = e3.Start.Point
        # 位置未找到
        if mark:
            if InTriangle(p1, p2, p3, point):
                posface = eachface
        ei = [e1, e2, e3]
        for each in ei:
            et = each.Twin
            if et:
                etf = et.Face
                # 未访问过
                if etf.Visit == visitvalue:
                    # 访问过
                    etf.Visit = notvisitvalue
                    faces.append(etf)

    return posface

# 在网中插入点，O(n)
def net_insert_point(point, net):
    # 点所在的面
    posface = get_point_posface(point, net)
    posface.Bucket.Points.append(point)
    infedge = posface.HalfEdge
    buckets = [posface.Bucket]

    while buckets:
        # 取桶
        bucket = buckets[-1]
        buckets.pop(-1)

        # 取桶的点
        point = bucket.Points[-1]
        bucket.Points.pop(-1)
        vo = Vertice(point)
        # 桶所在三角形的边
        crpface = bucket.Face
        hf1 = crpface.HalfEdge
        hf2 = hf1.Suc
        hf3 = hf2.Suc

        # 撕裂面
        ClipFace(crpface, vo, bucket.Points)
        # 看看是否要边翻转
        edges = [hf1, hf2, hf3]
        while edges:
            eachedge = edges[-1]
            edges.pop(-1)
            eachedgetwin = eachedge.Twin
            if eachedgetwin:
                trip1 = vo.Point
                trip2 = eachedgetwin.Start.Point
                trip3 = eachedgetwin.End.Point
                trip4 = eachedgetwin.Suc.End.Point
                if InCircle(trip1, trip2, trip3, trip4):
                    etfb = eachedgetwin.Face.Bucket
                    if len(etfb.Points) > 0:
                        buckets.remove(etfb)
                    edges.append(eachedgetwin.Pre)
                    edges.append(eachedgetwin.Suc)
                    EdgeFlipping(eachedge)

        # 遍历点周围的所有边，把桶加入
        ringvisit = vo.HalfEdge
        currvisit = ringvisit.Twin.Suc
        while currvisit != ringvisit:
            currbucket = currvisit.Face.Bucket
            if len(currbucket.Points) > 0:
                buckets.append(currbucket)
            currvisit = currvisit.Twin.Suc
        currbucket = currvisit.Face.Bucket
        if len(currbucket.Points) > 0:
            buckets.append(currbucket)

    return infedge.Face

# 在网中插入点，并设置外心，O(n)
def net_insert_point_and_set_circumcirclecenter(point, net):
    # 点所在的面，O(n)
    posface = get_point_posface(point, net)

    vo = Vertice(point)
    # 桶所在三角形的边
    crpface = posface
    hf1 = crpface.HalfEdge
    hf2 = hf1.Suc
    hf3 = hf2.Suc

    # 撕裂面
    ClipFace(crpface, vo, [])

    # 设置外心
    hf1.Face.Center = CircumcircleCenter(hf1.Start.Point, hf1.End.Point, point)
    hf2.Face.Center = CircumcircleCenter(hf2.Start.Point, hf2.End.Point, point)
    hf3.Face.Center = CircumcircleCenter(hf3.Start.Point, hf3.End.Point, point)

    # 看看是否要边翻转，O(6)
    edges = [hf1, hf2, hf3]
    while edges:
        eachedge = edges[-1]
        edges.pop(-1)
        eachedgetwin = eachedge.Twin
        if eachedgetwin:
            trip1 = vo.Point
            trip2 = eachedgetwin.Start.Point
            trip3 = eachedgetwin.End.Point
            trip4 = eachedgetwin.Suc.End.Point
            if InCircle(trip1, trip2, trip3, trip4):
                edges.append(eachedgetwin.Pre)
                edges.append(eachedgetwin.Suc)
                efv1 = eachedge.Suc
                efv2 = eachedgetwin.Suc
                EdgeFlipping(eachedge)
                efv1.Face.Center = CircumcircleCenter(trip1, trip2, trip4)
                efv2.Face.Center = CircumcircleCenter(trip1, trip3, trip4)

    return vo.HalfEdge.Face

# 德劳内三角网，O(nlogn)
class DelaunayTrianglation(VGroup):
    def __init__(self, *points, **kwargs):
        digest_config(self, kwargs)
        self.net = ConstructNet(list(points))
        self.kwargs = kwargs
        VGroup.__init__(self, *[Line(*each) for each in self.VisitNet()], **kwargs)

    # 获取网的顶点对，即用坐标表示的线
    def VisitNet(self):
        return VisitNet(self.net)

    def VisitTriangles(self):
        return VGroup(*VisitTriangles(self.net), **self.kwargs)

    # 获取网
    def GetNet(self):
        return self.net

    # 插入节点
    def InsertPoint(self, point):
        net_insert_point(point, self.net)
        self.become(VGroup(*[Line(*each, **self.kwargs) for each in self.VisitNet()]))
        return self

# 维诺图，O(n)+O(nlogn)=O(nlogn)
class Voronoi(VGroup):
    def __init__(self, *points, **kwargs):
        digest_config(self, kwargs)
        self.kwargs = kwargs
        self.net = DelaunayTrianglation(*points).GetNet()
        InitNetCircumcircleCenter(self.net)
        self.voronoi = self.VisitVoronoi()
        VGroup.__init__(self, *[Line(*each) for each in self.voronoi], **kwargs)

    def VisitVoronoi(self):
        return VisitVoronoi(self.net)

    # 获取网
    def GetNet(self):
        return self.net

    # 插入节点
    def InsertPoint(self, point):
        net_insert_point_and_set_circumcirclecenter(point, self.net)
        self.voronoi = self.VisitVoronoi()
        self.become(VGroup(*[Line(*each, **self.kwargs) for each in self.voronoi]))
        return self

# 测试类
class test(Scene):
    def construct(self):

        np.random.seed(2007)
        points = [
            [np.random.randint(-70000, 70000)/10500, np.random.randint(-38000, 38000)/10500, 0] for i in range(800)
        ]
        #points = [UL, UP, UR, LEFT, ORIGIN, RIGHT, DL, DOWN, DR]
        #points = [UL, DR, UR, DL]
        dots = [Dot(p).scale(0.5) for p in points]
        self.add(*dots)
        start = time.perf_counter()
        net = Voronoi(*points)
        self.add(net)
        end = time.perf_counter()
        print(end - start)

        '''
        p1, p2, p3 = DL, UL, UR
        p4 = DR
        p5 = ORIGIN
        p6 = UL/2
        p7 = UL
        p8 = UL*2
        print(InTriangle(p1, p2, p3, p4))
        print(InTriangle(p1, p2, p3, p5))
        print(InTriangle(p1, p2, p3, p6))
        print(InTriangle(p1, p2, p3, p7))
        print(InTriangle(p1, p2, p3, p8))
        print(InCircle(p1, p2, p3, p4))
        print(InCircle(p1, p2, p3, p5))
        print(InCircle(p1, p2, p3, p6))
        print(InCircle(p1, p2, p3, p7))
        print(InCircle(p1, p2, p3, p8))
        '''
        '''
        infnet = InitInfNet()
        he1 = infnet.HalfEdge
        he2 = he1.Suc
        he3 = he2.Suc
        print(get_polygon_directed_area(Polygon(he1.Start.Point, he2.Start.Point, he3.Start.Point)))
        '''
        '''
        np.random.seed(2007)
        points = [
            [np.random.randint(-70000, 70000)/10500, np.random.randint(-38000, 38000)/10500, 0] for i in range(1000)
        ]
        #points = [UL, UP, UR, LEFT, ORIGIN, RIGHT, DL, DOWN, DR]
        #points = [UL, DR, UR, DL]
        dots = [Dot(p) for p in points]
        #self.add(*dots)
        start = time.perf_counter()
        delaunay = ConstructNet(self, points)
        net = VisitNet(delaunay)
        end = time.perf_counter()
        print(end - start)
        self.add(net)
        '''
        '''
        np.random.seed(2000007)
        points = [
            [np.random.randint(-70000, 70000)/10000, np.random.randint(-38000, 38000)/10000, 0] for i in range(7)
        ]
        dots = [Dot(p) for p in points]
        self.add(*dots)
        start = time.perf_counter()
        delaunay = InitInfNet(points)
        #print(points[0])
        net1, net2, net3 = ClipFace(delaunay, Vertice(points[0]), points[1:])
        net = VisitTriangles(net1)
        end = time.perf_counter()
        print(end - start)
        self.add(net)
        '''
        '''
        p1, p2, p3, p4 = UL, UR*2, DR, DL*2
        v1, v2, v3, v4 = Vertice(p1), Vertice(p2), Vertice(p3), Vertice(p4)
        he1 = HalfEdge(v1, v2)
        he2 = HalfEdge(v2, v3)
        he3 = HalfEdge(v3, v4)
        he4 = HalfEdge(v4, v1)
        he5 = HalfEdge(v3, v1)
        he6 = HalfEdge(v1, v3)

        he1.Suc = he2
        he2.Pre = he1
        he2.Suc = he5
        he5.Pre = he2
        he5.Suc = he1
        he1.Pre = he5

        he3.Suc = he4
        he4.Pre = he3
        he4.Suc = he6
        he6.Pre = he4
        he6.Suc = he3
        he3.Pre = he6

        bucket1 = Bucket([UR+RIGHT/5, UR+LEFT/5])
        bucket2 = Bucket([])

        face1 = Face(he1)
        face1.Bucket = bucket1
        bucket1.Face = face1
        he1.Face = face1
        he2.Face = face1
        he5.Face = face1
        face2 = Face(he3)
        face2.Bucket = bucket2
        bucket2.Face = face2
        he3.Face = face2
        he4.Face = face2
        he6.Face = face2
        he5.Twin = he6
        he6.Twin = he5

        EdgeFlipping(he5)
        start = time.perf_counter()
        net = VisitInfNet(face1)
        end = time.perf_counter()
        print(end - start)

        print(get_polygon_directed_area(Polygon(face1.HalfEdge.Start.Point, face1.HalfEdge.Suc.Start.Point,
                      face1.HalfEdge.Suc.Suc.Start.Point)))
        print(get_polygon_directed_area(Polygon(face2.HalfEdge.Start.Point, face2.HalfEdge.Suc.Start.Point,
                      face2.HalfEdge.Suc.Suc.Start.Point)))
        self.add(net)
        '''
        #p1, p2, p3, p4 = UL, UR, DR, DL
        #print(InTriangle(p1, p2, p3, ORIGIN), InTriangle(p1, p2, p3, UR/2), InTriangle(p1, p2, p3, p4))
        '''
        start = time.perf_counter()
        print(
            InCircle(p1, p2, p3, p4),
            InCircle(p1, p2, p3, ORIGIN),
            InCircle(p1, p2, p3, p4+LEFT)
        )
        end = time.perf_counter()
        print(end - start)
        start = time.perf_counter()
        print(
            InCircle2(p1, p2, p3, p4),
            InCircle2(p1, p2, p3, ORIGIN),
            InCircle2(p1, p2, p3, p4+LEFT)
        )
        end = time.perf_counter()
        print(end - start)
        '''
        self.wait()

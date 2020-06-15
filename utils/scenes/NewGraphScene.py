# from @GZTime
"""
新绘图场景
NewGraphScene
~~~~~~~~~~~~
from @GZTime
"""
from manimlib.imports import *

class NewGraphScene(GraphScene):
    """NewGraphScene by GZTime.

    To use:

    - 更新函数展示区域，定义域和坐标轴位置同GraphScene，此项设置需要在setup_axes前完成。
    
    >>> self.graph_origin = ORIGIN
    >>> self.x_min, self.x_max = -5,5
    >>> self.y_min, self.y_max = -5,5

    - 新建坐标轴 create axes
   
    >>> self.setup_axes(animate=True)

    - 绘制函数图像 draw function graph
    
    >>> self.add_function_graph(
            lambda x: x**x,
            animate=True,x_min=0)
    >>> self.add_function_graph(
            lambda x: x**2-x,
            animate=True)
    >>> self.add_function_graph(
            lambda x: math.sin(2*x)+1,
            animate=True)

    - 绘制参数方程图像 draw parametric function graph
    
    >>> self.add_parametric_graph(
            lambda t: [2*math.sin(t) + 2,math.cos(t) + 1,0],
            animate=True,t_min=0,t_max=2*math.pi,
            color=RED)
    >>> self.add_parametric_graph(
            lambda t: [math.sin(t) + 1,math.tan(t) + 0.5,0],
            animate=True,t_min=0,t_max=2*math.pi,
            color=ORANGE)

    - 访问已经新建的函数使用如下两个`list`也可以直接获取add_graph函数的返回值。
    
    >>> self.play(FadeOut(self.functions[0]))
    >>> self.play(FadeOut(self.parametric_functions[0]))
    
    - 更新函数方程 updata graph
    
    >>> self.updata_graph(
            self.parametric_functions[0],
            lambda t: [2*math.cos(t),math.sin(t),0])

    - 除上述方法外，此类为GraphScene的子类，可以调用其方法和属性以及扩展，但不再建议使用原本的get_function函数。
    """
    functions = []
    parametric_functions = []

    def add_function_graph(self,func,animate=False,color=None,x_min=None,x_max=None,**kwargs):
        """向场景中添加函数图像。
        Add a function graph to scene.
        """
        if color is None:
            color = next(self.default_graph_colors_cycle)
        if x_min is None:
            x_min = self.x_min
        if x_max is None:
            x_max = self.x_max

        def parameterized_function(alpha):
            x = interpolate(x_min, x_max, alpha)
            y = func(x)
            return self.coords_to_point(x, y)

        graph = NewParametricFunction(
            parameterized_function,
            x_min = self.x_axis.number_to_point(self.x_min)[0] * RIGHT,
            x_max = self.x_axis.number_to_point(self.x_max)[0] * RIGHT,
            y_min = self.y_axis.number_to_point(self.y_min)[1] * UP,
            y_max = self.y_axis.number_to_point(self.y_max)[1] * UP,
            color=color,**kwargs)
        graph.underlying_function = func

        self.functions.append(graph)

        if animate:
            self.play(ShowCreation(graph))
        else:
            self.add(graph)
        return self

    def add_parametric_graph(self,func,animate=False,color=None,x_min=None,x_max=None,t_min=0,t_max=1,**kwargs):
        """向场景中添加参数方程。
        Add a parametric function graph to scene.
        """
        if color is None:
            color = next(self.default_graph_colors_cycle)
        if x_min is None:
            x_min = self.x_min
        if x_max is None:
            x_max = self.x_max

        graph = NewParametricFunction(func,t_min=t_min,t_max=t_max,
            x_min = self.x_axis.number_to_point(self.x_min)[0] * RIGHT,
            x_max = self.x_axis.number_to_point(self.x_max)[0] * RIGHT,
            y_min = self.y_axis.number_to_point(self.y_min)[1] * UP,
            y_max = self.y_axis.number_to_point(self.y_max)[1] * UP,
            color=color,**kwargs)

        graph.underlying_function = func

        self.parametric_functions.append(graph)

        if animate:
            self.play(ShowCreation(graph))
        else:
            self.add(graph)
        return self

    def updata_graph(self,graph,newfunc):
        """更新某图像的方程，并使用Transform变换。
        update and transform your graph to a new function.
        """
        newgraph = graph.copy().updata_function(newfunc)
        self.play(Transform(graph,newgraph))
        graph = newgraph

class NewParametricFunction(ParametricFunction):
    """NewParametricFunction by GZTime.
    
    此类主要覆写了generate_points函数使其生成的路径具有x轴以及y轴的限制，并将每一段曲线作为一个submobject展示。
    """
    CONFIG = {
        "y_min": -1,
        "y_max": 1,
        "x_min": -1,
        "x_max": 1
    }
    
    def __init__(self, function=None,y_min = -1,y_max = 1,x_min = -1,x_max = 1,**kwargs):
        # either get a function from __init__ or from CONFIG
        self.function = function or self.function
        self.y_min,self.y_max = y_min,y_max
        self.x_min,self.x_max = x_min,x_max
        VMobject.__init__(self, **kwargs)

    def generate_points(self):
        t_min, t_max = self.t_min, self.t_max
        y_min, y_max = self.y_min, self.y_max
        x_min, x_max = self.x_min, self.x_max

        dt = self.dt

        discontinuities = filter(
            lambda t: t_min <= t <= t_max,
            self.discontinuities
        )

        discontinuities = np.array(list(discontinuities))
        boundary_times = [
            self.t_min, self.t_max,
            *(discontinuities - dt),
            *(discontinuities + dt),
        ]
        boundary_times.sort()
        for t1, t2 in zip(boundary_times[0::2], boundary_times[1::2]):
            t_range = list(np.arange(t1, t2, self.get_step_size(t1)))
            if t_range[-1] != t2:
                t_range.append(t2)
            
            points = np.array([self.function(t) for t in t_range])
            
            valid_indices = np.apply_along_axis(
                np.all, 1, np.isfinite(points)
            )
            points = points[valid_indices]
            
            using_points = []
            if len(points) > 0:
                tlist = []
                for order in range(len(points) + 1):
                    if order == len(points):
                        if len(tlist) > 0:
                            using_points.append(np.array(tlist))
                            tlist.clear()
                    else:
                        if y_min[1] <= points[order][1] <= y_max[1] and\
                           x_min[0] <= points[order][0] <= x_max[0] :
                            tlist.append(points[order])
                        elif len(tlist) > 0:
                            using_points.append(np.array(tlist))
                            tlist.clear()

            for item in using_points:
                path = VMobject()
                path.start_new_path(item[0])
                path.add_points_as_corners(item[1:])
                path.make_smooth()
                self.add(path)

        return self
    
    def updata_function(self,newfunc = None, **kwargs):
        if newfunc == None:
            return
        self.function = newfunc
        VMobject.__init__(self, **kwargs)
        return self

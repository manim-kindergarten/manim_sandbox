# from @魔与方

from manimlib.imports import *

### This is the newest (2020.05.16) ThreeDVector class by @魔与方

class ThreeDVector(VMobject):

	"""
	This vector has two parts
	The top part is a cone (tip)
	The bottom part is a cylinder
	The parameter "tip_length" means the height of the cone (tip)
	The parameter "tip_radius" means the base radius of the cone (tip)
	The parameter "bottom_radius" means the base radius of the cylinder
	The parameter "circle_side_width" means the width of the side of the base circle of the cone and the base circle of the cylinder
	The parameter "circle_side_color" means the color of the side of the base circle of the cone and the base circle of the cylinder
	"""


	CONFIG = {
	'color': BLUE,
	'tip_length_to_vector_length': 1/5,		#The ratio of "tip_length" to the length of vector
	'tip_radius_to_tip_length': 1/2,		#The ratio of "tip_radius" to "tip_length"
	'bottom_radius_to_tip_radius': 2/5,		#The ratio of "bottom_radius" to "tip_radius"
	'max_tip_length': 0.8,					#The maximum of "tip_length"
	'max_bottom_radius': 0.2,				#The maximum of "bottom_radius"
	'circle_side_width': 2,
	'circle_side_color': None,
	'delta_radian': np.sqrt(3)/60,
	'fill_opacity': 1,
	}


	def __init__(self,direction=RIGHT,**kwargs):

		VMobject.__init__(self,**kwargs)
		self.direction = np.array(direction,dtype=np.float64)
		self.vector_length = get_norm(self.direction)
		if self.vector_length > 0.:
			self.get_some_parameters()
			self.get_cylinder()
			self.get_tip()
			self.get_rotation_angles()
			self.rotate(self.phi,axis=UP,about_point=ORIGIN)
			self.rotate(self.theta,axis=OUT,about_point=ORIGIN)


	def get_some_parameters(self):


		self.tip_length = self.vector_length * self.tip_length_to_vector_length
		if self.tip_length > self.max_tip_length:
			self.tip_length = self.max_tip_length


		self.tip_radius = self.tip_length * self.tip_radius_to_tip_length


		self.bottom_radius = self.tip_radius * self.bottom_radius_to_tip_radius
		if self.bottom_radius > self.max_bottom_radius:
			self.bottom_radius = self.max_bottom_radius


		self.tip_bottom_delta_theta = self.delta_radian/self.tip_radius


		self.bottom_delta_theta = self.delta_radian/self.bottom_radius


		if self.circle_side_color == None:
			self.circle_side_color = self.color


	def get_cylinder(self):

		thetas = np.c_[0:2*np.pi+self.bottom_delta_theta:self.bottom_delta_theta]
		bc_points = np.c_[
			self.bottom_radius * np.cos(thetas),
			self.bottom_radius * np.sin(thetas),
			np.zeros_like(thetas)].tolist()

		bc_points_ = np.c_[
			self.bottom_radius * np.cos(thetas),
			self.bottom_radius * np.sin(thetas),
			np.full_like(thetas,self.vector_length - self.tip_length)].tolist()

		for i in range(len(bc_points) - 1):
			self.add(Polygon(
				*[*bc_points[i:i+2],bc_points_[i+1],bc_points_[i]],
				color=self.color,
				stroke_width=1,
				stroke_color=self.color,
				fill_opacity=self.fill_opacity,
				shade_in_3d=True)
			)

		self.add(Polygon(
			*bc_points,
			color=self.color,
			stroke_width=self.circle_side_width,
			stroke_color=self.circle_side_color,
			fill_opacity=self.fill_opacity,
			shade_in_3d=True)
		)


	def get_tip(self):

		thetas = np.c_[0:2*np.pi+self.tip_bottom_delta_theta:self.tip_bottom_delta_theta]
		tbc_points = np.c_[
			self.tip_radius*np.cos(thetas),
			self.tip_radius*np.sin(thetas),
			np.full_like(thetas,self.vector_length - self.tip_length)].tolist()

		for i in range(len(tbc_points) - 1):
			self.add(
				Polygon(
					*[*tbc_points[i:i+2],[0,0,self.vector_length]],
					color=self.color,
					stroke_width=1,
					stroke_color=self.color,
					fill_opacity=self.fill_opacity,
					shade_in_3d=True),
				)

		self.add(Polygon(
			*tbc_points,
			color=self.color,
			stroke_width=self.circle_side_width,
			stroke_color=self.circle_side_color,
			fill_opacity=self.fill_opacity,
			shade_in_3d=True)
		)


	def get_rotation_angles(self):


		x,y,z = self.direction
		rho = get_norm([x,y])

		self.phi = np.arccos(z/self.vector_length)

		if rho > 0.:
			if y >= 0.:
				self.theta = np.arccos(x/rho)
			else:
				self.theta = -np.arccos(x/rho)
		else:
			self.theta = 0

### The ThreeDVectorByCone class below is also written by @魔与方, but slightly different from the former one
### So, just choose the style you like _(:з」∠)_

class ThreeDVectorByCone(VMobject):

	"""
	This vector has two parts
	The top part is a cone (tip)
	The bottom part is a cone too
	The parameter "tip_length" means the height of the cone (tip)
	The parameter "tip_radius" means the base radius of the cone (tip)
	The parameter "bottom_radius" means the base radius of the cone
	The parameter "circle_side_width" means the width of the side of the base circle of the cone and the base circle of the cone
	The parameter "circle_side_color" means the color of the side of the base circle of the cone and the base circle of the cone
	"""

	CONFIG = {
	'color':BLUE,
	'tip_length_to_vector_length': 1/5,		#The ratio of "tip_length" to the length of vector
	'tip_radius_to_tip_length': 1/2,		#The ratio of "tip_radius" to "tip_length"
	'bottom_radius_to_tip_radius': 2/5,		#The ratio of "bottom_radius" to "tip_radius"
	'max_tip_length': 0.8,					#The maximum of "tip_length"
	'max_bottom_radius': 0.2,				#The maximum of "bottom_radius"
	'circle_side_width': 2,
	'circle_side_color': None,
	'delta_radian': np.sqrt(3)/60,
	'fill_opacity': 1,
	}


	def __init__(self,direction=RIGHT,**kwargs):

		VMobject.__init__(self,**kwargs)
		self.direction = np.array(direction,dtype=np.float64)
		self.vector_length = get_norm(self.direction)
		if self.vector_length > 0.:
			self.get_some_parameters()
			self.get_cone()
			self.get_tip()
			self.get_rotation_angles()
			self.rotate(self.phi,axis=UP,about_point=ORIGIN)
			self.rotate(self.theta,axis=OUT,about_point=ORIGIN)


	def get_some_parameters(self):


		self.tip_length = self.vector_length * self.tip_length_to_vector_length
		if self.tip_length > self.max_tip_length:
			self.tip_length = self.max_tip_length


		self.tip_radius = self.tip_length * self.tip_radius_to_tip_length


		self.bottom_radius = self.tip_radius * self.bottom_radius_to_tip_radius
		if self.bottom_radius > self.max_bottom_radius:
			self.bottom_radius = self.max_bottom_radius


		self.tip_bottom_delta_theta = self.delta_radian/self.tip_radius


		self.bottom_delta_theta = self.delta_radian/self.bottom_radius


		if self.circle_side_color == None:
			self.circle_side_color = self.color


	def get_cone(self):


		thetas = np.c_[0:2*np.pi+self.bottom_delta_theta:self.bottom_delta_theta]
		bc_points = np.c_[
			self.bottom_radius * np.cos(thetas),
			self.bottom_radius * np.sin(thetas),
			np.zeros_like(thetas)].tolist()

		for i in range(len(bc_points) - 1):
			self.add(Polygon(
				*[*bc_points[i:i+2],[0,0,self.vector_length - self.tip_length]],
				color=self.color,
				stroke_width=1,
				stroke_color=self.color,
				fill_opacity=self.fill_opacity,
				shade_in_3d=True)
			)

		self.add(Polygon(
			*bc_points,
			color=self.color,
			stroke_width=self.circle_side_width,
			stroke_color=self.circle_side_color,
			fill_opacity=self.fill_opacity,
			shade_in_3d=True)
		)


	def get_tip(self):


		thetas = np.c_[0:2*np.pi+self.tip_bottom_delta_theta:self.tip_bottom_delta_theta]
		tbc_points = np.c_[
			self.tip_radius*np.cos(thetas),
			self.tip_radius*np.sin(thetas),
			np.full_like(thetas,self.vector_length - self.tip_length)].tolist()

		for i in range(len(tbc_points) - 1):
			self.add(
				Polygon(
					*[*tbc_points[i:i+2],[0,0,self.vector_length]],
					color=self.color,
					stroke_width=1,
					stroke_color=self.color,
					fill_opacity=self.fill_opacity,
					shade_in_3d=True),
				)

		self.add(Polygon(
			*tbc_points,
			color=self.color,
			stroke_width=self.circle_side_width,
			stroke_color=self.circle_side_color,
			fill_opacity=self.fill_opacity,
			shade_in_3d=True)
		)


	def get_rotation_angles(self):


		x,y,z = self.direction
		rho = get_norm([x,y])

		self.phi = np.arccos(z/self.vector_length)

		if rho > 0.:
			if y >= 0.:
				self.theta = np.arccos(x/rho)
			else:
				self.theta = -np.arccos(x/rho)
		else:
			self.theta = 0

### the old version of ThreeDVectorByCone
class ThreeDVector_Old(VMobject):
    """
    这个类的原理：
    向量主体和向量顶端是圆锥，
    圆锥的底面是用多边形近似的圆，
    圆锥的侧面也是用多边形拼接的，
    所以d_theta控制多边形近似圆的精度的
    """
    CONFIG = {
    "radio_of_tip_length_to_vector_length":1/5,#顶端圆锥长度与向量长度的比
    "max_bottom_radius":0.04,#向量主体底端圆锥的最大半径
    "max_tip_length":0.4,#顶端圆锥最大长度(圆锥的高)
    "bottom_circle_d_theta":0.1,
    "tip_bottom_circle_d_theta":0.1,
    "fill_opacity":0.8,
    }

    def __init__(self,direction=RIGHT,**kwargs):
        VMobject.__init__(self,**kwargs)
        self.direction = np.array(direction,dtype=np.float)
        if self.get_length(self.direction) != 0:
            self.get_and_reset_some_parameters()
            self.get_rotation_matrix()
            self.get_bottom_circle_points()
            self.get_cone()
            self.get_tip_circle_points()
            self.get_tip_cone()
            self.add(
                self.bottom_circle,
                self.cone_side,
                self.tip_bottom_circle,
                self.tip_cone_side
                )
    def get_and_reset_some_parameters(self):
        l = self.get_length(self.direction)
        tl = l*self.radio_of_tip_length_to_vector_length
        if tl > self.max_tip_length :
            self.tip_length = self.max_tip_length
        else:
            self.tip_length = tl
        self.tip_bottom_radius = self.tip_length/2
        br = self.tip_bottom_radius/4
        if br > self.max_bottom_radius:
            self.bottom_radius = self.max_bottom_radius
        else:
            self.bottom_radius = br
        self.direction *= (l-tl)/l

    def get_rotation_matrix(self):
        rho = self.get_length(self.direction[:2])
        r = self.get_length(self.direction)
        cos_phi = self.direction[2] / r
        sin_phi = rho / r

        if rho != 0:
            cos_theta = self.direction[0] / rho
            sin_theta = self.direction[1] / rho
        else:
            cos_theta = 1
            sin_theta = 0

        self.M_z = np.array([
            [cos_theta,-sin_theta,0],
            [sin_theta,cos_theta,0],
            [0,0,1]
            ])

        self.M_y = np.array([
            [cos_phi,0,sin_phi],
            [0,1,0],
            [-sin_phi,0,cos_phi]
            ])

    def get_bottom_circle_points(self):
        points = []
        for theta in np.arange(\
            0,2*np.pi+self.bottom_circle_d_theta,self.bottom_circle_d_theta):
            point = [self.bottom_radius*np.cos(theta),
                     self.bottom_radius*np.sin(theta),
                     0]
            points.append(point)
        points = np.array(points).T

        self.bc_points = list(np.dot(self.M_z,np.dot(self.M_y,points)).T)

    def get_cone(self):
        self.bottom_circle = Polygon(
            *self.bc_points,
            color=self.color,
            fill_opacity=self.fill_opacity,
            stroke_width=1,
            stroke_color=self.color)

        self.cone_side = VGroup()

        n = 4
        rm_n = (len(self.bc_points)-1)%(n-2)
        step = (len(self.bc_points)-1)//(n-2)
        range1 = range(0,step*(n-2),n-2)
        for i in range1:
            points = [self.bc_points[j] for j in range(i,i+n-1)]
            points.append(self.direction)
            self.cone_side.add(Polygon(
                *points,
                color=self.color,
                fill_opacity=self.fill_opacity,
                stroke_width=1,
                stroke_color=self.color))
        points = [self.bc_points[i] for i in \
            range(step*(n-2),step*(n-2)+rm_n+1)]
        if rm_n != 0:
            points = [self.bc_points[i] for i in \
                range(step*(n-2),step*(n-2)+rm_n+1)]
            points.append(self.direction)
            self.cone_side.add(Polygon(
                *points,
                color=self.color,
                fill_opacity=self.fill_opacity,
                stroke_width=1,
                stroke_color=self.color
                ))

    def get_tip_circle_points(self):
        points = []
        for theta in np.arange(\
            0,2*np.pi+self.tip_bottom_circle_d_theta,self.tip_bottom_circle_d_theta):
            point = [self.tip_bottom_radius*np.cos(theta),
                     self.tip_bottom_radius*np.sin(theta),
                     0]
            points.append(point)
        points = np.array(points).T
        self.tbc_points = list(
            np.dot(self.M_z,np.dot(self.M_y,points)).T + self.direction
            )

    def get_tip_cone(self):
        self.tip_vertex = self.direction + \
            self.direction/self.get_length(self.direction)*self.tip_length

        self.tip_bottom_circle = Polygon(
            *self.tbc_points,
            color=self.color,
            fill_opacity=self.fill_opacity,
            stroke_width=1,
            stroke_color=self.color)

        self.tip_cone_side = VGroup()

        n = 4
        rm_n = (len(self.tbc_points)-1)%(n-2)
        step = (len(self.tbc_points)-1)//(n-2)
        range1 = range(0,step*(n-2),n-2)
        for i in range1:
            points = [self.tbc_points[j] for j in range(i,i+n-1)]
            points.append(self.tip_vertex)
            self.tip_cone_side.add(Polygon(
                *points,
                color=self.color,
                fill_opacity=self.fill_opacity,
                stroke_width=1,
                stroke_color=self.color))
        points = [self.tbc_points[i] for i in \
            range(step*(n-2),step*(n-2)+rm_n+1)]
        if rm_n != 0:
            points = [self.tbc_points[i] for i in \
                range(step*(n-2),step*(n-2)+rm_n+1)]
            points.append(self.tip_vertex)
            self.tip_cone_side.add(Polygon(
                *points,
                color=self.color,
                fill_opacity=self.fill_opacity,
                stroke_width=1,
                stroke_color=self.color,
                ))

    def get_length(self,a):
        return np.sqrt(np.sum(np.square(a)))

### some test scenes ###

class Test1(ThreeDScene):

	def construct(self):

		axes = ThreeDAxes()
		self.add(axes)
		self.set_camera_orientation(phi=60*DEGREES,theta=0*DEGREES,distance=10)

		direction1 = [1,1,1]
		direction2 = [-1,2,1]
		direction3 = [0,0,1]
		direction4 = [0,0,0]

        # style 1
		v1 = ThreeDVectorByCone(direction1, color=BLUE)
		v2 = ThreeDVectorByCone(direction2, color=GREEN)
		v3 = ThreeDVectorByCone(direction3, color=RED)
		v4 = ThreeDVectorByCone(direction4, color=WHITE)

        # style 2
		# v1 = ThreeDVector(direction1,color=BLUE)
		# v2 = ThreeDVector(direction2,color=GREEN)
		# v3 = ThreeDVector(direction3,color=RED)
		# v4 = ThreeDVector(direction4,color=WHITE)

		self.add(v1,v2,v3)

		self.begin_ambient_camera_rotation(rate=1)

		self.wait(10)

class Test2(ThreeDScene):

	def construct(self):

		axes = ThreeDAxes()
		self.add(axes)
		self.set_camera_orientation(phi=60*DEGREES,theta=0*DEGREES,distance=10)

		###See the source code comments for more details on the parameters below
		direction = [2,2,2]
		color = BLUE
		tip_length_to_vector_length = 1/5
		tip_radius_to_tip_length = 1/2
		bottom_radius_to_tip_radius = 2/5
		max_tip_length = 0.8
		max_bottom_radius =  0.2
		circle_side_width =2
		circle_side_color = None
		delta_radian = np.sqrt(3)/60
		fill_opacity = 1

		vector = ThreeDVector(

			# direction,
			color=color,
			tip_length_to_vector_length=tip_length_to_vector_length,
			tip_radius_to_tip_length=tip_radius_to_tip_length,
			bottom_radius_to_tip_radius=bottom_radius_to_tip_radius,
			max_tip_length=max_tip_length,
			max_bottom_radius=max_bottom_radius,
			circle_side_width=circle_side_width,
			circle_side_color=circle_side_color,
			delta_radian=delta_radian,
			fill_opacity=fill_opacity
			)

		self.add(vector)

		#self.begin_ambient_camera_rotation(rate=1)

		self.wait(2)





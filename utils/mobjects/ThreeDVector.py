#from @魔与方

from manimlib.imports import *

### This is the newest (2020.05.19) ThreeDVector class by @魔与方

def cross_product(v1,v2):
	return np.array([
		v1[1]*v2[2] - v1[2]*v2[1],
		v1[2]*v2[0] - v1[0]*v2[2],
		v1[0]*v2[1] - v1[1]*v2[0]
		])


class ThreeDVector(VMobject):
	"""This vector has two parts

	The top part is a cone (tip)

	The bottom part is a circular cone 

	The parameter "tip_length" means the height of the cone (tip)

	The parameter "tip_radius" means the base radius of the cone (tip)

	The parameter "bottom_radius" means the bottom base radius of the truncated cone
	
	The parameter "top_radius"means the top base radius of the truncated cone
	
	The parameter "circle_side_width" means the width of the side of the base circle of the cone and the base circles of the truncated cone
	
	The parameter "circle_side_color" means the color of the side of the base circle of the cone and the base circles of the truncated cone
	"""
	CONFIG = {
	'color':BLUE,
	'tip_length_to_vector_length': 1/5,		#The ratio of "tip_length" to the length of vector
	'tip_radius_to_tip_length': 1/2,		#The ratio of "tip_radius" to "tip_length"
	'bottom_radius_to_tip_radius': 2/5,		#The ratio of "bottom_radius" to "tip_radius"
	'top_radius_to_bottom_radius':0,		#The ratio of "top_radius" to "bottom_radius"
	'max_tip_length': 0.8,					#The maximum of "tip_length"
	'max_bottom_radius': 0.2,				#The maximum of "bottom_radius"
	'circle_side_width': 2,					
	'circle_side_color': None,
	'delta_radian': np.sqrt(3)/60,
	'fill_opacity': 1,
	}
	def __init__(self,vector=RIGHT,position=ORIGIN,**kwargs):
		VMobject.__init__(self,**kwargs)
		self.__vector_position_dot = Dot(ORIGIN,radius=0.01,fill_opacity=0)
		self.__vector_end_dot = Dot([0,0,get_norm(vector)],radius=0.01,fill_opacity=0)
		self.add(self.__vector_position_dot,self.__vector_end_dot)
		self.__get_some_parameters()
		if get_norm(vector) > 0.:
			self.__add_truncated_cone()
			self.__add_tip()
			self.__delete_some_useless_parameters()
			self.set_direction(vector)
		self.shift(position)

	def __get_some_parameters(self):

		self.vector_length = self.get_vector_length()

		self.tip_length = self.get_vector_length() * self.tip_length_to_vector_length
		if self.tip_length > self.max_tip_length:
			self.tip_length = self.max_tip_length
			self.tip_length_to_vector_length = self.tip_length / self.vector_length

		self.tip_radius = self.tip_length * self.tip_radius_to_tip_length

		self.bottom_radius = self.tip_radius * self.bottom_radius_to_tip_radius
		if self.bottom_radius > self.max_bottom_radius:
			self.bottom_radius = self.max_bottom_radius
			self.bottom_radius_to_tip_radius = self.bottom_radius / self.tip_radius

		self.top_radius = self.bottom_radius * self.top_radius_to_bottom_radius 

		self.tip_bottom_delta_theta = self.delta_radian/self.tip_radius

		self.bottom_delta_theta = self.delta_radian/self.bottom_radius

		if self.circle_side_color == None:
			self.circle_side_color = self.color

	def __add_truncated_cone(self):

		thetas = np.c_[0:2*np.pi:self.bottom_delta_theta]

		bc_points = np.c_[
			self.bottom_radius * np.cos(thetas),
			self.bottom_radius * np.sin(thetas),
			np.zeros_like(thetas)].tolist()

		tc_points = np.c_[
			self.top_radius * np.cos(thetas),
			self.top_radius * np.sin(thetas),
			np.full_like(thetas,self.vector_length - self.tip_length)].tolist()

		for i in range(-1,len(bc_points) - 1):
			self.add(Polygon(
				*[*bc_points[i:i+2],tc_points[i+1],tc_points[i]],
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

	def __add_tip(self):

		thetas = np.c_[0:2*np.pi:self.tip_bottom_delta_theta]

		tbc_points = np.c_[
			self.tip_radius*np.cos(thetas),
			self.tip_radius*np.sin(thetas),
			np.full_like(thetas,self.vector_length - self.tip_length)].tolist()

		for i in range(-1,len(tbc_points) - 1):
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

	def __delete_some_useless_parameters(self):

		del self.vector_length
		del self.tip_length
		del self.tip_radius
		del self.bottom_radius
		del self.top_radius
		del self.delta_radian

	def get_position(self):
		#This method is used to get the position of vector
		#In this class, the position of the vector all means the position of beginning point of the vector
		return self.__vector_position_dot.get_center()

	def get_end(self):
		#This method is used to get the position of end point of the vector
		return self.__vector_end_dot.get_center()

	def get_vector(self):
		#This method is used to get the array of the vector
		return self.get_end() - self.get_position()

	def get_vector_length(self):
		#This method is used to get the length of the vector
		return get_norm(self.get_vector())

	def get_unit_vector(self):
		#This method is used to get the unit vector of the vector
		return self.get_vector()/self.get_vector_length()

	def get_tip_length(self):

		return self.get_vector_length() * self.tip_length_to_vector_length

	def get_tip_radius(self):

		return self.get_tip_length() * self.tip_radius_to_tip_length

	def get_bottom_radius(self):

		return self.get_tip_radius() * self.bottom_radius_to_tip_radius

	def get_top_radius(self):

		return self.get_bottom_radius() * self.top_radius_to_bottom_radius

	def set_direction(self,new_direction):
		#This method is used to change the direction of vector into a new direction
		#It only changes the direction but not changes the length of the vector
		norm = np.array(new_direction,dtype=np.float64)/get_norm(new_direction)
		cosine = self.get_unit_vector().dot(norm)
		if cosine > 1.:
			cosine = 1
		elif cosine < -1.:
			cosine = -1
		return self.rotate(
			np.arccos(cosine),
			axis=cross_product(self.get_vector(),norm),
			about_point=self.get_position())

	def set_position(self,new_position):
		#This method is used to change the position of vector into a new position
		return self.shift(np.array(new_position,dtype=np.float64) - self.get_position())

	def set_vector_length(self,new_length):
		#This method is used to change the length of the vector into a new length
		#It achieves the aim through scaling the vector(self.scale(...)), so the vector will be made larger of smaller
		#Scaling the vector will also change the position of the vector
		#So this method also sets the position to the original position
		original_position = self.get_position()
		self.scale(new_length/self.get_vector_length())
		return self.set_position(original_position)

	def set_vector(self,new_vector,new_position=None):
		#This method does the three things below:
		#The first one is changing the direction of the vector into the direction of a new vector
		#The second one is changing the length of  the vector into the length of the new vector
		#The last one is changing the position of the vector into the position of the new vector
		#If you don't give the paramter 'new_position', the last one won't be done
		if new_position:
			self.set_position(new_position)
		self.set_direction(new_vector)
		return self.set_vector_length(get_norm(new_vector))

	def move_along_curve(self,func,t,dt):
		#The form of this parameter 'func' is 'lambda t:np.array([x(t),y(t),z(t)])'
		#This method will move the vector to a point on the curve of 'func'
		#And change the direction of the vector into the direction of the tangent vector at this point
		self.set_direction(func(t+dt) - func(t))
		return self.set_position(func(t))


class ThreeDVectorByCone(ThreeDVector):


	CONFIG = {
	'top_radius_to_bottom_radius':0,
	}


class ThreeDVectorByCylinder(ThreeDVector):

	CONFIG = {
	'top_radius_to_bottom_radius':1,
	}


###TestExamples


class Test1(ThreeDScene):


	def construct(self):


		axes = ThreeDAxes()
		self.add(axes)
		self.set_camera_orientation(phi=60*DEGREES,theta=85*DEGREES,distance=10)

		direction1 = [1,1,1]
		direction2 = [-1,2,1]
		direction3 = [0,0,1]
		direction4 = [0,-2,0]
		direction5 = [0,0,0]

		v1 = ThreeDVector(direction1,color=BLUE)
		v2 = ThreeDVector(direction2,color=GREEN)
		v3 = ThreeDVector(direction3,color=RED)
		v4 = ThreeDVector(direction4,color=YELLOW)
		v5 = ThreeDVector(direction5,color=WHITE)

		self.add(v1,v2,v3,v4,v5)

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
		top_radius_to_bottom_radius = 1/2
		max_tip_length = 0.8
		max_bottom_radius =  0.2
		circle_side_width =2
		circle_side_color = None
		delta_radian = np.sqrt(3)/60
		fill_opacity = 1

		vector = ThreeDVector(
			direction,
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

		self.begin_ambient_camera_rotation(rate=1)

		self.wait(10)


class Test3(ThreeDScene):


	def construct(self):


		axes = ThreeDAxes()
		self.add(axes)
		self.set_camera_orientation(phi=60*DEGREES,theta=-90*DEGREES,distance=10)

		direction = [0,0,2]

		trtbr_list = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] #The constraction of "top_radius_to_bottom_radius"

		vectors = VGroup()

		n = len(trtbr_list)

		for x in range(n):
			v = ThreeDVector(
				direction,
				#[0,0,0],
				top_radius_to_bottom_radius=trtbr_list[x],
				color=BLUE)
			v.shift([-(n-1)/2 + x,0,0])
			vectors.add(v)
			#print(ORIGIN)

		self.add(vectors)

		#self.begin_ambient_camera_rotation(1)

		self.wait(2)


class Test4(ThreeDScene):


	def construct(self):


		axes = ThreeDAxes()
		self.add(axes)
		self.set_camera_orientation(phi=60*DEGREES,theta=90*DEGREES)

		def func(t):
			r = 1.5
			velocity_z = 0.2
			return np.array([
				r * np.cos(t),
				r * np.sin(t),
				velocity_z * t
				])

		curve = ParametricFunction(
			func,
			color=RED,
			t_min=0,t_max=3*TAU,
			shade_in_3d=True)

		#self.add(curve)

		v = ThreeDVector([1,1,1],[0,0,0],color=YELLOW)
		self.add(v)
		self.wait()

		self.play(
			v.set_direction,[2,0,0],
			v.set_position,[1,1,0],
			run_time=2)
		print('***1***',v.get_vector(),v.get_position())
		self.wait()

		self.play(
			v.set_vector_length,3,
			run_time=2)
		print('***2***',v.get_vector_length())
		self.wait()

		self.play(
			v.set_vector,[1,0,1],
			run_time=2)
		print('***3***',v.get_vector(),v.get_position(),v.get_vector_length())
		self.wait()

		print('***4***',
			v.get_tip_length(),
			v.get_tip_radius(),
			v.get_bottom_radius(),
			v.get_top_radius())

		self.play(FadeOut(v))

		v = ThreeDVector(color=GREEN)

		self.play(ShowCreation(curve))

		t = ValueTracker(0)
		v.move_along_curve(func=func,t=t.get_value(),dt=0.005)
		self.play(FadeIn(v))
		self.wait(0.5)


		def v_ud(obj):
			obj.move_along_curve(func=func,t=t.get_value(),dt=0.005)

		v.add_updater(v_ud)
		self.add(v)

		self.play(t.increment_value,3*TAU,rate_func=linear,run_time=5)

		self.wait(2)




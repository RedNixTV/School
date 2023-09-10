import math

class Physic:
	def __init__(self):
		self.input_values = {
			'east': 0.0,
			'west': 0.0,
			'windmill_time': 0.0,
			'bench_time': 0.0
		}
	
	def average_velocity_given_function(self):
		"""
			A Honda Civic travels in a straight line along a road. Its distance x
			 from a stop sign is given as a function of time t
			 by the equation x(t)=αt2−βt3
			, where α = 1.55 m/s2 and β= 0.0480 m/s3

			Calculate the average velocity of the car for the time interval  t=0
			  to  t=1.95  s .
			   answer: v = 2.84m/s
   
			Calculate the average velocity of the car for the time interval  t= 1.95  s
			  to  t=4.00  s
			 answer: v = 7.90m/s
			 
			 Calculate the instantaneous velocity of the car at  t= 5.00  s

			v = 12.3	m/s
		"""
		# Ask the user for input values
		print("The acceleration of a Honda Civic is given by x(t) = αt2−βt3")
		A = float(input("Enter function value A m/s^2: "))
		C = float(input("Enter function value B m/s^3: "))

	
		# Ask the user which calculation they want to perform
		print("Choose an option:")
		print("1. Calculate Instant Velocity")
		print("2. Calculate Average Velocity")
		print("3. Calculate when is the vehicle at rest")
		choice = input("Enter the corresponding number: ")
	
		# Display the results based on the user's choice
		if choice == '1':
			t_end = float(input("Enter function value end t: "))
			# Calculate average velocity (v av-x) using the formula
			instant_velocity = ((2*A * t_end) - (3*C * t_end**2)) 
			print(f"Calculate the instantaneous velocity of the car at  t = {t_end} ", instant_velocity, "m/s")
		elif choice == '2':
			t_end = float(input("Enter function value end t: "))
			t_start = float(input("Enter function value starting t: "))
			# Calculate average velocity (v av-x) using the formula
			velocity = (((A * t_end**2) - (C * t_end**3)) - ((A * t_start**2) - (C * t_start**3))) / (t_end - t_start)
			print(f"Calculate the average velocity of the car for the time interval  t= {t_start} to  t= {t_end} s   ", velocity, "m/s")
		if choice == '3':
			# Calculate average velocity (v av-x) using the formula
			at_rest = (2*A) / (3*C)
			print("How long after starting from rest is the car again at rest? =", at_rest, "m/s")
		else:
			print("Invalid choice. Please enter '1', '2', or '3'.")

		
		
	
	def get_user_input():
		# Ask the user the questions and store the values in the dictionary
		self.input_values['east'] = float(input("Starting from the front door of your ranch house, you walk (in meters) due east to your windmill: "))
		self.input_values['west'] = float(input("You turn around and then slowly walk (in meters) west to a bench, where you sit and watch the sunrise: "))
		self.input_values['windmill_time'] = float(input("It takes you (in seconds) to walk from your house to the windmill: "))
		self.input_values['bench_time'] = float(input("And then (in seconds) to walk from the windmill to the bench: "))
		
        
	def calculate_average_velocity(self):
		"""
		 Starting from the front door of your ranch house, you walk 55.0 m
		 due east to your windmill, turn around, and then slowly walk 35.0 m
		 west to a bench, where you sit and watch the sunrise. It takes you 25.0 s
		 to walk from your house to the windmill and then 41.0 s
		 to walk from the windmill to the bench.
		 For the entire trip from your front door to the bench, what is your average velocity?
		 v av−x = 0.303  ms
 

		"""
		self.get_user_input()
		
		# Calculate displacement and time using the dictionary values
		displacement = self.input_values['east'] - self.input_values['west']
		time = self.input_values['windmill_time'] + self.input_values['bench_time']

		# Calculate average velocity
		average_velocity = displacement / time
		
		# Display the results
		print("Displacement =", displacement, "m")
		print("Time =",time, "s")
		print("Average Velocity =", average_velocity, "m/s")
		
	
	def calculate_average_speed(self):
		"""
		 Starting from the front door of your ranch house, you walk 55.0 m
		 due east to your windmill, turn around, and then slowly walk 35.0 m
		 west to a bench, where you sit and watch the sunrise. It takes you 25.0 s
		 to walk from your house to the windmill and then 41.0 s
		 to walk from the windmill to the bench.
		 For the entire trip from your front door to the bench, what is your average speed?
		 v av−x = 0.303  ms
 

		"""
		self.get_user_input()
		
		# Calculate displacement and time using the dictionary values
		displacement = self.input_values['east'] + self.input_values['west']
		time = self.input_values['windmill_time'] + self.input_values['bench_time']

		# Calculate average velocity
		average_speed= displacement / time
		
		# Display the results
		print("Displacement =", displacement, "m")
		print("Time =",time, "s")
		print("Average speed =", average_speed, "m/s")
		
		
	
	def calculate_instant_velocity(self):
		"""
		 Starting from the front door of your ranch house, you walk 55.0 m
		 due east to your windmill, turn around, and then slowly walk 35.0 m
		 west to a bench, where you sit and watch the sunrise. It takes you 25.0 s
		 to walk from your house to the windmill and then 41.0 s
		 to walk from the windmill to the bench.
		 For the entire trip from your front door to the bench, what is your average velocity?
		 v av−x = 0.303  ms
 

		"""
		# Ask the user the questions and store the values in the dictionary
		self.input_values['east'] = float(input("End point : "))
		self.input_values['west'] = float(input("Start Point: "))
		self.input_values['windmill_time'] = float(input("End time: "))
		self.input_values['bench_time'] = float(input("Start time: "))
		
		# Calculate displacement and time using the dictionary values
		displacement = self.input_values['east'] - self.input_values['west']
		time = self.input_values['windmill_time'] - self.input_values['bench_time']

		# Calculate average velocity
		average_velocity = displacement / time
		
		# Display the results
		print("Displacement =", displacement, "m")
		print("Time =",time, "s")
		print("Find its instantaneous velocity at point  A=", average_velocity, "m/s")
		
		
	def calculate_constant_acceleration(self):
		"""
		 An antelope moving with constant acceleration covers the distance 75.0 m
		 between two points in time 8.00 s
		 Its speed as it passes the second point is 15.0 m/s
		 What is its speed at the first point? v = 3.75  ms
		 What is the acceleration? a = 1.41  ms2
		"""
		# Ask the user the questions and store the values in the dictionary
		distance_covered= float(input("Enter distance covered : "))
		t = float(input("enter t: "))
		v = float(input("Enter final velocity: "))

		
		# Calculate displacement and time using the dictionary values
		speed_at_first_point = 2*distance_covered/t - v
		acceleration =(v - speed_at_first_point) / t
		
		print("What is its speed at the first point? ",speed_at_first_point,"m/s")
		print("What is the acceleration? ",acceleration,"m/s^2")
		
	
	def baseball_acceleration(self):
		"""
		 The fastest measured pitched baseball left the pitcher's hand at a speed of 44.0 m/s
		 The pitcher was in contact with the ball over a distance of 1.50 m
		 and produced constant acceleration.
		 
		 What acceleration did he give the ball? ax = 645 m/s2
		 EXECUTE:  x−x0=1.50m ,  vx=44.0m/s and  v0x=0 v2x=v20x+2ax(x−x0)
  		 gives  ax=v2x−v20x2(x−x0)=(44.0m/s)22(1.50m)=645m/s2
		 
		 How much time did it take him to pitch it? t = 6.82×10−2 s
		 x−x0=(v0x+vx2)t gives  t=2(x−x0) v0x+vx= 2(1.50m)44.0m/s = 6.82×10−2s
		 EVALUATE: We could also use  vx=v0x+axt  to find  t=vx ax= 44.0m/s 645m/s2 = 6.82×10−2 s
         which agrees with our previous result. The acceleration of the ball is very large.
		"""
		# Ask the user the questions and store the values in the dictionary
		velocity1= float(input("left the pitcher's hand at a speed of : "))
		velocity2 = 0
		distance = float(input("The pitcher was in contact with the ball over a distance of: "))

		

		acceleration = ((velocity1**2)-velocity2)/(2*distance)
		time_to_pitch = velocity1/ acceleration
		
		print("What acceleration did he give the ball? ",acceleration,"m/s^2")
		print("How much time did it take him to pitch it?",time_to_pitch,"s")
		
	
	def slow_down_airbag(self):
		"""
		 During an auto accident, the vehicle's airbags deploy and slow down the passengers more gently than if they 
		 had hit the windshield or steering wheel. According to safety standards, airbags produce a maximum acceleration of 60g
 		 that lasts for only 36 ms (or less).
		 
		 How far (in meters) does a person travel in coming to a complete stop in 36  ms at a constant acceleration of 60 g?
		 using the equation of motion v = u + at,  final speed v = 0,  a = -60 * 9.81,  t = 36 * 10^-3, 
		 equation of motion v^2 = u^2 + 2as		
		 
		 IDENTIFY: If a person comes to a stop in 36  ms while slowing down with an acceleration of 60 g , or 588  m/s2
         , how far does he travel during this time?
         
         SET UP: Let  +x be the direction the person travels.  vx=0 (he stops),  
         ax is negative since it is opposite to the direction of the motion, and  t=36ms=3.6×10−2s
         The equations  vx=v0x+axt and  x=x0+v0xt+12a x t2 both apply since the acceleration is constant.
         
         EXECUTE: Solving  vx=v0x+axt for  v0x gives  v0x=−axt  Then  x=x0+v0xt+12axt2
         gives  x=−12axt2=−12(−588m/s2)(3.6×10−2s)2= 38cm
         
         EVALUATE: Notice that we were not given the initial speed, but we could find it:
         v0x=−axt=−(−588m/s2)(36×10−3s)=21m/s=47mph
 .
		 """
		# Ask the user the questions and store the values in the dictionary
		max_acceleration = float(input("Enter airbags maximum acceleration: "))
		time_accelerated = float(input("How was the max time that air bag accelerates for: "))

		

		acceleration = max_acceleration * 9.81
		print("Acceleration",acceleration)
		time = time_accelerated * (10**(-3))
		initial_velocity = acceleration * time
		print("U ",initial_velocity)
		distance_to_stop = ((initial_velocity**2) / (2*acceleration))
		
		print("How far (in meters) does a person travel in coming to a complete stop in 36  ms  at a constant acceleration of 60 g?",distance_to_stop,"m")
		
		
	def flea_jump(self):
		"""
		 If a flea can jump straight up to a height of 0.350  m, what is its initial speed as it leaves the ground? 2.62m/s
		 The equation of motion v^2  = u^2 -2gh, is used where v is the final speed and u is the initial speed and at highest point velocity is 0
		 and is substituted in the equation of motion to calculate initial speed. 
		 IDENTIFY: Apply the constant acceleration equations to the motion of the flea. After the flea leaves the ground,  ay=g
         , downward. Take the origin at the ground and the positive direction to be upward.
         
         SET UP: At the maximum height  vy=0
         vy=0,  y−y0=0.350m,  ay=−9.80 m/s2,  v0y=?  v2y=v20y+2ay(y−y0)
         
         EXECUTE:  v0y=−2ay(y−y0)−−−−−−−−−−√ =−2(−9.80m/s2)(0.350m)−−−−−−−−−−−−−−−−−−−−√ =2.62m/s
 
		 How long is it in the air? 0.535s
		 SET UP: When the flea has returned to the ground  y−y0= 0y − y0=0 ,  v0y = +2.62m/s,  ay =  −9.80m/s2,  t=?
		 y−y0 = v0yt + 12ayt^2
		 
		 EXECUTE: With  y−y0 = 0 this gives  t= −2v0yay =−2(2.62m/s) − 9.80m/s2 =0.535s
		 
		 EVALUATE: We can use  vy=v0y + ayt to show that with  v0y=2.62m/s,  vy=0 after  0.267s
		 """
		# Ask the user the questions and store the values in the dictionary
		flea_jump = float(input("flea can jump straight up to a height of?: "))

		

		acceleration = 2* 9.81
		initial_velocity = math.sqrt(flea_jump * acceleration)
		time_in_air = (initial_velocity / 9.81) *2
		
		print(f"If a flea can jump straight up to a height of {flea_jump}  m, what is its initial speed as it leaves the ground?",initial_velocity,"m/s")
		print("How long is it in the air?",time_in_air,"s")
		
		
	def juggler (self):
		"""
		 A juggler throws a bowling pin straight up with an initial speed of 6.40 m/s
		 The second kinematics equation is the relation between the distance, time, initial velocity, and acceleration of an object.
		 It is represented as: S = ut + 1/2 at^2
		 where
		 S is the distance
		 u is the initial velocity
		 t is the time
		 a is the acceleration
		 If the projectile started moving from the rest then the initial velocity of the projectile is zero.
		 
		 
		 IDENTIFY: The pin has a constant downward acceleration of  9.80m/s2 and returns to its initial position.
		 SET UP: We can use the kinematics formulas for constant acceleration.
		 EXECUTE: The kinematics formulas give  y−y0 = v0yt + 12ayt^2 . We know that  y−y0=0
		 , so  t = −2v0y / ay = −2(6.40m/s) / −9.80m/s2 = +1.31s
		 
		 EVALUATE: It takes the pin half this time to reach its highest point and the remainder of the time to return.
		 
		 How much time elapses until the bowling pin returns to the juggler's hand? +1.31s
		 
		 """
		# Ask the user the questions and store the values in the dictionary
		initial_velocity = float(input("A juggler throws a bowling pin straight up with an initial speed of ?: "))


		time_elapse = (2 * initial_velocity ) / 9.8
		
		print(f"How much time elapses until the bowling pin returns to the juggler's hand?",time_elapse,"s")
		
	
	def egg_throw (self):
	 	
		"""
		 An egg is thrown nearly vertically upward from a point near the cornice of a tall building. It just misses the cornice on the way down and passes a point a distance 47.0 m
		 below its starting point at a time 5.00 s after it leaves the thrower's hand. Air resistance may be ignored.
		 x ( t ) = vt - 1/2 g t2
		 
		 What is the initial speed of the egg? 15.1 s
		 How high does it rise above its starting point? 11.6 s
		 the magnitude of its velocity at the highest point ZERO
		 the magnitude of its acceleration at the highest point is same as a = g,   g = 9.8
	     What is the direction of its acceleration at the highest point? down
		 """
		# Ask the user the questions and store the values in the dictionary
		x_t = float(input("the cornice on the way down and passes a point a distance ?: "))
		time = float(input("below its starting point at a time __ s, after it leaves the thrower's hand?: "))


		initial_velocity = (((1/2)*-9.8) * (time**2) + x_t) / -5
		height = (initial_velocity**2) / (2 * 9.8)
	
		print(f"What is the initial speed of the egg?",initial_velocity,"s")
		print(f"How high does it rise above its starting point?",height,"s")
		
	
	def rocket_launch (self):
	 	
		"""
		 A rocket starts from rest and moves upward from the surface of the earth. For the first 10.0 s
 		 of its motion, the vertical acceleration of the rocket is given by ay=(2.80m/s3)t, where the +y
         -direction is upward.
         What is the height of the rocket above the surface of the earth at  t = 10.0  s? 467 m
         What is the speed of the rocket when it is 295  m above the surface of the earth?
		 """
		
		function_str = input("Enter function  (integrate function): ")
		time = float(input("For the first ___ s of its motion,: "))
		ay = float(input(" the vertical acceleration of the rocket is given by ay: "))
		y_t = float(input("What is the speed of the rocket when it is   ____ m above the surface of the earth??: "))
		

		initial_velocity = ay * (time**3 / 6)
		time = (y_t/(2.7/6))**(1/3)
		velocity_t = 2.7* ((time)**2)/2
	
		print(f"What is the height of the rocket above the surface of the earth at  t = 10.0  s?",initial_velocity,"m")
		print(f"What is the speed of the rocket when it is 295  m above the surface of the earth?",velocity_t,"m/s")
		
		
	
	def motorcycle_acceleration (self):
	 	
		"""
		 The acceleration of a motorcycle is given by ax(t)=At−Bt, where A=1.50m/s3
		 and B=0.120m/s4. The motorcycle is at rest at the origin at time t=0
		 ax(t) = At - Bt^2
		 
		 Find its velocity as a function of time. Letters  A and  B are not allowed in the answer. ( 0.75 m/s^3) t^2 - ( 0.04 m/s^4) t^3 m
		 dv = acceleration * distance * time
		 acceleration =  dv / dt, v is the velocity of the body
		 
		 Find its position as a function of time. Letters  A and  B are not allowed in the answer
		 Velocity, v = dx / dt, where x represents the position of body.
		 dx = vdt
		 
		 Calculate the maximum velocity it attains. Letters  A and  B are not allowed in the answer
		 v(t) = At^2 / 2 - Bt^3 / 3
		 dv/dt = At - Bt^2 = 0
		 """
		
		print("The acceleration of a motorcycle is given by ax(t) = At - Bt^2")
		A = float(input("where A=: "))
		B = float(input(" and B=: "))
		time_0 = float(input("The motorcycle is at rest at the origin at time t=: "))
		

		result_a = A/2 
		result_b = B/3
		result_c = A/6
		result_d = B/12
		max_velocity_time = (A)/(B)
		max_velocity = result_a * max_velocity_time**2 - result_b * max_velocity_time**3
	
		print(f"Find its velocity as a function of time. Letters  A and  B are not allowed in the answer. v(t) = (",result_a,"m/s^3) t^2 - (",result_b,"m/s^4) t^3","m")
		print(f"Find its position as a function of time. Letters  A and  B are not allowed in the answer. x(t) = (",result_c,"m/s^3) t^3 - (",result_d,"m/s^4) t^4","m")
		print(f"Calculate the maximum velocity it attains. Letters  A and  B are not allowed in the answer.",max_velocity,"m/s")
		
	
	
	def user_choice(self):
		print("Choose an option:")
		print("1. Calculate average velocity")
		print("2. Calculate average speed")
		print("3. Calculate average velocity or instant velocity given a function")
		print("4. Calculate instant velocity")
		print("5. What is its speed at the first point?")
		print("6. What acceleration did he give the ball?")
		print("7. How far (in meters) does a person travel in coming to a complete stop in 36  ms  at a constant acceleration of 60 g?")
		print("8. If a flea can jump straight up to a height of 0.350  m, what is its initial speed as it leaves the ground?")
		print("9. How much time elapses until the bowling pin returns to the juggler's hand?")
		print("10. How much time elapses until the bowling pin returns to the juggler's hand?")
		print("11. What is the height of the rocket above the surface of the earth at  t= 10.0  s??")
		print("12. Find its velocity as a function of time. Letters  A and  B are not allowed in the answer.?")
		choice = input("Enter the corresponding number: ")
		if choice == '1':
			self.calculate_average_velocity()
		elif choice == '2':
			self.calculate_average_speed()
		elif choice == '3':
			self.average_velocity_given_function()
		elif choice == '4':
			self.calculate_instant_velocity()
		elif choice == '5':
			self.calculate_constant_acceleration()
		elif choice == '6':
			self.baseball_acceleration()
		elif choice == '7':
			self.slow_down_airbag()
		elif choice == '8':
			self.flea_jump()
		elif choice == '9':
			self.juggler()
		elif choice == '10':
			self.egg_throw()
		elif choice == '11':
			self.rocket_launch()
		elif choice == '12':
			self.motorcycle_acceleration()
		else:
			print("Invalid choice. Please enter '1' through '10'.")



# Create an instance of the class
calculator = Physic()

# Call the average_velocity method to calculate and display the result
calculator.user_choice()

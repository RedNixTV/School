import math
import pandas as pd

class Physic:
	def __init__(self):
		self.equation = None
		self.variables = None

	def average_velocity(self):
		# Ask the user to enter the stopping point X2 and starting point X1
		X2 = float(input("Enter the stopping point (X2) in meters: "))
		X1 = float(input("Enter the starting point (X1) in meters: "))

		# Calculate the displacement
		displacement = X2 - X1

		# Ask the user to enter the ending time T2 and starting time T1
		T2 = float(input("Enter the ending time (T2) in seconds: "))
		T1 = float(input("Enter the starting time (T1) in seconds: "))

		# Calculate the change in time
		change_in_time = T2 - T1

		# Calculate the average velocity
		average_velocity = displacement / change_in_time

		# Print the result
		print("Average Velocity =", average_velocity, "m/s")
		print("The average velocity is also known as the slope = rise/run")
		print("a race along a straight line is really a competition to see whose average velocity")
		print(", υav−x, has the greatest magnitude")
		print("The prize goes to the competitor who can travel the displacement Δx from ")
		print("the start to the finish line in the shortest time interval, Δt")
		print("the average velocity of a particle during a time interval can’t tell us how fast, or in what direction, ")
		print("the particle was moving at any given time during the interval")
		print("For that we need to know the instantaneous velocity, or the velocity at a specific ")
		print("instant of time or specific point along the path")
		print("In the language of calculus, the limit of Δx/Δt as Δt approaches zero is called ")
		print("the derivative of x with respect to t and is written dx/dt.")
		print("We use the symbol Vx, with no “av” subscript, for the instantaneous velocity ")
		print("along the x-axis, or the instantaneous x-velocity")
		print("The time interval Δt is always positive, so υx has the same algebraic sign as Δx.")
		print("A positive value of Vx means that x is increasing and the motion is in the positive x-direction; ")
		print("a negative value of Vx means that x is decreasing and the motion is in the negative x-direction.")
		print("An object can have positive x and negative Vx, or the reverse; x tells us where the object is, ")
		print("while Vx tells us how it’s moving")
		print("When we use the term “velocity,” we’ll always mean instantaneous rather than average velocity")
		print("We use the term speed to denote distance traveled divided by time, on either an average or an instantaneous basis.")
		print("Instantaneous speed, for which we use the symbol V with no subscripts, measures how fast a particle ")
		print("is moving; instantaneous velocity measures how fast and in what direction it’s moving.")
		print("Instantaneous speed is the magnitude of instantaneous velocity and so can never be negative")
		print("Average speed is not the magnitude of average velocity.")
		print("When César Cielo set a world record in 2009 by swimming 100.0 m in 46.91 s, his average speed ")
		print("was (100.0 m)/(46.91 s)=2.132 m/s. But because he swam two lengths in a 50 m pool, he started and ")
		print("ended at the same point and so had zero total displacement and zero average velocity!")
		print("Both average speed and instantaneous speed are scalars, not vectors, because these quantities ")
		print("contain no information about direction.")

	def average_n_instant_velocity(self):
		"""
		A cheetah is crouched 20 m to the east of a vehicle (Fig. 2.6a). At time t=0 the cheetah begins to run due east toward an 
		antelope that is 50 m to the east of the vehicle. During the first 2.0 s of the chase, the cheetah’s x-coordinate varies with 
		time according to the equation x=20 m+(5.0 m/s2)t2.
		(a) Find the cheetah’s displacement between t1=1.0 s and t2=2.0 s.
		(b) Find its average velocity during that interval. (c) Find its instantaneous velocity at t1=1.0 s by taking Δt=0.1 s,
		then 0.01 s, then 0.001 s.
		(d) Derive an expression for the cheetah’s instantaneous velocity as a function of time, and use it to find υx at t=1.0 s
		and t=2.0 s.
		"""
		meter_traveled = float(input("Enter constant of equation (20 m): "))
		speed = float(input("Enter speed (5 m/s): "))
		time1 = float(input("Enter time elapsed for time 1: "))
		time2 = float(input("Enter time elapsed for time 2: "))
		time3 = float(input("Enter time to find instant velocity: "))
		sp = float(input("Enter cheetah starting point: "))
		time4 = float(input("Enter time to how much ground cheetah cover during that time: "))
	
		#user given function
		distance_traveled_1 = meter_traveled + (speed)*time1**2
		distance_traveled_2 = meter_traveled + (speed)*time2**2
		#calculate displacement
		displacement = distance_traveled_2 - distance_traveled_1
		time = time2-time1
		#calculate velocity
		average_velocity = displacement / time
		#get the derivative of the user given equation so t^2 becomes 2t to get instant velocity
		instant_velocity = 2*(speed)*time3
		#calculate distance cheetah covered from t0 to user specified time
		distance_cheetah_cover = (meter_traveled + (speed)*time4**2) - sp
		print(f"Distance traveled in {time1} seconds:",distance_traveled_1,"m/s")
		print(f"Distance traveled in {time2} seconds:",distance_traveled_2,"m/s")
		print(f"Displacement in {time2-time1} seconds:",displacement,"m")
		print(f"Average velocity during this interval is {time2-time1} s :",average_velocity,"m/s")
		print(f"Instant velocity at specified time {time3} s :",instant_velocity,"m/s")
		print(f"Distance cheetah covered in {time4} s :",distance_cheetah_cover,"m")
		print("To calculate the average velocity of an object in straight-line motion, first find its displacement ")
		print("(final coordinate minus initial coordinate) during a time interval. Then divide by the time interval. ")
		print("To calculate the object’s instantaneous velocity (its average velocity over an infinitesimally short ")
		print("time interval), take the derivative of its position with respect to time.")
		print("Using an x-t graph to go from (a), (b) average x-velocity to (c) instantaneous x-velocity υx. In (c) we find the slope")
		print("of the tangent to the x-t curve by dividing any vertical interval (with distance units) along the tangent by the")
		print("corresponding horizontal interval (with time units).")
		print("If the tangent to the x-t curve slopes upward to the right, as in Fig. 2.7c, then its slope is positive, the x-velocity")
		print("is positive, and the motion is in the positive x-direction. If the tangent slopes downward to the right, the slopes of")
		print(" the x-t graph and the x-velocity are negative, and the motion is in the negative x-direction. When the tangent is")
		print("horizontal, the slope and the x-velocity are zero. Figure 2.8 illustrates these three possibilities.")
	


	def average_velocity_sign_rules(self):
		# Rules for the sign of x-velocity
		print("Positive and increasing: sign is positive: particle is moving in the +x direction")
		print("Positive and decreasing: sign is negative; particle is moving in the -x direction")
		print("Negative and increasing: sign is positive: particle is moving in the +x direction")
		print("Negative and decreasing: sign is negative; particle is moving in the -x direction")
		print("In our example positive Vav−x means motion to the right")
		print("In our example negative Vav−x means motion to the left")
		print("But that’s only because we chose the +x-direction to be to the right.")
		print("Had we chosen the +x-direction to be to the left, the average x-velocity υav−x")
		print("would have been negative for the dragster moving to the right and positive for the truck moving to the left")
		print("the direction of the coordinate axis is yours to choose")
		print("The average x-velocity depends on only the total displacement Δx=x2−x1")
		print("that occurs during the time interval Δt=t2−t1, not on what happens during the time interval.")
		print("At time t1 a motorcycle might have raced past the dragster at point P1 in Fig. 2.1, ")
		print("then slowed down to pass through point P2 at the same time t2 as the dragster..")
		print("Both vehicles have the same displacement during the same time interval and so have the same average x-velocity.")
		print("The rules that we presented in Table 2.1 (Section 2.1) for the sign of average x-velocity ")
		print("υav−x also apply to the sign of instantaneous x-velocity υx.")
	
	def acceleration_explanation(self):
		print("Just as velocity describes the rate of change of position with time, acceleration describes the rate of change")
		print("of velocity with time. Like velocity, acceleration is a vector quantity. When the motion is along a straight line")
		print("In everyday language, acceleration refers only to speeding up; in physics, acceleration refers to any kind of")
		print("velocity change, so we say an object accelerates if it is either speeding up or slowing down")
		print("Velocity describes how an object’s position changes with time; it tells us how fast and in what direction the")
		print("object moves.")
		print("Acceleration describes how the velocity changes with time; it tells us how the speed and direction of motion change.")
		print("Another difference is that you can feel acceleration but you can’t feel velocity.")
		print("If you’re a passenger in a car that accelerates forward and gains speed, you feel pushed backward in your seat; ")
		print("if it accelerates backward and loses speed, you feel pushed forward.")
		print("If the velocity is constant and there’s no acceleration, you feel neither sensation.")
		print("To calculate the average acceleration of an object in straight-line motion, first find the change in its velocity")
		print("(final velocity minus initial velocity) during a time interval. Then divide by the time interval.")
		print("")
		print("Notice that when the average x-acceleration has the same algebraic sign as the initial velocity, as in intervals (a)")
		print(" and (c), the astronaut goes faster. When A_av−xhas the opposite algebraic sign from the initial velocity, as in")
		print("intervals (b) and (d), she slows down. Thus positive x-acceleration means speeding up if the x-velocity is positive")
		print("[interval (a)] but slowing down if the x-velocity is negative [interval (d)]. Similarly, negative x-acceleration means ")
		print("speeding up if the x-velocity is negative [interval (c)] but slowing down if the x-velocity is positive [interval (b)].")
	
	def acceleration(self):
		"""
		An astronaut has left an orbiting spacecraft to test a new personal maneuvering unit. As she moves along a straight line, 
		her partner on the spacecraft measures her velocity every 2.0 s, starting at time t=1.0 s:
		t		Vx			t			Vx
		1s		0.8 m/s	    9 s		-0.4 m/s
		3s		1.2 m/s		11s		-1.0 m/s
		5s		1.6 m/s		13.0s	-1.6 m/s
		7s		1.7 m/s		15s		-0.8 m/s
		Find the average x-acceleration, and state whether the speed of the astronaut increases or decreases over each of 
		these 2.0 s time intervals: (a) t1=1.0 s to t2=3.0 s; (b) t1=5.0 s to t2=7.0 s; (c) t1=9.0 s to t2=11.0 s; (d) t1=13.0 s to 
		t2=15.0 s.
		IDENTIFY and SET UP We’ll use Eq. (2.4) to determine the average acceleration Aav−x from the change in velocity 
		over each time interval. To find the changes in speed, we’ll use the idea that speed V is the magnitude of the 
		instantaneous velocity Vx.
	
		Aav−x=(1.2 m/s−0.8 m/s)/(3.0 s−1.0 s)= 0.2 m/s2. The speed (magnitude of instantaneous x-velocity) increases from 
		0.8 m/s to 1.2 m/s.
		Aav−x=(1.2 m/s−1.6 m/s)/(7.0 s−5.0 s)= −0.2 m/s2. The speed decreases from 1.6 m/s to 1.2 m/s.
		Aav−x=[−1.0 m/s−(−0.4 m/s)]/(11.0 s−9.0 s)=−0.3 m/s2. The speed increases from 0.4 m/s to 1.0 m/s.
		Aav−x=[−0.8 m/s−(−1.6 m/s)]/(15.0 s−13.0 s)=0.4 m/s2. The speed decreases from 1.6 m/s to 0.8 m/
		"""
		velocity_X2 = float(input("Enter velocity at X2 (m/s): "))
		velocity_X1 = float(input("Enter velocity at X1 (m/s): "))
		time_t2 = float(input("Enter time at t2 (s): "))
		time_t1 = float(input("Enter time at t1 (s): "))
	
		acceleration = round((velocity_X2 - velocity_X1) / (time_t2 - time_t1), 1)
		print(f"The acceleration A_av-x is: {acceleration} m/s^2")
		
		
	def instant_acceleration(self):
		"""
		print("To define the instantaneous acceleration at point P1,")
		print("we take point P2 in Fig. 2.11 to be closer and closer to P1")
		print("so that the average acceleration is computed over shorter and shorter time intervals.")
		print("Ax = limit as change in time approaches 0 is (change Vx)/(change time) = (dVx)/(dt)")
		print("ax is the x-component of the acceleration vector, which we call the instantaneous x-acceleration;")
		print("in straight-line motion, all other components of this vector are zero. From now on, when we use")
		print("the term “acceleration,” we’ll always mean instantaneous acceleration, not average acceleration.")
		print("(a) Find the change in x-velocity of the car in the time interval t1=1.0 s to t2=3.0 s.")
		print("(b) Find the average x-acceleration in this time interval.")
		print("(c) Find the instantaneous x-acceleration at time t1=1.0 s by taking Δt to be first 0.1 s, then 0.01 s, then 0.001 s.")
		print("(d) Derive an expression for the instantaneous x-acceleration as a function of time,")
		print("    and use it to find ax at t=1.0 s and t=3.0 s.")
		print("In that example we found the average x-velocity from the change in position over shorter and shorter time intervals,") 
		print("and we obtained an expression for the instantaneous x-velocity by differentiating the position as a function of time.")
		print("In this example we have an exact parallel.")
		print("Using Eq. (2.4), we’ll find the average x-acceleration from the change in x-velocity over a time interval.")
		print("Likewise, using Eq. (2.5), we’ll obtain an expression for the instantaneous x-acceleration by differentiating") 
		print("the x-velocity as a function of time.")
		"""

		equation_velocity = float(input("Enter constant of equation (60 m/s): "))
		equation_acceleration = float(input("Enter integral of acceleration (0.50 m/s^3): "))
		time1 = float(input("Enter time elapsed for time 1: "))
		time2 = float(input("Enter time elapsed for time 2: "))
		time3 = float(input("Enter time to find instant acceleration: "))
		#Before we can apply Eq. (2.4), we must find the x-velocity at each time from the given equation. At t1=1.0 s
		#and t2=3.0 s,the velocities are
		#user given function
		acceleration_V1x = equation_velocity + (equation_acceleration)*time1**2
		acceleration_V2x = equation_velocity + (equation_acceleration)*time2**2
		#The change in x-velocity ΔVx between t1=1.0 s and t2=3.0 s is
		#calculate displacement
		change_Vx = acceleration_V2x - acceleration_V1x
		time = time2-time1
		#The average x-acceleration during this time interval of duration t2−t1=2.0 s is
		average_acceleration_Aav_x = change_Vx / time
		#get the derivative of the user given equation so t^2 becomes 2t to get instant velocity
		instant_acceleration_Ax = 2*(equation_acceleration)*time3
		#calculate distance cheetah covered from t0 to user specified time
		#distance_cheetah_cover = (meter_traveled + (speed)*time4**2) - sp
		print(f"Acceleration {time1} seconds:",acceleration_V1x,"m/s")
		print(f"Acceleration in {time2} seconds:",acceleration_V2x,"m/s")
		print(f"Change in x-velocity in {time2-time1} seconds between {time2}s and {time1}s is:",change_Vx,"m/s")
		print(f"Average x-acceleration Aav-x during this interval is {time2-time1} s :",average_acceleration_Aav_x,"m/s^2")
		print(f"Instant velocity Ax at specified time {time3} s :",instant_acceleration_Ax,"m/s")
		print("To calculate an object’s instantaneous acceleration (its average acceleration over an infinitesimally short ")
		print("time interval), take the derivative of its velocity with respect to time.")
		print("Thus, on a graph of x-velocity as a function of time,")
		print("the instantaneous x-acceleration at any point is equal to the slope of the tangent to the curve at that point.")
		print("Tangents drawn at different points along the curve in Fig. 2.12 have different slopes,")
		print("so the instantaneous x-acceleration varies with time.")


	def instant_acceleration_sign_rules(self):
		# Rules for the sign of x-acceleration
		print("The algebraic sign of the x-acceleration does not tell you whether an object is speeding up or slowing down.")
		print("You must compare the signs of the x-velocity and the x-acceleration.")
		print("As we saw in Example 2.2, when Vx and Ax have the same sign, the object is speeding up.")
		print("When Vx and Ax have opposite signs, the object is slowing down.")
		print("Table 2.3 summarizes these rules, and Fig. 2.13 illustrates some of them.")
		print("Positive and increasing: sign is positive: particle is moving in the +x direction and speeding up")
		print("Positive and decreasing: sign is negative; particle is moving in the +x direction and slowing down")
		print("Negative and increasing: sign is positive: particle is moving in the +x direction and slowing down")
		print("Negative and decreasing: sign is negative; particle is moving in the -x direction and speeding up")
		
	
	def constant_acceleration_explanation(self):
		print("The simplest kind of accelerated motion is straight-line motion with constant acceleration.")
		print("In this case, the velocity changes at the same rate throughout the motion.")
		print("As an example, a falling object has a constant acceleration if the effects of the air are not important.")
		print("Since the x-acceleration is constant,")
		print("the ax-t graph (graph of x-acceleration versus time) in Fig. 2.16 is a horizontal line.")
		print("The graph of x-velocity versus time, or υx-t graph,")
		print("has a constant slope because the acceleration is constant,")
		print("so this graph is a straight line (Fig. 2.17).")
		print("An acceleration-time (ax-t) graph of straight-line motion with constant positive x-acceleration ax.")
		print("A velocity-time (vx-t) graph of straight-line motion with constant positive x-acceleration ax. The initial x-velocity v0x") 
		print("is also positive in this case.")
		print("When the x-acceleration Ax is constant, the average x-acceleration Aav−x for any time interval is the same as Ax.")
		print("This makes it easy to derive equations for the position x and the x-velocity Vx as functions of time.")
		print("To find an equation for Vx, we first replace Aav−x in Eq. (2.4) by Ax:")
		print("Ax = (V2x -V0x) / (t2 - t1)")
		print("Now we let t1 = 0")
		print("and let t2 be any later time t.")
		print("We use the symbol V0x for the initial x-velocity at time t = 0;")
		print("the x-velocity at the later time t is Vx.")
		print("Then Eq. (2.7) becomes Ax = (Vx -V0x) / (t - 0)  or Vx = V0x + Axt")
		print("The change in x-velocity Vx−V0x of the particle between t=0")
		print("and any later time t equals the area under the ax-t graph between those two times.")
		print("The area Axt is indeed equal to the change in velocity Vx−V0x.")
		print("In Section 2.6 we’ll show that even if the x-acceleration is not constant,")
		print("the change in x-velocity during a time interval is still equal to the area under the Ax-t curve,")
		print("although then Eq. (2.8) does not apply.")
		print("Next we’ll derive an equation for the position x as a function of time when the x-acceleration is constant.")
		print("The position at time t=0, called the initial position, is x0.")
		print("The position at time t is simply x.")
		print("Thus for the time interval Δt=t−0 the displacement is Δx=x−x0, and Eq. (2.2) gives")
		print("Vav-x = (X- X0) / (t) or (contant x-acceleration only) Vav-x = 1/2 (V0x + Vx) or = V0x + 1/2 Axt")
		print("tells us that the particle’s position at time t")
		print("is the sum of three terms: its initial position at t=0, x0,")
		print("plus the displacement υ0xt it would have if its x-velocity remained equal to its initial value,")
		print("plus an additional displacement 1/2Axt2 caused by the change in x-velocity.")
		print("Postion at time t of a particle with constant x-aceleration: x = X0 + V0xt + 1/2 Ax t^2")
		print("t for time, x for postion at time t of a particle iwth a constant x-acceleration, x-velocity of the particle at tim 0")
		print("Constant x-acceleration of the particle ax")
		print("A graph of Eq. (2.12)—that is, an x-t graph for motion with constant x-acceleration (Fig. 2.18a)—is always .")
		print("a parabola. The curve intercepts the vertical axis (x-axis) at x0, the position at t=0. The slope of the tangent at")
		print("t=0 equals υ0x, the initial x-velocity, and the slope of the tangent at any time t equals the x-velocity υx at that time.")
		print("The slope and x-acceleration ax are continuously increasing, so the x-acceleration ax is positive and the graph in") 
		print("Fig. 2.18b is concave up (it curves upward).")
		print("If ax is negative, the x-t graph is a parabola that is concave down (has a downward curvature).")
		print("If there is zero x-acceleration, the x-t graph is a straight line;")
		print("if there is constant x-acceleration, the additional 12axt2 term in Eq. (2.12) for x as a function of t curves the graph into a parabola (Fig. 2.19a).")
		print("Similarly, if there is zero x-acceleration, the υx-t graph is a horizontal line (the x-velocity is constant).")
		print("Adding a constant x-acceleration in Eq. (2.8) gives a slope to the graph (Fig. 2.19b).")
		
	def constant_acceleration(self):
		"""
		print("A motorcyclist heading east through a small town accelerates at a constant 4.0 m/s2")
		print("after he leaves the city limits (Fig. 2.20). At time t=0")
		print("he is 5.0 m east of the city-limits signpost while he moves east at 15 m/s.")
		print("(a) Find his position and velocity at t=2.0 s.")
		print("(b) Where is he when his speed is 25 m/s?")
		message = "IDENTIFY and SET UP\n" \
          "The x-acceleration is constant, so we can use the constant-acceleration equations.\n" \
          "We take the signpost as the origin of coordinates (x=0)\n" \
          "and choose the positive x-axis to point east (see Fig. 2.20, which is also a motion diagram).\n" \
          "The known variables are the initial position and velocity, x0=5.0 m\n" \
          "and υ0x=15 m/s,\n" \
          "and the acceleration, ax=4.0 m/s2.\n" \
          "The unknown target variables in part (a) are the values of the position x\n" \
          "and the x-velocity Vx\n" \
          "at t=2.0 s;\n" \
          "the target variable in part (b) is the value of x\n" \
          "when Vx=25 m/s."
		# Print the message with line breaks
		print(message)
		print("EXECUTE (a) Since we know the values of x0, υ0x, and ax,")
		print("Table 2.5 tells us that we can find the position x at t=2.0 s")
		print("by using Eq. (2.12) and the x-velocity υx at this time by using Eq. (2.8):")
		
		print("(b) We want to find the value of x when υx=25 m/s,")
		print("but we don’t know the time when the motorcycle has this velocity.")
		print("Table 2.5 tells us that we should use Eq. (2.13), which involves x,")
		print("υx, and ax but does not involve t:")
		print("Vx^2: V0x^2 + 2Ax * (X - X0)")
		print("Solving for x and substituting the known values, we find")
		print("X = X0 + (Vx^2 - V0x^2)/2Ax")
		"""
		# Ask the user to enter values
		X0 = float(input("Enter X0 (Initial position in meters): "))
		V0x = float(input("Enter V0x (Initial x-velocity in m/s): "))
		t = float(input("Enter t (Time in seconds): "))
		Ax = float(input("Enter Ax (Acceleration in m/s^2): "))
		# Ask the user for the value of Vx
		Vx = float(input("Enter the value of Vx when you don't know time it has that velocity: "))

		# Calculate particle position at time t
		x = X0 + V0x * t + (1/2) * Ax * t**2
		# Calculate x-velocity at time t
		x_velocity_Vx = V0x + Ax * t
		# Calculate X using the formula given Vx
		X = X0 + (Vx**2 - V0x**2) / (2 * Ax)

		# Print the results
		print("Position x as a value of time t:", x, "meters")
		print("x-velocity Vx at time t:", x_velocity_Vx, "m/s")
		# Print the result
		print(f"The value of X when Vx is {Vx} m/s is {X} meters.")
		print("By using one or more of the four equations in Table 2.5,")
		print("you can solve any problem involving straight-line motion with constant acceleration.")
		
		
	def different_acceleration(self):
		print("A motorist traveling at a constant 15 m/s")
		print("(54 km/h, or about 34 mi/h) passes a school crossing where the speed limit is 10 m/s")
		print("(36 km/h, or about 22 mi/h).")
		print("Just as the motorist passes the school-crossing sign, a police officer on a motorcycle stopped there")
		print(" starts in pursuit with constant acceleration 3.0 m/s2")
		print("(Fig. 2.21a).")
		print("(a) How much time elapses before the officer passes the motorist?")
		print("At that time, (b) what is the officer’s speed and (c) how far has each vehicle traveled?")
		identify_and_setup = """
		IDENTIFY and SET UP Both the officer and the motorist move with constant acceleration (equal to zero for the motorist),
		so we can use the constant-acceleration formulas.
		We take the origin at the sign, so x0=0 for both, and we take the positive direction to the right.
		Let xP and xM represent the positions of the police officer and the motorist at any time.
		Their initial velocities are υP0x=0 and υM0x=15 m/s, and their accelerations are aPx=3.0 m/s2 and aMx=0.
		Our target variable in part (a) is the time when the officer and motorist are at the same position x; Table 2.5 tells us that 
		Eq. (2.12) is useful for this part.
		In part (b) we’ll use Eq. (2.8) to find the officer’s speed υ (the magnitude of her velocity) at the time found in part (a).
		In part (c) we’ll use Eq. (2.12) again to find the position of either vehicle at this same time.

		Figure 2.21b shows an x-t graph for both vehicles.
		The straight line represents the motorist’s motion, xM=xM0+υM0xt=υM0xt.
		The graph for the officer’s motion is the right half of a parabola with upward curvature:
		A good sketch shows that the officer and motorist are at the same position (xP=xM) at about t=10 s,
		at which time both have traveled about 150 m from the sign.
		print("Xp = Xp0 + Vp0xt + 1/2Apxt^2 = (1/2)Apxt^2")
		"""
		execute = """
		EXECUTE (a) To find the value of the time t,
		at which the motorist and police officer are at the same position, we set xP=xM
		by equating the expressions above and solving that equation for t:
		Both vehicles have the same x-coordinate at two times, as Fig. 2.21b indicates. At t=0,
		the motorist passes the officer; at t=10 s,
		the officer passes the motorist.

		(b) We want the magnitude of the officer’s x-velocity υPx, at the time t, found in part (a). Substituting the values of υP0x
		and aPx into Eq. (2.8) along with t=10 s from part (a), we find
		Vpx = Vp0x + Apxt 
		"""
		# Ask the user for initial velocities and accelerations
		VP0x = float(input("Enter initial velocity of the police officer (VP0x = 0) in m/s: "))
		VM0x = float(input("Enter initial velocity of the motorist (VM0x = 15 m/s) in m/s: "))
		APx = float(input("Enter acceleration of the police officer (APx = 3.0) in m/s^2: "))
		AMx = float(input("Enter acceleration of the motorist (AMx = 0) in m/s^2: "))

		# Calculate the value of 't'
		t = 2 * VM0x / APx

		# Calculate υPx
		VPx = VP0x + APx * t

		# Calculate Xm
		Xm = VM0x * t
		# Calculate Xo
		Xo = (1/2) * APx * t**2

		# Print the calculated 't'
		print(f" t = {t} seconds, time at which the motorist and police officer are at the same position.")
		# Print the calculated υPx
		print(f"The magnitude of the officer’s x-velocity (VPx) at time {t} s is {abs(VPx)} m/s.")
		# Print the calculated Xm
		print(f"The distance traveled by the motorist in {t} s is {Xm} meters.")
		# Print the calculated Xo
		print(f"The distance traveled by the officer in {t} s is {Xo} meters.")
		# Verify if Xo and Xm are equal after 10 seconds
		if Xo == Xm:
			print("Verification: The officer and the motorist have gone equal distances after 10 s.")
		else:
			print("Verification failed: The distances covered by the officer and the motorist are not equal after 10 s.")
			
		print("In straight-line motion, one object meets or passes another at the time when the two objects have the same ")
		print("coordinate x (and so their x-t graphs cross). The objects can have different velocities at that time.")

	
	def free_falling_explanation(self):
		print("Don’t confuse speed, velocity, and acceleration in free fall")
		print("Speed can never be negative; velocity can be positive or negative, depending on the direction of motion.")
		print("In free fall, speed and velocity change continuously but acceleration (the rate of change of velocity) is constant")
		print("and downward.")
		print("The constant acceleration of a freely falling object is called the acceleration due to gravity, and we denote its")
		print("magnitude with the letter g. We’ll frequently use the approximate value of g at or near the earth’s surface:")
		print("g = 9.8 m/s^2, 980 cm/s^2, 32.2 ft/s^2")
		print("g is always a positive number Because g is the magnitude of a vector quantity, it is always a positive number.")
		print("If you take the positive y-direction to be upward, as we do in most situations involving free fall,")
		print("the y-component of the acceleration is negative and equal to −g.")
		print("Be careful with the sign of g, or you’ll have trouble with free-fall problems.")
		print("A one-euro coin is dropped from the Leaning Tower of Pisa and falls freely from rest. What are its position")
		print("and velocity after 1.0 s, 2.0 s, and 3.0 s? Ignore air resistance.")
		
	def free_falling(self):
		identify_and_setup = """
		IDENTIFY and SET UP “Falls freely” means “falls with constant acceleration due to gravity,” so we can use the 
		constant-acceleration equations. The right side of Fig. 2.23 shows our motion diagram for the coin. The motion 
		is vertical, so we use a vertical coordinate axis and call the coordinate y instead of x.
		 We take the origin at the starting point and the upward direction as positive. Both the initial coordinate y0 and initial y-
		velocity υ0y are zero. The y-acceleration is downward (in the negative y-direction), so ay=−g=−9.8 m/s2.
		 (Remember that g is a positive quantity.) Our target variables are the values of y and υy
		 at the three given times. To find these, we use Eqs. (2.12) and (2.8) with x replaced by y.
		 Our choice of the upward direction as positive means that all positions and velocities we calculate will be negative.
		"""
		execute = """
		EXECUTE: At a time t after the coin is dropped, its position and y-velocity are
		y = y0 + V0yt + (1/2)*(Ay)t^2
		vy = V0y +Ayt
		When t=1.0 s,
		 y=(−4.9 m/s2)(1.0 s)2=−4.9 m
		 and υy =(−9.8 m/s2)(1.0 s)=−9.8 m/s;
		 after 1.0 s,
		 the coin is 4.9 m
		 below the origin (y
		 is negative) and has a downward velocity (υy
		 is negative) with magnitude 9.8 m/s.

		We can find the positions and y-
		velocities at 2.0 s and 3.0 s in the same way. The results are y=−20 m
		 and υy=−20 m/s
		 at t=2.0 s,
		 and y=−44 m
		 and υy=−29 m/s
		 at t=3.0 s.
		"""

		
		# Ask the user for inputs
		y0 = float(input("Enter the initial height (y0) in meters: "))
		V0yt = float(input("Enter the initial vertical velocity (V0yt) in m/s: "))
		Ay_input = input("Enter the acceleration due to gravity (Ay) in m/s^2 or leave blank: ")
		if Ay_input.strip():  # Check if the input is not empty
			Ay = float(Ay_input)
		else:
			Ay = 9.8  # Default value

		# Ask the user for time values
		time_values = []  # Store the time values entered by the user

		while True:
			t = input("Enter a time in seconds (or 'q' to quit): ")
	
			if t.lower() == 'q':
				break  # Exit the loop if the user enters 'q'

			try:
				t = float(t)  # Try to convert input to float
				time_values.append(t)  # Add the time value to the list
			except ValueError:
				print("Invalid input. Please enter a valid number.")

		# Calculate and present the results for each time
		for t in time_values:
			# Calculate the position and vertical velocity
			y = y0 + V0yt * t + 0.5 * (-Ay) * t**2
			Vy = V0yt + (-Ay) * t

			# Print the results with no decimal points
			print(f"At time t = {t} seconds:")
			print(f"Vertical position (y) = {y:.1f} meters")
			print(f"Vertical velocity (Vy) = {Vy:.1f} m/s")
			print()
		# Create a dataframe to store the results
		df = pd.DataFrame(columns=['time', 'position', 'y-velocity'])
		print()
		# Calculate and append the results for each time
		for t in time_values:
			# Calculate the position and vertical velocity
			y = y0 + V0yt * t + 0.5 * (-Ay) * t**2
			Vy = V0yt + (-Ay) * t

			# Append the results to the dataframe
			df = pd.concat([df, pd.DataFrame({'time': [t], 'position': [y], 'y-velocity': [Vy]})], ignore_index=True)

		# Display the results DataFrame
		print(df)
		print()
		print("By using one or more of the four equations in Table 2.5 with x")
		print("replaced by y,")
		print("the positive y-direction chosen to be upward, and acceleration ay=-g,")
		print("you can solve any free-fall problem.")
		print()
		
	
	def free_fall_up_and_down(self):
		"""
		WITH VARIATION PROBLEMS
		You throw a ball vertically upward from the roof of a tall building.The ball leaves your hand at a point even with the roof railing 
		with an upward speed of 15.0 m/s; the ball is then in free fall. (We ignore air resistance.)
		
		On its way back down, it just misses the railing. Find:
		(a) The ball’s position and velocity 1.00 s and 4.00 s after leaving your hand;
		(b) The ball’s velocity when it is 5.00 m above the railing;
		(c) The maximum height reached;
		(d) The ball’s acceleration when it is at its maximum height.
		"""
		identify_and_setup = """
		IDENTIFY and SET UP The words “in free fall” mean that the acceleration is due to gravity, which is constant. 
		Our target variables are position [in parts (a) and (c)], velocity [in parts (a) and (b)], and acceleration [in part (d)].
		We take the origin at the point where the ball leaves your hand, and take the positive direction to be upward (Fig. 2.24). 
		The initial position y0 is zero, the initial y-velocity V0y is +15.0 m/s, and the y-acceleration is ay=−g=−9.80 m/s2. 
		In part (a), as in Example 2.6, we’ll use Eqs. (2.12) and (2.8) to find the position and velocity as functions of time. 
		In part (b) we must find the velocity at a given position (no time is given), so we’ll use Eq. (2.13).
		
		The ball actually moves straight up and then straight down; we show a U shaped path for clarity
		"""
		figure_description = """
		Figure 2.25 shows the y-t and υy-t graphs for the ball. 
		The y-t graph is a concave-down parabola that rises and then falls, 
		and the υy-t graph is a downward-sloping straight line. 
		Note that the ball’s velocity is zero when it is at its highest point.
		
		(a) Position and (b) velocity as functions of time for a ball thrown upward with an initial speed of 15.0 m/s.
		(a) y-t graph (curvature is downward because ay = −g is negative)
		Before t = 1.53 s the ball moves upward; after t = 1.53 s the ball moves downward
		(b) vy-t graph (straight line with negative slope because ay = −g is constant and negative)
		Before t = 1.53 s the y-velocity is positive; after t = 1.53 s the y-velocity is negative
		"""
		execute = """
		EXECUTE (a) The position and y-velocity at time t are given by Eqs. (2.12) and (2.8) with x’s replaced by y’s:

		y = y0 + V0yt + (1/2)Ayt^2 = y0 + V0yt + 1/2(-g)t^2

		When t=1.00 s, these equations give y = +10.1 m and Vy = +5.2 m/s.
		That is, the ball is 10.1 m above the origin (y is positive) and moving upward (Vy is positive) with a speed of 5.2 m/s.
		This is less than the initial speed because the ball slows as it ascends. When t=4.00 s, those equations give y = −18.4 m 
		and Vy = −24.2 m/s. The ball has passed its highest point and is 18.4 m below the origin (y is negative). It is moving 
		downward (υy is negative) with a speed of 24.2 m/s.

		(b) The y-velocity at any position y is given by Eq. (2.13) with x’s replaced by y’s:

		υy^2 = υ0y^2 + 2ay(y − y0) = υ0y^2 + 2(-g)(y − 0)

		When the ball is 5.00 m above the origin we have y = +5.00 m, so

		Vy^2 = V0y^2 + 2(-9.80 m/s^2)(5.00 m) = (15.0 m/s)^2 + 2(-9.80 m/s^2)(5.00 m) = 127 m^2/s^2 ± 11.3 m/s

		We get two values of υy because the ball passes through the point y = +5.00 m twice, once on the way up (so υy is positive) and 
		once on the way down (so υy is negative) (see Fig. 2.24). Note that the speed of the ball is 11.3 m/s each time it passes through 
		this point.

		(c) At the instant at which the ball reaches its maximum height y1, its y-velocity is momentarily zero: Vy = 0. We use Eq. (2.13) 
		to find y1. With Vy = 0, y0 = 0, and ay = −g, we get

		0 = V0y^2 + 2(-Ay)(y1 − 0)
		V0y^2 = 2*Ay*y1
		y1 = (υ0y^2)/(2g) = (15.0 m/s)^2/(2(9.80 m/s^2)) = +11.5 m

		(d) CAUTION A free-fall misconception: It’s a common misconception that at the highest point of free-fall motion, where the 
		velocity is zero, the acceleration is also zero. If this were so, once the ball reached the highest point it would hang there 
		suspended in midair! Remember that acceleration is the rate of change of velocity, and the ball’s velocity is continuously 
		changing. At every point, including the highest point, and at any velocity, including zero, the acceleration in free fall is always 
		ay = −g = −9.80 m/s^2.
		"""
		
		# Ask the user for inputs
		y0 = float(input("Enter the initial height (y0) in meters: "))
		V0y = float(input("Enter the initial vertical velocity (V0yt) in m/s: "))
		Ay_input = input("Enter the acceleration due to gravity (Ay) in m/s^2 or leave blank: ")
		if Ay_input.strip():  # Check if the input is not empty
			Ay = float(Ay_input)
		else:
			Ay = 9.8  # Default value

		# Ask the user for time values
		time_values = []  # Store the time values entered by the user

		while True:
			t = input("Enter a time in seconds (or 'q' to quit): ")
	
			if t.lower() == 'q':
				break  # Exit the loop if the user enters 'q'

			try:
				t = float(t)  # Try to convert input to float
				time_values.append(t)  # Add the time value to the list
			except ValueError:
				print("Invalid input. Please enter a valid number.")
			
		# Create a dataframe to store the results
		df = pd.DataFrame(columns=['time', 'position', 'y-velocity'])
		print()
		# Calculate, append, and present the results for each time
		for t in time_values:
			# Calculate the position and vertical velocity
			y = y0 + V0y * t + 0.5 * (-Ay) * t**2
			Vy = V0y + (-Ay) * t

			# Append the results to the dataframe with one decimal place precision
			df = pd.concat([df, pd.DataFrame({'time': [t], 'position': [round(y, 1)], 'y-velocity': [round(Vy, 1)]})], ignore_index=False)
			# Print the results with no decimal points
			print(f"At time t = {t} seconds:")
			print(f"Vertical position (y) = {y:.1f} meters")
			print(f"Vertical velocity (Vy) = {Vy:.1f} m/s")
			print()
		print(df)
		print()
		heights = []  # Store the heights entered by the user
		velocities = []  # Store the corresponding velocities
		
		#calculate velocity give user height
		while True:
			# Ask the user for the desired height (position)
			y = input("Enter a desired height (y) in meters (or 'q' to quit): ")
		
			if y.lower() == 'q':
				break  # Exit the loop if the user enters 'q'
		
			y = float(y)  # Convert input to float
			heights.append(y)  # Add the height value to the list

			# Calculate velocity using the formula Ay = g
			Vy_squared = V0y**2 + 2 * (-Ay) * (y - 0)
		
			# Take the square root to get the velocity
			Vy = round((Vy_squared)**0.5, 1)
			velocities.append(Vy)  # Add the velocity to the list
		# Create a DataFrame to store the results
		df = pd.DataFrame({'Position (y)': heights, 'Vertical Velocity (Vy)': velocities})

		# Print the results
		print("Results:")
		for i in range(len(heights)):
			print(f"At height y = {heights[i]} meters:")
			print(f"Vertical velocity (Vy) = {velocities[i]:.1f} m/s")
			print()
		# Print the DataFrame for the user to see
		print("\nResults:")
		print(df.to_string(index=False))
		print()
		misconception = """
		CAUTION A free-fall misconception:
		It’s a common misconception that at the highest point of free-fall motion, 
		where the velocity is zero, the acceleration is also zero. 
		If this were so, once the ball reached the highest point it would hang there suspended in midair! 
		Remember that acceleration is the rate of change of velocity, 
		and the ball’s velocity is continuously changing. 
		At every point, including the highest point, and at any velocity, 
		including zero, the acceleration in free fall is always ay=−g=−9.80 m/s^2.
		"""
		# Calculate the maximum height object traveled using the formula Ay = g
		y1 = (V0y**2) / (2 * (Ay))
		# Print the maximum height for the user to see
		print(f"The maximum height (y1) is: {y1:.1f} meters")
		print()
		key_concept = """
		If a freely falling object passes a given point at two different times, 
		once moving upward and once moving downward, its speed will be the same at both times.
		"""
		
		variation_problems = """
		WITH VARIATION PROBLEMS

		At what time after being released has the ball in Example 2.7 fallen 5.00 m below the roof railing?
		"""
		identify_and_setup = """
		IDENTIFY and SET UP We treat this as in Example 2.7, so y0, V0y, and ay=−g have the same values as there. 
		Now, however, the target variable is the time at which the ball is at y=−5.00 m.
		 The best equation to use is Eq. (2.12) with ay replaced by −g, which gives the position y as a function of time t:
		 
		 y=y0+V0y*t+12(−g)t2
		 This is a quadratic equation for t, which we want to solve for the value of t when y=−5.00 m.

		EXECUTE We rearrange the equation so that it has the standard form of a quadratic equation for an unknown x,
		 Ax2+Bx+C=0:

		(12g)t2+(−V0y)t+(y−y0)=At2+Bt+C=0
		By comparison, we identify A=12g, B=−V0y, and C=y−y0.
		 The quadratic formula (see Appendix B) tells us that this equation has two solutions:

		t===−B±B2−4AC/2A‾‾‾‾‾‾‾‾‾√−(−V0y)±(−V0y)^2−4((1/2)g)(y−y0)‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾√2((1/2)g)V0y±V0y2 −2g(y−y0)‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾√g
		Substituting the values y0=0,
		 V0y=+15.0 m/s,
		 g=9.80 m/s2,
		 and y=−5.00
		 m, we find

		t=(15.0 m/s)±(15.0 m/s)2−2(9.80 m/s2)(−5.00 m−0)‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾√9.80 m/s2
		You can confirm that the numerical answers are t=+3.36 s and t=−0.30 s.
		 The answer t=−0.30 s doesn’t make physical sense, since it refers to a time before the ball left your hand at t=0.
		 So the correct answer is t=+3.36 s.
		"""
		"""
		# List to store target positions (heights)
		target_positions = []

		# Ask the user to provide target positions (heights)
		while True:
			y = input("Enter the target position (y) in meters (or 'q' to quit): ")
			if y == 'q':
				break
			try:
				target_positions.append(float(y))
			except ValueError:
				print("Invalid input. Please enter a valid height.")
		"""

		# Calculate times for each target position and print the results
		for y in heights:
			discriminant = ((-V0y) ** 2) - 4 * (0.5 * Ay) * (y - y0)

			if discriminant < 0:
				print(f"No real solutions for time at height {y} meters.")
			else:
				t1 = (-(-V0y) - math.sqrt(discriminant)) / (2 * (0.5 * Ay))
				t2 = (-(-V0y) + math.sqrt(discriminant)) / (2 * (0.5 * Ay))
				times = [t1, t2]
				print(f"For height {y} meters:")
				for t in times:
					print(f"Time t = {t:.2f} seconds")
		print()
		print("By using one or more of the four equations in Table 2.5 with x")
		print("replaced by y,")
		print("the positive y-direction chosen to be upward, and acceleration ay=-g,")
		print("you can solve any free-fall problem.")
		print()
		evaluate_text = """
		EVALUATE Why did we get a second, fictitious solution? The explanation is that constant-acceleration equations like 
		Eq. (2.12) are based on the assumption that the acceleration is constant for all values of time, whether positive, negative, 
		or zero. Hence the solution t=−0.30 s refers to an imaginary moment when a freely falling ball was 5.00 m below the roof 
		railing and rising to meet your hand. Since the ball didn’t leave your hand and go into free fall until t=0, this result is pure fiction.

		Repeat these calculations to find the times when the ball is 5.00 m above the origin (y=+5.00 m). The two answers are t=+0.38 s 
		and t=+2.68 s. Both are positive values of t, and both refer to the real motion of the ball after leaving your hand. At the earlier time, 
		the ball passes through y=+5.00 m moving upward; at the later time, it passes through this point moving downward. 
		[Compare this with part (b) of Example 2.7, and again refer to Fig. 2.25a.]

		You should also solve for the times when y=+15.0 m. In this case, both solutions involve the square root of a negative number, 
		so there are no real solutions. Again Fig. 2.25a shows why; we found in part (c) of Example 2.7 that the ball’s maximum height is 
		y=+11.5 m, so it never reaches y=+15.0 m. While a quadratic equation such as Eq. (2.12) always has two solutions, in some 
		situations one or both of the solutions aren’t physically reasonable.

		In this example, we encountered a quadratic equation for the case of free fall. But Eq. (2.12) is a quadratic equation that applies to 
		all cases of straight-line motion with constant acceleration, so you’ll need to exercise the same care in solving many problems of 
		this kind.
		"""
		key_concept_text = """
		KEY CONCEPT
		When the acceleration of an object is constant, its position as a function of time is given by a quadratic equation. 
		Inspect the solutions to this equation to determine what they tell you about the problem you’re solving.
		"""
		
	def average_n_instant_velocity_3d(self):
		rover_exploration_problem = """
		A robotic vehicle, or rover, is exploring the surface of Mars. The stationary Mars lander is the origin of coordinates, and the 
		surrounding Martian surface lies in the xy plane. The rover, which we represent as a point, has x- and y-coordinate that vary 
		with time:
			x = 2.0 m - (0.25 m/s^2)* t^2
			y = (1.0 m/s)* t + (0.025 m/s^3)* t^3
		(a) Find the rover’s coordinates and distance from the lander at  t = 2.0 s (b) Find the rover’s displacement and average velocity 
		vectors for the interval t = 0.0 s to t = 2.0 s (c) Find a general expression for the rover’s instantaneous velocity vector . Express
		vector v at  t = 2.0 s in component form and in terms of magnitude and direction.
		"""
		identify_and_setup = """
		IDENTIFY and SET UP This problem involves motion in two dimensions, so we must use the vector equations obtained in this 
		section. Figure 3.5 shows the rover’s path (dashed line). We’ll use Eq. (3.1) for position r vector , the expression 
		change r vector = r vector2 - r vector 1 for displacement, Eq. (3.2) for average velocity, and Eqs. (3.5), (3.6), and (3.7) for 
		instantaneous velocity and its magnitude and direction. At  s the rover has position vector r0 and instantaneous velocity vector  V0
		Likewise,  r vector1 and v vector1 are the vectors at  t = 1.0 s; r vector2 and v vector2 are the vectors at  t = 2.0 s
		"""

		# User inputs
		meter_traveled_x = float(input("Enter constant of equation for x (2 m): "))
		acceleration_x = float(input("Enter acceleration for x (0.25 m/s^2): "))
		meter_traveled_y = float(input("Enter constant of equation for y (1 m): "))
		acceleration_y = float(input("Enter acceleration for y (0.025 m/s^2): "))

		# Ask the user to enter the first time value
		time1 = float(input("Enter time 1 (in seconds): "))
		# Ask the user to enter the second time value
		time2 = float(input("Enter time 2 (in seconds): "))

		# Calculate x and y coordinates at time 1 and time 2
		x_coordinate_1 = meter_traveled_x - (acceleration_x) * time1 ** 2
		y_coordinate_1 = meter_traveled_y - (acceleration_y) * time1 ** 2
		x_coordinate_2 = meter_traveled_x - (acceleration_x) * time2 ** 2
		y_coordinate_2 = meter_traveled_y - (acceleration_y) * time2 ** 2

		# Calculate the position vector 'r' using the given formulas
		x_1 = 2.0 - (0.25 * time1 ** 2)
		y_1 = (1.0 * time1) + (0.025 * time1 ** 3)
		x_2 = 2.0 - (0.25 * time2 ** 2)
		y_2 = (1.0 * time2) + (0.025 * time2 ** 3)

		# Calculate distance from the origin for time 1 and time 2
		distance_origin_1 = math.sqrt(x_coordinate_1 ** 2 + y_coordinate_1 ** 2)
		distance_origin_2 = math.sqrt(x_coordinate_2 ** 2 + y_coordinate_2 ** 2)

		# Calculate displacement as change in r in 2D
		displacement_x = x_2 - x_1
		displacement_y = y_2 - y_1
		
		# Calculate average velocity components
		V_av_x = (x_2 - x_1) / (time2 - time1)
		V_av_y = (y_2 - y_1) / (time2 - time1)
		
		# Calculate instantaneous velocity components at time 1
		Vx = -0.25 * time2 *2
		Vy = 1 + 0.025 * 3 * time2 ** 2
		
		# Calculate the speed (magnitude of velocity) at time 1
		speed = math.sqrt(Vx ** 2 + Vy ** 2)
		# Calculate the angle of the vector
		angle = math.degrees(math.atan(Vy / Vx))
		# If the angle is negative, adjust it
		if angle < 0:
			angle += 180
		

		# Print the results
		print(f"At time t = {time2} seconds, the position vector (x, y) is ({x_2:.2f} m, {y_2:.2f} m).")
		print(f"Distance from the origin at time 1 t = {time1}: {distance_origin_1:.2f} meters")
		print(f"Distance from the origin at time 2 t = {time2}: {distance_origin_2:.2f} meters")
		print(f"At time t = {time1} seconds, the position vector (x, y) is ({x_1:.2f}i^ m, {y_1:.2f}j^ m).")
		print(f"At time t = {time2} seconds, the position vector (x, y) is ({x_2:.2f}i^ m, {y_2:.2f}j^ m).")
		print(f"Displacement (change in r) is ({displacement_x:.2f} m, {displacement_y:.2f} m).")
		print(f"Average velocity components are V_av =  {V_av_x:.2f}i^ m/s,  {V_av_y:.2f}j^ m/s.")
		print(f"Instantaneous velocity components at time t = {time1} seconds: Vx  = {Vx:.2f} and Vy {Vy:.2f} m/s")
		print(f"Speed at time t = {time2} seconds: {speed:.0f} m/s")
		print(f"Angle of the vector at time t = {time2} seconds: {angle:.0f} degrees")
		# If the angle is greater than 90 degrees, adjust it
		if angle > 90:
			angle -= 90
			print(f"North western Angle of the vector at time t = {time2} seconds: {angle:.0f} degrees")

		
		execute = """
		EXECUTE (a) At t = 2.0 s, the rover’s coordinates are:
		x = 2.0 m - (0.25 m/s^2)* (2.0 s)^2 = 1.0 m (east)
		y = (1.0 m/s)* (2.0 s) + (0.025 m/s^3)* (2.0 s)^3 = 2.2 m (north)

		The rover’s distance from the origin at this time is:
		r = sqrt(x^2 + y^2) = sqrt((1.0 m)^2 + (2.2)^2) = 2.4 m

		(b) To find the displacement and average velocity over the given time interval, we first express the position vector r as a function 
		of time t. From Eq. (3.1) this is:
		r vector = x i^ + y j^
		= [2.0 m - (0.25 m/s^2)* t^2] i^ + [(1.0 m/s)* t + (0.025 m/s^3)* t^3] j^

		At t = 0 s, the position vector r0 is:
		r(0) = [2.0 m] i^ + [(0.0 m] j^

		From part (a), the position vector r2 at t = 2.0 s is:
		r(2 s) = [1.0 m] i^ + [(2.2 m] j^

		The displacement from t = 0 s to t = 2.0 s is therefore:
		Δr = r(2.0 s) - r(0) = [1.0 m] i^ + [2.2 m] j^ -  [2.0 m] i^ + [0.0 m] j^ [2.0 m] i^ + [0.0 m] j^
		=[-1.0 m] i^ + [2.2 m] j^

		During this interval, the rover moves 1.0 m in the negative x-direction and 2.2 m in the positive y-direction. 
		From Eq. (3.2), the average velocity over this interval is the displacement divided by the elapsed time:
		v_avg = Δr / Δt   =( [-1.0 m] i^ + [2.2 m] j^) / (2. 0 s - 0.0 s)
		=  [-0.50 m/s] i^ + [1.1 m/s] j^

		The components of this average velocity are:
		v_avg_x = 0.50 m/s 
		v_avg_y = 1.1 m/s 

		(c) From Eq. (3.4), the components of instantaneous velocity are the time derivatives of the coordinates:
		v_x = dr_x / dt = (-0.25 m/s^2) (2t)
		v_y = dr_y / dt = (1.0 m/s^2) + (0.025 m/s^3) *(3 * t^2)

		Hence the instantaneous velocity vector is:
		v = v_x i^ + v_y j^ = (-0.50 m/s^2)*t *i^  + [1.0 m/s + (0.075 m/s^3)*t^2]j^

		At t = 2.0 s, the velocity vector V2 has components:
		V2x = (-0.50 m/s^2)(2.0 s)  = -1.0 m/s
		V2y = 1.0 m/s + (0.075 m/s^3)(2.0 s)^2 = 1.3 m/s

		The magnitude of the instantaneous velocity (that is, the speed) at t = 2.0 s is:
		|V2| = sqrt(V2x^2 + V2y^2) = sqrt((-1.0 m/s)^2 + (1.3  m/s)^2) = 1.6 m/s

		Figure 3.5 shows the direction of velocity vector v, which is at an angle θ between the positive x-axis and v with respect to 
		the positive x-direction. From Eq. (3.7) we have:
		tan(θ) = v_y / v_x
		tan(θ) = (1.3  m/s) / (-1.0 m/s) = arctan(-3.2)
		θ = 52 degree

		This is off by 180 degrees; the correct value is theta = 180 - 52 = 128 degree
		or θ = 38 degrees west of north.
		"""
		evaluation = """
		EVALUATE Compare the components of average velocity from part (b) for the interval from  to  with the components of 
		instantaneous velocity at  from part (c)  Just as in one dimension, the average velocity vector  over an interval is in general 
		not equal to the instantaneous velocity  at the end of the interval (see Example 2.1).
		Figure 3.5 shows the position vectors  and instantaneous velocity vectors  at  1.0 s, and 2.0 s. (Calculate these quantities 
		for  and ) Notice that  is tangent to the path at every point. The magnitude of  increases as the rover moves, which means 
		that its speed is increasing.
		"""
		key_concept = """
		KEY CONCEPT
		To calculate the average velocity vector of an object, first find its displacement vector during a time interval. 
		Then divide by the time interval. To calculate the object’s instantaneous velocity vector (its average velocity 
		vector over an infinitesimally short time interval), take the derivative of its position vector with respect to time.
		"""

		# Print the key concept
		print(key_concept)
		
	
	def acceleration_explained_3d_explanation(self):
		# Variable describing acceleration in three dimensions
		acceleration_description = """Now let’s consider the acceleration of a particle moving in space. Just as for motion in a straight line, 
		acceleration describes how the velocity of the particle changes. But since we now treat velocity as a vector, acceleration will 
		describe changes in the velocity magnitude (that is, the speed) and changes in the direction of velocity (that is, the direction in 
		which the particle is moving)."""
		
		# change in velocity and change in time gives you acceleration
		t2 = 2
		t1 = 0
		V_final = 20
		V_initial = 0
		time_interval = t2 - t1
		#average acceleration between  and p1 and p2
		average_acceleration = (V_final - V_initial) / time_interval
		statements = """
		During the time interval from t1 to t2, the vector change in velocity is ΔV, so (Fig. 3.6b).
		The average acceleration A_avg of the car during this time interval is the velocity change ΔV divided by the time interval Δt.
		To find the car's average acceleration between p1 and p2, we first find the change in velocity V by subtracting v 1 and v2. 
		The average acceleration has the same direction as the change in velocity V
		As in Chapter 2, we define the instantaneous acceleration  (a vector quantity) at point  as the limit of the average 
		acceleration vector when point p2 approaches point p1, so both  v and t approach zero (Fig. 3.7):
		Acceleration points  to the concave side of path; only if the trajectory is a straight line is the acceleration tangent to the 
		trajectory
		"""
		curved_path_acceleration = """
		The velocity vector v is always tangent to the particle’s path, but the instantaneous acceleration vector a does not have to be 
		tangent to the path. If the path is curved, a points toward the concave side of the path—that is, toward the inside of any turn that 
		the particle is making (Fig. 3.7a). The acceleration is tangent to the path only if the particle moves in a straight line (Fig. 3.7b).
		"""
		caution_curved_path_acceleration = """
		CAUTION: Any particle following a curved path is accelerating. When a particle is moving in a curved path, it always has 
		nonzero acceleration, even when it moves with constant speed. This conclusion is contrary to the everyday use of the word 
		“acceleration” to mean that speed is increasing. The more precise definition given in Eq. (3.9) shows that there is a nonzero 
		acceleration whenever the velocity vector changes in any way, whether there is a change of speed, direction, or both.
		
		To convince yourself that a particle is accelerating as it moves on a curved path with constant speed, think of your sensations 
		when you ride in a car. When the car accelerates, you tend to move inside the car in a direction opposite to the car’s 
		acceleration. (In Chapter 4 we’ll learn why this is so.) Thus you tend to slide toward the back of the car when it accelerates 
		forward (speeds up) and toward the front of the car when it accelerates backward (slows down). If the car makes a turn on a 
		level road, you tend to slide toward the outside of the turn; hence the car is accelerating toward the inside of the turn.
		
		We’ll usually be interested in instantaneous acceleration, not average acceleration. From now on, we’ll use the term 
		“acceleration” to mean the instantaneous acceleration vector 
		"""
		
	def average_n_instant_velocity_3d(self):
		problem = """
		Let’s return to the motions of the Mars rover in Example 3.1. 
		(a) Find the components of the average acceleration for the interval Δt from t1 to t2. 
		(b) Find the instantaneous acceleration at t2.
		"""
		identify_and_setup = """
		IDENTIFY and SET UP In Example 3.1 we found the components of the rover’s instantaneous velocity at any time :
			Vx = dx / dt = (-0.25 m/s^2)(2 * t) = (-0.50 m/s^2)* t
			Vy = dy / dt = 1.0 m/s + (0.025 m/s^3)(3 * t^2) = 1.0 m/s + (0.075 m/s^3)* t^2
		
		We’ll use the vector relationships among velocity, average acceleration, and instantaneous acceleration. In part (a) we 
		determine the values of  Vx and Vy at the beginning and end of the interval and then use Eq. (3.8) to calculate the components 
		of the average acceleration. In part (b) we obtain expressions for the instantaneous acceleration components at any time  
		by taking the time derivatives of the velocity components as in Eqs. (3.10).
		"""
		execute = """
		EXECUTE (a) In Example 3.1 we found that at t = 0.0 s the velocity components are
		Vx1 = 0.0 m/s
		Vy1 = 1.0 m/s

		and that at t = 2.0 s the components are
		Vx2 = -1.0 m/s
		Vy2 = 1.3 m/s

		Thus the components of average acceleration in the interval t = 0.0 s to t = 2.0 are
		A_avg_x = change Vx / change t
		= (-1.0 m/s - 0.0 m/s) / (2.0 s - 0.0 s)
		= -0.50 m/s^2
		
		A_avg_y = change Vy / change t
		= (1.3 m/s - 1.0 m/s) / (2.0 - 0.0 s) 
		= 0.15 m/s^2
		

		(b) Using Eqs. (3.10), we find
		A_inst_x = dVx / change t 
		= -0.50 m/s^2
		
		A_inst_y = dVy / change t
		= (-.075 m/s^3)* 2* t

		Hence the instantaneous acceleration vector A at time t is
		A = ax i^ + ay j^ 
		= (-0.50 m/s^2)i^ + (0.15 m/s^3)*tj^

		At t = 2.0 s, the components of acceleration and the acceleration vector are
		ax = -0.50 m/s^2 
		ay = (0.15 m/s^3)* (2.0 s) = 0.30 m/s^2
		vector_a = (-0.50 m/s^2)i^ + ( 0.30 m/s^2)j^

		The magnitude of acceleration at this time is
		A_mag1 = sqrt(ax^2 + ay^2)
		= sqrt((-0.50 m/s^2)^2 + ( 0.30 m/s^2)^2) = 0.58 m/s^2

		A sketch of this vector (Fig. 3.9) shows that the direction angle theta of A with respect to the positive x-axis is between 0 and 
		90 degrees and 180 degree. From Eq. (3.7) we have 
		
		theta = arctan(A_inst_y / A_inst_x) 
		= arctan(( 0.30 m/s^2) / (-0.50 m/s^2)) = -31 degrees

		Hence theta =  180 degree + (-31 degrees) = 149 degree

		The path of the robotic rover, showing the velocity and acceleration at t = 0.0 s ( V0 and A0) and t = 1.0 s,
		(V1 and A1)  and t = 2.0 s (V2 and A2)
		"""
		execute = """EVALUATE
		Figure 3.9 shows the rover’s path and the velocity and acceleration vectors at 1.0 s, and 2.0 s. 
		(Use the results of part (b) to calculate the instantaneous acceleration at and for yourself.) Note that v and a are not in the 
		same direction at any of these times. The velocity vector v is tangent to the path at each point (as is always the case), and 
		the acceleration vector a points toward the concave side of the path.
		"""
		key_concept = """
		To calculate the average acceleration vector of an object, first find the change in its velocity vector (final velocity minus 
		initial velocity) during a time interval. Then divide by the time interval. 
		
		To calculate the object’s instantaneous acceleration vector (its average velocity vector over an infinitesimally short time interval),
		take the derivative of its velocity vector with respect to time.
		"""
		# Ask the user to enter the first time value
		time1 = float(input("Enter time 1 (in seconds): "))
		# Ask the user to enter the second time value
		time2 = float(input("Enter time 2 (in seconds): "))
		
		# Calculate instantaneous velocity components at time 1
		Vx1 = -0.25 * time1 *2
		Vy1 = 1 + 0.025 * 3 * time1 ** 2
		# Calculate instantaneous velocity components at time 2
		Vx2 = -0.25 * time2 *2
		Vy2 = 1 + 0.025 * 3 * time2 ** 2
		
		#calculate change in velocity on the x and y direction
		change_Vx = Vx2 - Vx1
		change_Vy = Vy2 - Vy1
		time_interval = time2 - time1
		
		#calculate average acceleration in the x and y direciton in the interval user specifies t = 0 to t = 1
		A_av_x = change_Vx / time_interval
		A_av_y = change_Vy / time_interval
		
		# Calculate instantaneous Acceleration components at time 1
		Ax = -0.25  *2
		Ay = 0.025 * 3 * time2 * 2
		
		#calculate the magnitude of acceleration at his time is
		a = math.sqrt(Ax**2 + Ay**2)
		
		# Calculate the angle of the vector
		angle = math.degrees(math.atan(Ay / Ax))
		# If the angle is negative, adjust it
		if angle < 0:
			angle += 180
		

		print(f"Instantaneous velocity components at time t = {time1} seconds: Vx  = {Vx1:.2f} and Vy {Vy1:.2f} m/s")
		print(f"Instantaneous velocity components at time t = {time2} seconds: Vx  = {Vx2:.2f} and Vy {Vy2:.2f} m/s")
		print(f"Average acceleration (A_av)(x, y) direction is ({A_av_x:.2f} m/s^2, {A_av_y:.2f} m/s^2).")
		print(f"Instantaneous acceleration components at time t = {time2} seconds: Ax  = {Ax:.2f} m/s^2 and Ay {Ay:.2f} m/s^3")
		print(f"Instantaneous acceleration vector A at time t = {time2} seconds: a arrow  = ({Ax:.2f}m/s^2 )i^ and Ay ({Ay:.2f}m/s^3)j^")
		print(f"Magnitude of acceleration (|a|) is {a:.2f} m/s^2.")
		print(f"Angle of the vector at time t = {time2} seconds: {angle:.0f} degrees")
		# If the angle is greater than 90 degrees, adjust it
		if angle > 90:
			angle -= 90
			print(f"North western Angle of the vector at time t = {time2} seconds: {angle:.0f} degrees")
			
	def parallel_n_perpendicular_acceleration_explanation(self):
		parrallel_perpendicular_acceleration = """
		That’s because the parallel component A∥ tells us about changes in the particle’s speed, 
		while the perpendicular component A⊥ tells us about changes in the particle’s direction of motion.
		"""
		parallel_acceleration_velocity = """
		Changes only magnitude of velocity: speed changes; direction doesn't"""
		perpendicular_acceleration_velocity = """
		Changes only direction of velocity: particle follows curved path at constant speed."""
		
		constant_increasing_decreasing_acceleration = """
		constant speed, increasing speed, and decreasing speed. If the speed is constant, vector A is perpendicular, or normal, to the 
		path and to  Vx and points toward the concave side of the path (Fig. 3.12a). If the speed is increasing, there is still a 
		perpendicular component of vector A , but there is also a parallel component with the same direction as vector Vx (Fig. 3.12b). 
		Then vector A points ahead of the normal to the path. (This was the case in Example 3.2.) If the speed is decreasing, the parallel 
		component has the direction opposite to vector Vx , and  Vector A points behind the normal to the path.
		"""
		
	def parallel_n_perpendicular_acceleration(self):
		problem = """
		For the rover of Examples 3.1 and 3.2, find the parallel and perpendicular components of the acceleration at t = 2.0 s.
		"""
		identify_and_setup = """
		IDENTIFY and SET UP We want to find the components of the acceleration vector a that are parallel and perpendicular 
		to the velocity vector v. We found the directions of a_parallel and a_perpendicular in Examples 3.1 and 3.2, respectively; 
		Fig. 3.9 shows the results. From these directions, we can find the angle between the two vectors and the components of a 
		with respect to the direction of v.
		"""
		# Ask the user to enter the angle between acceleration and velocity vectors
		while True:
			angle_degrees = float(input("Enter the angle between acceleration and velocity vectors (in degrees): "))
	
			if angle_degrees >= 0:
				break
			else:
				print("Please enter a positive angle.")

		# Ask the user to enter the magnitude of acceleration (a)
		a = float(input("Enter the magnitude of acceleration (a): "))

		# Convert the angle from degrees to radians
		angle_radians = math.radians(angle_degrees)

		# Calculate the perpendicular and parallel components of acceleration
		a_perpendicular = a * math.sin(angle_radians)
		a_parallel = a * math.cos(angle_radians)

		# Print the results for the user to see
		print(f"Perpendicular component of acceleration (a_perpendicular (a_Tbar)): {a_perpendicular:.2f}")
		print(f"Parallel component of acceleration (a_parallel (a_bar)): {a_parallel:.2f}")


		execute = """
		EXECUTE From Example 3.2, at t = 2.0 s, the particle has an acceleration of magnitude 0.58 m/s^2 at an angle of 149 degrees 
		with respect to the positive x-direction. In Example 3.1 we found that at this time the velocity vector is at an angle of 128 
		degrees with respect to the positive x-direction. The angle between acceleration (A) and velocity (V) is therefore 
		149 degrees - 128 degree = 21 degree 
		(Fig. 3.13). Hence the components of acceleration parallel and perpendicular to velocity are
		a bar = a cos21 degree = (0.58 m/s^2) cos21 degree = 0.54 m/s^2
		a t_bar = a sin 21 degree = (0.58 m/s^2) sin 21 degree = 0.21 m/s^2

		A_parallel = A * cos(30 degrees)
		A_perpendicular = A * sin(30 degrees)
		"""
		evaluate = """
		EVALUATE The parallel component (Ax) is positive (in the same direction as Vx), which means that the speed is increasing 
		at this instant. The value of Ax tells us that the speed is increasing at this instant at a rate of dVx / dt per second. 
		The perpendicular component (Ay) is not zero, which means that at this instant the rover is turning—that is, it is changing 
		direction and following a curved path.
		"""
		key_concept = """
		KEY CONCEPT
		If an object’s speed is changing, there is a component of its acceleration vector parallel to its velocity vector. 
		If an object’s direction of motion is changing—that is, it is turning—there is a component of its acceleration 
		vector perpendicular to its velocity vector and toward the inside of the turn.
		"""
		problem2 = """
		A skier moves along a ski-jump ramp (Fig. 3.14a). The ramp is straight from point A to point B and curved from point B 
		onward. The skier speeds up as she moves downhill from point A to point B, where her speed is maximum. She slows 
		down after passing point B. Draw the direction of the acceleration vector at each of the points A, B, C, and D.
		"""
		solution = """
		SOLUTION Figure 3.14b shows our solution. At point A, the skier is moving in a straight line with increasing speed, so her 
		acceleration points downhill, in the same direction as her velocity. At points B, C, and D, the skier is moving along a curved 
		path, so her acceleration has a component perpendicular to the path (toward the concave side of the path) at each of these 
		points. At point E, there is also an acceleration component in the direction of her motion because she is speeding up. 
		So the acceleration vector points ahead of the normal to her path at point E. At point F, the skier’s speed is 
		instantaneously not changing; her speed is maximum at this point, so its derivative is zero. There is therefore no 
		parallel component of the acceleration, and the acceleration is perpendicular to her motion. At point G, there is an 
		acceleration component opposite to the direction of her motion because she’s slowing down. The acceleration vector 
		therefore points behind the normal to her path.
		"""
		key_concept = """
		KEY CONCEPT: If a moving object is turning (changing direction), its acceleration vector points ahead of the normal to its 
		path if it is speeding up, behind the normal if it is slowing down, and along the normal if its speed is instantaneously not 
		changing.
		"""
		
	def projectile_acceleration_no_air_resistance_explained(self):
		problem3 = """
		PROBLEM 3
		Let’s consider again the skier in Conceptual Example 3.4. What is her acceleration at each of the points A, B, and C in 
		Fig. 3.21a after she flies off the ramp? Neglect air resistance.
		"""
		solution = """
		SOLUTION
		Figure 3.21b shows our answer. The skier’s acceleration changed from point to point while she was on the ramp. 
		But as soon as she leaves the ramp, she becomes a projectile. So at points A, B, and C, and indeed at all points 
		after she leaves the ramp, the skier’s acceleration points vertically downward and has magnitude g.
		"""
		key_concept = """
		KEY CONCEPT
		No matter how complicated the acceleration of a particle before it becomes a projectile, its acceleration as a projectile is given 
		by g, directed downward, and has a magnitude of 9.8 m/s^2 near Earth’s surface.
		"""
		identify = """
		IDENTIFY the relevant concepts: The key concept is that throughout projectile motion, the acceleration is downward and 
		has a constant magnitude g. Projectile-motion equations don’t apply to throwing a ball, because during the throw 
		the ball is acted on by both the thrower’s hand and gravity. These equations apply only after the ball leaves the thrower’s hand.
		"""
		setup = """
		SET UP the problem using the following steps:
		1. Define your coordinate system and make a sketch showing your axes. It’s almost always best to make the x-axis 
		horizontal and the y-axis vertical, and to choose the origin to be where the object first becomes a projectile 
		(for example, where a ball leaves the thrower’s hand). Then the components of acceleration are ax and ay, as in 
		Eq. (3.13); the initial position is (x0, y0) and you can use Eqs. (3.19) through (3.22). (If you choose a different origin 
		or axes, you’ll have to modify these equations.)

		2. List the unknown and known quantities, and decide which unknowns are your target variables. For example, you 
		might be given the initial velocity (either the components or the magnitude and direction) and asked to find the 
		coordinates and velocity components at some later time. Make sure that you have as many equations as there 
		are target variables to be found. In addition to Eqs. (3.19) through (3.22), Eqs. (3.23), (3.24), (3.25), and (3.26) may be useful.

		3. State the problem in words and then translate those words into symbols. For example, when does the particle arrive 
		at a certain point? (That is, at what value of t?) Where is the particle when its velocity has a certain value? (That is, what 
		are the values of x and y when vx or vy has the specified value?) Since vy = 0 at the highest point in a trajectory, the 
		question “When does the projectile reach its highest point?” translates into “What is the value of t when vy = 0?” Similarly, 
		“When does the projectile return to its initial elevation?” translates into “What is the value of t when y = y0?”
		"""
		execute = """
		EXECUTE the solution: Find the target variables using the equations you chose. Resist the temptation to break the trajectory 
		into segments and analyze each segment separately. You don’t have to start all over when the projectile reaches its 
		highest point! It’s almost always easier to use the same axes and time scale throughout the problem. If you need 
		numerical values, use g = 9.8 m/s². Remember that g is positive!
		"""
	

	def batted_baseball_problem(self):
		batted_baseball = """
		WITH VARIATION PROBLEMS
		A batter hits a baseball so that it leaves the bat at speed V at an angle θ. 
		(a) Find the position of the ball and its velocity (magnitude and direction) at time t.
		(b) Find the time when the ball reaches the highest point of its flight, and its height at this time.
		(c) Find the horizontal range R—that is, the horizontal distance from the starting point to 
		where the ball hits the ground—and the ball’s velocity just before it hits.
		"""
		identify_and_set_up_description = """
		IDENTIFY and SET UP As Fig. 3.20 shows, air resistance strongly affects the 
		motion of a baseball. For simplicity, however, we’ll ignore air resistance here 
		and use the projectile-motion equations to describe the motion. The ball 
		leaves the bat at a meter or so above ground level, but we’ll ignore this distance 
		and assume that it starts at ground level. Figure 3.23 shows our sketch of the 
		ball’s trajectory. We’ll use the same coordinate system as in Figs. 3.17 and 3.18, 
		so we can use Eqs. (3.19) through (3.22). Our target variables are 
		(a) the position and velocity of the ball 2.00 s after it leaves the bat, 
		(b) the time when the ball is at its maximum height, that is, when Vy = 0, and 
		the height at this time, and 
		(c) the time when the ball returns to ground level, and the ball’s vertical 
		component of velocity then.
		"""
		execute_a = """
		(a) We want to find the position (x, y), the magnitude of velocity V, and the angle θ at t = 2.00 s. The initial velocity of the ball has components V0x = 18.0 m/s and V0y = 24.0 m/s.

		From Eqs. (3.19) through (3.22):
		x = V0x * t
		y = V0y * t - (1/2) * g * t^2

		The magnitude of velocity is positive at t = 2.00 s, so the ball is still moving upward (Fig. 3.23). From Eqs. (3.24) and (3.25):
		V = sqrt(V0x^2 + V0y^2)
		θ = arctan(V0y / V0x)

		The ball is moving at 24.4 m/s in a direction 59.04 degrees above the horizontal.
		"""

		execute_b = """
		(b) At the highest point, the vertical velocity Vy is zero. Call the time when this happens t_max; then:
		Vy = V0y - g * t_max = 0

		Solving for t_max:
		t_max = V0y / g

		The height h at the highest point is the value of y at time t_max:
		h = V0y * t_max - (1/2) * g * t_max^2
		"""

		execute_c = """
		(c) We’ll find the horizontal range in two steps. First, we find the time t_ground when y = 0 (the ball is at ground level):
		0 = V0y * t_ground - (1/2) * g * t_ground^2

		This is a quadratic equation for t_ground. It has two roots:
		t_ground1 = 0 (at the initial position)
		t_ground2 = (2 * V0y) / g

		The ball is at y = 0 at both times. The ball leaves the ground at t_ground1 = 0, and it hits the ground at t_ground2.

		The horizontal range R is the value of x at time t_ground2:
		R = V0x * t_ground2

		The vertical component of velocity when the ball hits the ground is -V0y, which means it has the same magnitude as the initial vertical velocity V0y but the opposite direction (down). Since tan(θ) = V0y / V0x is constant, the angle θ at this point is the negative of the initial angle θ.
		"""

		# Initial values
		g = 9.8  # m/s^2
		# Given initial velocity V0 and launch angle θ 
		# Get user input
		# Get user input
		V0 = input("Enter the initial velocity (m/s): ")
		θ = input("Enter the launch angle (degrees): ")
		t = input("Enter the time (seconds): ")

		# Initialize with default values if user input is empty
		if V0 == "":
			V0 = 37.0
		else:
			V0 = float(V0)
		# Direction of the velocity vector at time t
		if θ == "":
			# Convert degrees to radians
			θ = math.radians( 53.1)
		else:
			θ = float(θ)
			# Convert degrees to radians
			θ = math.radians(θ)

		if t == "":
			t = 2.0
		else:
			t = float(t)
		
		#describe velocity of the projectile
		# Initial Velocity variables Calculate V0x and V0y
		V0x = V0 * math.cos(θ) # Velocity of the ball in the x-direction at time t
		V0y = V0 * math.sin(θ) # Velocity of the ball in the y-direction at time t
		
		# (a) Find the position of the ball and its velocity at time t
		# Position variables
		# Calculate the x and y coordinates
		#describe the position of the projectile in Fig. 3.17 at any time t
		x = V0x * t
		y = V0y * t - 0.5 * g * t**2
		
		# Calculate the velocity of the ball 2 seconds after it was hit
		Vx = V0x
		Vy = V0y - (g * t)
		if Vy > 0:
			print()
			print(f"The y-component of velocity is positive at t={t} seconds, so the ball is still moving upward.")
		else:
			print()
			print(f"The y-component of velocity is positive at t={t} seconds, so the ball is moving downward.")


		# Calculate the magnitude of velocity
		velocity = math.sqrt(Vx**2 + Vy**2)
		# Calculate the angle of velocity
		angle_degrees = math.degrees(math.atan2(Vy, Vx))

		# (b) Find the time when the ball reaches the highest point and its height at this time
		# Calculate the time at the highest point (t1)
		t1 = V0y / g

		# Calculate the height at the highest point (h)
		h = V0y * t1 - (1/2) * g * t1**2

		# (c) Find the horizontal range R and the ball’s velocity just before it hits
		# Calculate the time when the ball is at ground level (t2)
		t2 = (2 * V0y) / g
		# Calculate the horizontal range (R)
		R = V0x * t2
		# Calculate the vertical component of velocity when the ball hits the ground (Vy)
		Vy_ground = V0y - g * t2
		
		
		print()
		print("(a) Find the position of the ball and its velocity (magnitude and direction) at time.")
		print(f"t = {t} seconds,")
		print(f"Initial horizontal velocity (V0x) = {V0x:.1f} m/s")
		print(f"Initial vertical velocity (V0y) = {V0y:.1f} m/s")
		print(f"x-coordinate (x) = {x:.1f} meters")
		print(f"y-coordinate (y) = {y:.1f} meters")
		print(f"Velocity in the x-direction (Vx) = {Vx:.1f} m/s")
		print(f"Velocity in the y-direction (Vy) = {Vy:.1f} m/s")
		print(f"Magnitude of velocity = {velocity:.1f} m/s")
		print(f"Angle of velocity = {angle_degrees:.1f} degrees")
		print()
		print("(b) Find the time when the ball reaches the highest point of its flight, and its height at this time.")
		print(f"Time at the highest point (t1) = {t1:.2f} seconds")
		print(f"Height at the highest point (h) = {h:.1f} meters")
		print()
		print("(c) Find the horizontal range R—that is, the horizontal distance from the starting point to")
		print("    where the ball hits the ground—and the ball’s velocity just before it hits.")
		print(f"Time when the ball is at ground level (t2) = {t2:.2f} seconds")
		print(f"Horizontal range (R) = {R:.0f} meters")
		print(f"Vertical component of velocity when the ball hits the ground (Vy) = {Vy_ground:.1f} m/s")
		

	def projected_horizontally_problem(self):
		projected_horizontally = """
		WITH VARIATION PROBLEMS
		A motorcycle stunt rider rides off the edge of a cliff. Just at the edge his velocity is horizontal, with magnitude  9.0 m/s
		Find the motorcycle’s position, distance from the edge of the cliff, and velocity 0.50 s after it leaves the edge 
		of the cliff. Ignore air resistance.
		"""
		identify_setup = """
		IDENTIFY and SET UP
		Figure 3.22 shows our sketch of the trajectory of the motorcycle and rider. The rider is in projectile motion as soon as he 
		leaves the edge of the cliff, which we take to be the origin (so x0 = 0 and y0 = 0). His initial velocity V0 at the edge of 
		the cliff is horizontal, which means V0x = V0 and V0y = 0, so its components are V0x and V0y.

		To find the motorcycle’s position at time t, we use Eqs. (3.19) and (3.20); we then find the distance from the origin 
		using Eq. (3.23). Finally, we use Eqs. (3.21) and (3.22) to find the velocity components at time t.
		"""
		# Ask the user to enter the initial velocity (V0) and time (t)
		V0x = float(input("Enter the initial velocity (m/s): "))
		time = float(input("Enter the time elapsed after leaving the edge of the cliff (s): "))

		# Constants
		g = 9.8  # Acceleration due to gravity in m/s^2

		# Calculate the x and y coordinates
		x = V0x * time
		y = -(1/2) * g * time**2

		# Print the motorcycle’s position
		print(f"The motorcycle's position at time t = {time} seconds is:")
		print(f"x = {x:.1f} meters")
		print(f"y = {y:.1f} meters")

		# Calculate the motorcycle’s distance from the origin (edge of the cliff)
		distance_from_origin = math.sqrt(x**2 + y**2)
		print(f"The motorcycle's distance from the edge of the cliff is {distance_from_origin:.1f} meters")

		# Calculate the x and y velocities
		Vx = V0x
		Vy = -g * time

		# Print the velocity vector
		print(f"The motorcycle's velocity vector at time t = {time} seconds is:")
		print(f"Vx = {Vx:.2f} m/s i^")
		print(f"Vy = {Vy:.2f} m/s j^")

		# Calculate the magnitude of the velocity
		V = math.sqrt(Vx**2 + Vy**2)
		print(f"The magnitude of the velocity is {V:.1f} m/s")

		# Calculate the angle θ
		theta = math.atan(Vy / Vx)
		print(f"The angle θ is {math.degrees(theta):.0f} degrees")

		execute = """
		EXECUTE From Eqs. (3.19) and (3.20), the motorcycle’s position components at t = 0.50 s are

		x = V0x * t = (9.0 m/s) * (0.50 s)
		y = -(1/2)*g*t^2 = -(1/2)*(9.80 m/s^2)* (0.50 s)^2 = -1.2

		The negative value of y shows that the motorcycle is below its starting point.
		From Eq. (3.23), the motorcycle’s distance from the origin at t = 0.50 s is

		r = math.sqrt(x^2  + y^2) = math.sqrt(4.5^2 m + (-1.2m)^2) = 4.7 m

		From Eqs. (3.21) and (3.22), the velocity components at t = 0.50 s are

		Vx =  V0x = 9.0 m/s
		Vy = -g * t = (-9.80 m/s^2)*(0.50 s) = -4.9 m/s

		The motorcycle has the same horizontal velocity Vx as when it left the cliff at t = 0, but in addition, there is a 
		downward (negative) vertical velocity Vy. The velocity vector at t = 0.50 s is

		V = Vx i^  + Vx j^ = (9.0 m/s)i^ + (-4.9 m/s)j^

		From Eqs. (3.24) and (3.25), at t = 0.50 s, the velocity has a magnitude of V and an angle θ given by
		V = math.sqrt(Vx^2 + Vy^2) = math.sqrt((9.0 m/s)^2 + (-4.9 m/s)^2) = 10.2 m/s
		θ = arctan(Vy/ Vx) = arctan(-4.9 m/s / 9.0 m/s) = -29 degree

		The motorcycle is moving at 10.2 m/s in a direction 29.0° below the horizontal.
		"""
		evaluate = """
		EVALUATE Just as in Fig. 3.17, the motorcycle’s horizontal motion is unchanged by gravity; the motorcycle 
		continues to move horizontally at 9.0 m/s, covering 4.5 m in 0.50 s. The motorcycle initially has zero vertical 
		velocity, so it falls vertically just like an object released from rest and 
		descends a distance 1/2* g * t^2 = 1.2 m in 0.50 s.
		"""
		key_concept = """
		KEY CONCEPT
		The motion of a projectile is a combination of motion with constant velocity in the horizontal direction and motion 
		with constant downward acceleration in the vertical direction.
		"""
	
	
	def max_height_range(self):
		problem_statement = """
		Find the maximum height h and horizontal range R (see Fig. 3.23) of a projectile launched with 
		speed V0
		at an initial angle α0 between 0 and 90°. For a given V0, what value of α0 gives maximum 
		height? What value gives maximum horizontal range?
		"""
		g = 9.8  # m/s^2
		# Given initial velocity V0 and launch angle θ 
		# Get user input
		# Get user input
		V0 = float(input("Enter the initial velocity (m/s): "))
		t = float(input("Enter the time (seconds): "))
		
		angles = []

		while True:
			angle_input = input("Enter an angle in degrees (or 'done' to finish): ")
		
			if angle_input.lower() == 'done':
				break

			try:
				angle = float(angle_input)
				angles.append(angle)
			except ValueError:
				print("Invalid input. Please enter a valid angle.")
			
		for angle in angles:
			# Convert degrees to radians
			θ = math.radians(angle)

			# Calculate the height at the highest point (h) at t1
			h = (V0 ** 2 * math.sin(θ) ** 2) / (2 * g)
			# Calculate the height at the highest point (h)
			t2 = (V0 * math.sin(θ)) / g
			# Calculate the horizontal range (R)
			R = (V0 ** 2 * math.sin(2 * θ)) / g
			print(f"For θ = {angle} degrees:")
			print(f"Height at the highest point (h): {h:.2f} meters")
			print(f"Time at the highest point (t2): {t2:.2f} seconds")
			print(f"Horizontal range (R): {R:.2f} meters")
			print()
	
	def ball_at_height_thrown(self):
		problem_statement = """
		You throw a ball from your window 8.0 m above the ground. When the ball leaves your hand, 
		it is moving at 10.0 m/s
		at an angle of 20.0° below the horizontal. How far horizontally from your window will the ball 
		hit the ground? Ignore air resistance.
		"""
		g = 9.8  #gravity
		V0 = float(input("Enter the initial velocity (m/s): "))
		y = float(input("Enter height of where you are: "))
		angles = []

		while True:
			angle_input = input("Enter an angle in degrees (or 'done' to finish): ")
	
			if angle_input.lower() == 'done':
				break

			try:
				angle = float(angle_input)
				angles.append(angle)
			except ValueError:
				print("Invalid input. Please enter a valid angle.")
	
		for angle in angles:
			θ = math.radians(angle)
			discriminant = math.sqrt(((V0)**2)*((math.sin(θ))**2) - 2*g*(-y))
			t = (V0 * math.sin(-θ) + discriminant)/g
			t1 = (V0 * math.sin(-θ) - discriminant)/g
			x = V0 * math.cos(-θ) * t
			print(f"Time at the highest point (t): {t:.2f} seconds")
			print(f"Time at the highest point (t): {t1:.1f} seconds")
			print(f"Horizontal range (x) = {x:.1f} meters")
			print()
			
	def monkey_zookeeper(self):
		dart_monkey_problem = """
		A monkey escapes from the zoo and climbs a tree. After failing to entice the monkey 
		down, the zookeeper fires a tranquilizer dart directly at the monkey (Fig. 3.26). The monkey 
		lets go at the instant the dart leaves the gun. Show that the dart will always hit the monkey, 
		provided that the dart reaches the monkey before he hits the ground and runs away.
		"""
		d = float(input("Enter the horizontal distance to the monkey (in meters): "))
		V0 = float(input("Enter the initial velocity of the dart (in m/s): "))
		theta_degrees = float(input("Enter the launch angle (in degrees): "))
		θ = math.radians(theta_degrees)

		g = 9.8  #gravity
		t = d / (V0 * math.cos(θ))
		meet = d * math.tan(θ)
		
		# Print the results for the user
		print(f"Time of flight (t) = {t:.2f} seconds")
		print(f"Dart and monkey meet (intersection) = {meet:.2f} meters")

	
	def projectile_acceleration_no_air_resistance(self):
		while True:
			print("Choose a problem:")
			print("0. Enter 0 to exit")
			print("1. Batted Baseball: given V0, Angle, and needing to know position and velocity at time t")
			print("2. Motorcycle stunt: given magnitude and needing to know position and velocity at time t ")
			print("3. Max heigh h and horizontal range R of a projectile lauched given speed and angle")
			print("4. How far horizontally will the ball hit the ground?")
			print("5. Zookeeper hitting monkey with dart given angle, V0, and distance")
			choice = input("Enter your choice (1 or 3): ")
			
			if choice == '0':
				break;
			elif choice == '1':
				self.batted_baseball_problem()
			elif choice == '2':
				self.projected_horizontally_problem()
			elif choice == '3':
				self.max_height_range()
			elif choice == '4':	
				self.ball_at_height_thrown()
			elif choice == '5':	
				self.monkey_zookeeper()
			else:
				print("Invalid choice. Please select 1 or 4.")

	
	def sports_car(self):
		problem_lateral_acceleration = """
		WITH VARIATION PROBLEMS
		An Aston Martin V12 Vantage sports car has a “lateral acceleration” of  This is the 
		maximum centripetal acceleration the car can sustain without skidding out of a 
		curved path. If the car is traveling at a constant  (about  or ) on level ground, 
		what is the radius  of the tightest unbanked curve it can negotiate?
		"""
		#Ar is the lateral acceleration, V is the constant acceleration, R is the radius
		# Ask the user to enter lateral acceleration in m/s^2
		lateral_acceleration = float(input("Enter the lateral acceleration (m/s^2): "))

		# Ask the user to enter velocity in m/s
		velocity = float(input("Enter the velocity (m/s): "))

		# Calculate the radius of the tightest unbanked curve
		radius = velocity ** 2 / lateral_acceleration

		# Display the result to the user
		print(f"The radius of the tightest unbanked curve is {radius:.0f} meters.")
		
		
	def carnival_ride(self):
		carnival_ride_problem = """
		WITH VARIATION PROBLEMS
		Passengers on a carnival ride move at constant speed in a horizontal circle of 
		radius 5.0 m, making a complete circle in 4.0 s. What is their acceleration?
		"""
		# Given values
		radius = float(input("Enter the radius of the circle (in meters): "))
		time_period = float(input("Enter the time to complete one full circle (in seconds): "))

		# Calculate the velocity (V) using the formula V = 2πR / T
		V = (2 * math.pi * radius) / time_period

		# Calculate the lateral acceleration using the formula a = V^2 / R
		lateral_acceleration = (V ** 2) / radius
		# Calculate the velocity (V) using the formula V = 2πR / T
		V = (2 * math.pi * radius) / time_period
		
		# Calculate the centripetal acceleration using the same formula
		centripetal_acceleration = (V ** 2) / radius

		# Print the result
		print("Both centripetal accelarition and lateral acceleration are equal:")
		print(f"The lateral acceleration is {lateral_acceleration:.0 f} m/s^2")
		print(f"The centripetal acceleration is {centripetal_acceleration:.0f} m/s^2")
		print(f"The velocity is {V:.1f} m/s")

		
	def centripetal_acceleration(self):
		while True:
			print("Choose a problem:")
			print("0. Enter 0 to exit")
			print("1. what is the radius of the tightest unbanked curve it can negotiate?")
			print("2. What is their acceleration?'")
			choice = input("Enter your choice (1 or 2): ")
			
			if choice == '0':
				break;
			elif choice == '1':
				self.sports_car()
			elif choice == '2':
				self.carnival_ride()
			else:
				print("Invalid choice. Please select 1 or 4.")

	def relative_velocity_explained(self):
		# IDENTIFY the relevant concepts
		relative_velocity_concept = """
		Whenever you see the phrase “velocity relative to” or “velocity with respect to,” it’s likely that 
		the concepts of relative velocity will be helpful.
		"""

		# SET UP the problem
		setup_problem_concept = """
		Sketch and label each frame of reference in the problem. Each moving object has its own frame of reference; 
		in addition, you’ll almost always have to include the frame of reference of the earth’s surface. 
		(Statements such as “The car is traveling north at ” implicitly refer to the car’s velocity relative to the surface of the earth.) 
		Use the labels to help identify the target variable. For example, if you want to find the velocity of a car 
		with respect to a bus, your target variable is .
		"""

		# EXECUTE the solution
		execute_solution_concept = """
		Solve for the target variable using Eq. (3.32). (If the velocities aren’t along the same direction, 
		you’ll need to use the vector form of this equation, derived later in this section.) It’s important to note 
		the order of the double subscripts in Eq. (3.32):  means “velocity of A relative to B.” 
		These subscripts obey a kind of algebra. If we regard each one as a fraction, then the fraction on the left side 
		is the product of the fractions on the right side: . 
		You can apply this rule to any number of frames of reference. For example, if there are three frames of reference 
		A, B, and C, Eq. (3.32) becomes .
		"""

		# EVALUATE your answer
		evaluate_answer_concept = """
		Be on the lookout for stray minus signs in your answer. If the target variable is the velocity of a car relative to a bus, 
		make sure that you haven’t accidentally calculated the velocity of the bus relative to the car. 
		If you’ve made this mistake, you can recover by using Eq. (3.33).
		"""
	
	def straight_road(self):
		relative_velocity_problem = """
		WITH VARIATION PROBLEMS
		You drive north on a straight two-lane road at a constant velocity V_car. A truck in the other 
		lane approaches you at a constant velocity V_truck (Fig. 3.33). Find (a) the truck’s 
		velocity relative to you and (b) your velocity relative to the truck. (c) How do the relative 
		velocities change after you and the truck pass each other? 
		Treat this as a one-dimensional problem.
		"""
		# Ask the user to enter Vt/E_x and Vy/E_x values in km/h
		Vt_Ex = float(input("Enter Vt/E_x value in km/h: "))
		Vy_Ex = float(input("Enter Vy/E_x value in km/h: "))

		# Calculate Vt/Y_x in km/h
		Vt_Yx = Vt_Ex - Vy_Ex

		# Calculate Vy/T_x by setting it equal to Vt_Yx
		Vy_Tx = -Vt_Yx

		# Print the statement about the truck's motion relative to you
		print(f"A) The truck is moving at {Vt_Yx:.0f} km/h in the negative (south) relative to you.")

		# Print the statement about your motion relative to the truck
		print(f"B) You are moving at {Vy_Tx:.0f} km/h in the positive (north) relative to the truck.")
		print("C) The relative velocities do not change after you and the truck pass each other.")
		
		# Variable for the statement
		relative_velocities_do_not_change = """The relative velocities do not change after you and 
		the truck pass each other."""
		
	
	def flying_crosswind(self):
		print()
		# Variable for the statement
		airplane_velocity_relative_to_earth = """An airplane’s compass indicates that it is headed due 
		north, and its airspeed indicator shows that it is moving through the air at  If there is a  wind 
		from west to east, what is the velocity of the airplane relative to the earth?"""

		# Ask the user to enter airspeed indicator reading
		airspeed_indicator = float(input("Enter the airspeed indicator reading (in km/h): "))

		# Ask the user to enter wind speed from west to east
		wind_speed_west_east = float(input("Enter the wind speed from west to east (in km/h): "))

		# Calculate the airplane's relative speed to the earth using the distance formula
		relative_speed_to_earth = math.sqrt(airspeed_indicator**2 + wind_speed_west_east**2)
		# Calculate the direction (angle) using arctan
		direction_angle = math.degrees(math.atan2(wind_speed_west_east, airspeed_indicator))


		# Display the result to the user
		print(f"The airplane's relative speed to the earth is {relative_speed_to_earth:.0f} km/h.")
		print(f"The direction of the airplane's velocity relative to the earth is {direction_angle:.0f} degrees.")
		print("East of North")
		key_concept_relative_velocity = """
		KEY CONCEPT
		To solve problems involving relative velocity in a plane or in space, use Eq. (3.35). Pay careful attention to the subscripts for the frames of reference in the problem.
		"""
		print()
		
	def correcting_for_crosswind(self):
		problem_statement = """
		WITH VARIATION PROBLEMS
		With wind and airspeed as in Example 3.14, in what direction should the pilot head to travel due north? 
		What will be her velocity relative to the earth?
		Vp/e = magnitude unkown due north
		Vp/a = 240 km/h direction  unknown
		Va/e = 100 km/h                due east
		"""
		print(problem_statement)
		# Ask the user to enter airspeed indicator reading
		airspeed_indicator = float(input("Enter the airspeed indicator reading (in km/h): "))

		# Ask the user to enter wind speed from west to east
		wind_speed_west_east = float(input("Enter the wind speed from west to east (in km/h): "))
		
		# Calculate the airplane's relative speed to the earth using the distance formula
		relative_speed_to_earth = math.sqrt(airspeed_indicator**2 - wind_speed_west_east**2)

		# Calculate the direction (angle) using arcsin and convert to degrees
		direction_angle_pilot_should_point = math.degrees(math.asin(wind_speed_west_east / airspeed_indicator))

		# Display the results to the user
		print()
		print(f"The airplane's relative speed to the earth is {relative_speed_to_earth:.0f} m/s.")
		print(f"The pilot should point at an angle of {direction_angle_pilot_should_point:.0f} degrees from north.")
		key_concept = """
		KEY CONCEPT
		The vector equation for relative velocity in a plane, Eq. (3.35), allows you to solve for two 
		unknowns, such as an unknown vector magnitude and an unknown direction.
		"""
		print()



	
	def relative_velocity(self):
		while True:
			print("Choose a problem:")
			print("0. Enter 0 to exit")
			print("1. Velocity relative to you, you to them, how does velcity change after passing each other?")
			print("2. What's the airplane velocity relative to the earth?'")
			print("3. What direction should pilot head based on wind, what will his velocity be?'")
			choice = input("Enter your choice (1 or 2): ")
			self.relative_velocity_explained()
			if choice == '0':
				break;
			elif choice == '1':
				self.straight_road()
			elif choice == '2':
				self.flying_crosswind()
			elif choice == '3':
				self.correcting_for_crosswind()
			else:
				print("Invalid choice. Please select 1 or 4.")



	def user_choice(self):
		while True:
			print("Choose an option:")
			print("1. Exit")
			print("2. Ch 2 Calculate average velocity")
			print("3. Ch 2 Find instant velocity and average velocity")
			print("4. Ch 2 Find acceleration")
			print("5. Ch 2 Find instant acceleration")
			print("6. Ch 2 Find Constant acceleration")
			print("7. Ch 2 Find different acceleration")
			print("8. Ch 2 Find free falling acceleration")
			print("9. Ch 2 Find free falling acceleration when object is thrown upward")
			print("10. Ch 3 Find instant velocity and average velocity")
			print("11. Ch 3 Calculate parallel and perpendicular components of acceleration")
			print("12. Ch 3 Calculate projectile motion downward")
			print("13. Ch 3 Centripetal acceleration in circular motion")
			print("14. Ch 3 Relative velocity")
			
			choice = input("Enter the corresponding number: ")
			if choice == '1':
				print("Qutting")
				break;
			elif choice == '2':
				self.average_velocity_sign_rules()
				self.average_velocity()
			elif choice == '3':
				self.average_n_instant_velocity()
			elif choice == '4':
				self.acceleration_explanation()
				self.acceleration()
			elif choice == '5':
				self.instant_acceleration()
			elif choice == '6':
				self.constant_acceleration_explanation()
				self.constant_acceleration()
			elif choice == '7':
				self.different_acceleration()
			elif choice == '8':
				self.free_falling_explanation()
				self.free_falling()
			elif choice == '9':
				self.free_fall_up_and_down()
			elif choice =="10":
				self.acceleration_explained_3d_explanation()
				self.average_n_instant_velocity_3d()
			elif choice =="11":	
				self.parallel_n_perpendicular_acceleration_explanation()
				self.parallel_n_perpendicular_acceleration()
			elif choice =="12":	
				self.projectile_acceleration_no_air_resistance_explained()
				self.projectile_acceleration_no_air_resistance()
			elif choice =="13":	
				self.centripetal_acceleration()
			elif choice =="14":	
				self.relative_velocity()
			else:
				print("Invalid choice. Please enter '1' through '10'.")



# Create an instance of the class
calculator = Physic()

# Call the average_velocity method to calculate and display the result
calculator.user_choice()

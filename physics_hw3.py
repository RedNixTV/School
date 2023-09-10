import math

class Physic:
	
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

		
	
	def user_choice(self):
		print("Choose an option:")
		print("1. Calculate average velocity")
		choice = input("Enter the corresponding number: ")
		if choice == '1':
			self.calculate_average_velocity()

		else:
			print("Invalid choice. Please enter '1' through '10'.")



# Create an instance of the class
calculator = Physic()

# Call the average_velocity method to calculate and display the result
calculator.user_choice()

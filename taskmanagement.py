from datetime import timedelta
import datetime
import os
import json
import pytz
import json

class DeadlineTracker:
	def __init__(self):
		self.deadlines = {}
		self.load_deadlines()
	
	def get_valid_task_name(self):
		while True:
			task = input("Enter the task name: ")
			if task.strip() and any(c.isalpha() for c in task):
				return task
			print("Invalid task name. Please enter a non-empty name containing letters.")

	def get_valid_due_datetime(self):
		while True:
			due_datetime_input = input("Enter the updated due date and time (YYMMDDHHMM): ")
			try:
				due_datetime = datetime.datetime.strptime(due_datetime_input, "%y%m%d%H%M")
				# Convert to the desired format before returning
				formatted_due_datetime = due_datetime.strftime('%Y-%m-%d %H:%M:%S%z')
				return formatted_due_datetime
			except ValueError:
				print("Invalid date and time format. Please enter in YYMMDDHHMM format.")

	def get_valid_task_class(self):
		while True:
			task_class = input("What class: ")
			if task_class.strip() and any(c.isalpha() for c in task_class):
				return task_class
			print("Invalid class name. Please enter a non-empty name containing letters.")

	def add_deadline(self, task, due_datetime, task_class):
		self.deadlines.setdefault(task_class, []).append({
			"task": task,
			"due_date": due_datetime,
		})
		self.save_deadlines()


	def check_deadlines(self):
		today = datetime.datetime.now(pytz.timezone("US/Eastern"))

		print("Upcoming Deadlines:")
	
		# Create a list of (task_class, task_info) tuples, sorted by due_date
		sorted_deadlines = []
		for task_class, tasks in self.deadlines.items():
			for task_info in tasks:
				due_date_str = task_info["due_date"]
				due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d %H:%M:%S%z')
				if due_date > today:
					sorted_deadlines.append((due_date, task_class, task_info))

		# Sort the deadlines by due_date
		sorted_deadlines.sort(key=lambda x: x[0])

		# Print the sorted deadlines
		for idx, (due_date, task_class, task_info) in enumerate(sorted_deadlines, start=1):
			formatted_time = due_date.strftime('%Y-%m-%d %H:%M:%S%z')
			print(f"{idx}) {task_class}")
			print(f"     {task_info['task']}")
			print(f"     {formatted_time}\n")


	def delete_old_deadlines(self):
		today = datetime.datetime.now(pytz.timezone("US/Eastern"))

		old_tasks = {}
		for task_class, tasks in self.deadlines.items():
			old_tasks[task_class] = [
				task_info for task_info in tasks if
				datetime.datetime.strptime(task_info["due_date"], '%Y-%m-%d %H:%M:%S%z') < today - timedelta(days=3)
			]
		for task_class, old_task_list in old_tasks.items():
			self.deadlines[task_class] = [
				task_info for task_info in self.deadlines[task_class] if task_info not in old_task_list
			]

		# Save updated data to the deadlines.json file
		with open("deadlines.json", "w") as json_file:
			json.dump(self.deadlines, json_file, default=str, indent=4)
		print("Old deadlines successfully deleted and file updated.")
		

	def load_deadlines(self):
		if os.path.exists("deadlines.json"):
			with open("deadlines.json", "r") as file:
				self.deadlines = json.load(file)
		else:
			self.save_deadlines()  # Create an empty file
		
		
	def get_valid_task_name(self):
		while True:
			task = input("Enter the updated task name: ")
			if not (task.isdigit() or len(task) < 2):
				return task
			else:
				print("Invalid task name. Please enter a valid name.")

	def get_valid_due_datetime(self):
		while True:
			due_datetime_input = input("Enter the updated due date and time (YYMMDDHHMM): ")
			try:
				due_datetime = datetime.datetime.strptime(due_datetime_input, "%y%m%d%H%M'")
				return due_datetime
			except ValueError:
				print("Invalid date and time format. Please enter in YYMMDDHHMM format.")
				
	def get_valid_due_datetime(self):
		while True:
			due_datetime_input = input("Enter the updated due date and time (YYMMDDHHMM): ")
			try:
				due_datetime = datetime.datetime.strptime(due_datetime_input, "%y%m%d%H%M")
				# Convert to the desired format before returning
				formatted_due_datetime = due_datetime.replace(tzinfo=pytz.timezone("US/Eastern")).strftime('%Y-%m-%d %H:%M:%S%z')
				return formatted_due_datetime
			except ValueError:
				print("Invalid date and time format. Please enter in YYMMDDHHMM format.")


	def get_valid_task_class(self):
		while True:
			task_class = input("Enter the updated class: ")
			if len(task_class) > 0:
				return task_class
			else:
				print("Invalid class name. Please enter a valid name.")


	def update_deadline_option(self):
		print("Available Classes:")
		for idx, class_name in enumerate(self.deadlines.keys(), start=1):
			print(f"{idx}. {class_name}")
	
		try:
			class_number = int(input("Enter the number of the class for which you want to update deadlines: "))
			class_names = list(self.deadlines.keys())
			if 1 <= class_number <= len(class_names):
				class_name = class_names[class_number - 1]
			
				# Display deadlines for the selected class and update deadlines based on user input
				print(f"Updating deadlines for {class_name}:")
				class_deadlines = self.deadlines[class_name]
				for idx, task_info in enumerate(class_deadlines):
					print(f"Updating deadline {idx + 1}: {task_info['task']} - {task_info['due_date']}")
					print("Select an option:")
					print("1. Update Task")
					print("2. Update Due Date")
					print("3. Update Both")
					print("4. Skip")
					update_option = int(input("Enter your choice: "))
				
					if update_option == 1:
						updated_task = input(f"Enter the updated task for deadline {idx + 1}: ")
						task_info["task"] = updated_task
						print(f"Task for deadline {idx + 1} updated successfully!")
					elif update_option == 2:
						updated_due_datetime_input = input(f"Enter the updated due date and time for deadline {idx + 1} (YYMMDDHHMM): ")
						try:
							updated_due_datetime = datetime.datetime.strptime(updated_due_datetime_input, "%y%m%d%H%M")
							updated_due_datetime = updated_due_datetime.replace(second=0, tzinfo=pytz.timezone('US/Eastern'))
							task_info["due_date"] = updated_due_datetime.strftime('%Y-%m-%d %H:%M:%S%z')  # Convert to JSON format
							print(f"Due date for deadline {idx + 1} updated successfully!")
						except ValueError:
							print("Invalid date and time format. Please enter in YYMMDDHHMM format.")
					elif update_option == 3:
						updated_task = input(f"Enter the updated task for deadline {idx + 1}: ")
						updated_due_datetime_input = input(f"Enter the updated due date and time for deadline {idx + 1} (YYMMDDHHMM): ")
						try:
							updated_due_datetime = datetime.datetime.strptime(updated_due_datetime_input, "%y%m%d%H%M'")
							task_info["task"] = updated_task
							task_info["due_date"] = updated_due_datetime
							print(f"Deadline {idx + 1} updated successfully!")
						except ValueError:
							print("Invalid date and time format. Please enter in YYMMDDHHMM format.")
					elif update_option == 4:
						print(f"Skipping update for deadline {idx + 1}")
					else:
						print("Invalid option selected.")
			
				# Save updated data to the deadlines.json file
				self.save_deadlines()
				print("All updates completed successfully!")
			else:
				print("Invalid class number.")
		except ValueError:
			print("Invalid input. Please enter a valid number.")


	def save_deadlines(self):
		with open("deadlines.json", "w") as file:
			json.dump(self.deadlines, file, default=str,indent=4)

	def add_deadline_option(self):
		task = self.get_valid_task_name()
		due_datetime = self.get_valid_due_datetime()
		task_class = self.get_valid_task_class()
		self.add_deadline(task, due_datetime, task_class)
		print(f"Deadline added for {task} on {due_datetime} (Class: {task_class})")


	def delete_deadline_option(self):
		print("Delete Deadline:")
	
		# Show the available classes
		print("Available Classes:")
		for idx, class_name in enumerate(self.deadlines.keys(), start=1):
			print(f"{idx}. {class_name}")
	
		try:
			class_number = int(input("Enter the number of the class for which you want to delete a deadline: "))
			class_names = list(self.deadlines.keys())
			if 1 <= class_number <= len(class_names):
				class_name = class_names[class_number - 1]
			
				if class_name in self.deadlines:
					task_list = self.deadlines[class_name]
					print(f"Select a deadline to delete for {class_name}:")
					for idx, task_info in enumerate(task_list, start=1):
						formatted_time = datetime.datetime.strptime(task_info["due_date"], "%Y-%m-%d %H:%M:%S%z").strftime('%Y-%m-%d %H:%M:%S%z')
						print(f"{idx}. {task_info['task']} - {formatted_time}")

					try:
						deadline_idx = int(input("Enter the number of the deadline you want to delete: ")) - 1
						if 0 <= deadline_idx < len(task_list):
							deleted_task = task_list.pop(deadline_idx)
							print(f"Deleted: {deleted_task['task']}")
							# Save the updated deadlines to the JSON file
							self.save_deadlines()
						else:
							print("Invalid deadline number.")
					except ValueError:
						print("Invalid input. Please enter a valid number.")
				else:
					print("Invalid class name.")
			else:
				print("Invalid class number.")
		except ValueError:
			print("Invalid input. Please enter a valid number.")




	def exit_option(self):
		print("Exiting...")
		exit()

	def run(self):
		menu_options = {
			1: self.add_deadline_option,
			2: self.check_deadlines,
			3: self.delete_old_deadlines,
			4: self.update_deadline_option,  # Added option to update deadline
			5: self.delete_deadline_option,  # Added option to delete deadline
			6: self.exit_option
		}

		while True:
			print("1. Add Deadline")
			print("2. Check Deadlines")
			print("3. Delete Old Deadlines")
			print("4. Update Deadline")  # Added new option
			print("5. Delete Deadline")  # Added new option
			print("6. Exit")
	
			choice = None
			while choice not in menu_options:
				try:
					choice = int(input("Select an option: "))
				except ValueError:
					print("Invalid input. Please enter a valid number.")
	
			menu_options[choice]()

if __name__ == "__main__":
    tracker = DeadlineTracker()
    tracker.run()

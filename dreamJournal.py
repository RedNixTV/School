import os
import datetime
import json
import shutil  
import textwrap

class DreamJournal:
	def __init__(self):
		self.filename = "dreams.json"
		self.diary_filename = "diary.json"
		self.dream_signs = []
		# Define dictionaries to store categorized lists
		self.categories = {
			"Emotional Tone": ["None","Happy", "Sad", "Anxious", "Exciting", "Peaceful","Curious","Flirting","a little scared","Frustrated","Vindicated","Dissapointment","Upset","Pride","Rejected"],
			"Symbols": ["None","Flying","Animals","Levitating","Army uniform","Holding hands","ghost","Super Hero","Confrontational","Court room","Podium","Prisoners","Daily Life","Naked","Sex","Old Man","Homework","Football","House"],
			"Themes": ["Adventure", "Mystery", "Love", "Success", "Failure","Learning a Skill","Attending Class","Group Setting","Renting a building Floor","Fighting Enemy Forces","Fighting","Disorder","Penis","Team mission","Meeting Deadlines","Pattern Recognition","Playing Football","Buying a house"],
			"Time Period": ["None","Childhood", "Recent", "Recurring", "Past", "Future","Imaginary",],
			"Lucidity Level": ["Fully Lucid", "Partially Lucid", "Non-Lucid"],
			"People and Relationships": ["None","Family", "Friends", "Romantic", "Strangers", "Colleagues","Classmate","Teacher and Student","Fictitious Classmate","Fictitious Friends","Fictitious Team","Pet","Authority Figure","Famous People","Supervisor and Subordinate","Father and Son","Customer and owner"],
			"Physical Sensations": ["None","Flying Sensation", "Falling Sensation", "Heat/Cold", "Weightlessness", "Pain","Focus Attention"],
			"Dream Setting": ["My mind","Nature", "City", "Historical", "Fantasy", "Outer Space","House","Mansion","University or College","Classroom","Restaurant","Building","The wood","Court room","Farm","Business","Factory","Football Field"]
		}

	def choose_category(self, category_name):
		"""Allow the user to choose a category or enter their own."""
		print(f"Choose a {category_name} for the dream or enter your own:")
		category_list = self.categories[category_name]

		for i, category in enumerate(category_list, start=1):
			print(f"{i}. {category}")

		choice = input(f"Enter the number of your chosen {category_name} or enter your own: ")
		try:
			choice = int(choice)
			if 1 <= choice <= len(category_list):
				chosen_category = category_list[choice - 1]
			else:
				chosen_category = input(f"Enter your own {category_name}: ")
		except ValueError:
			chosen_category = input(f"Enter your own {category_name}: ")

		return chosen_category
	
	def add_dream_sign(self):
		"""Allow the user to add a dream sign."""
		dream_sign = input("Enter a dream sign (press Enter on an empty line to finish):\n")
		while dream_sign:
			self.dream_signs.append(dream_sign)
			dream_sign = input("Enter another dream sign or press Enter to finish:\n")
            
            
	def add_dream(self):
		"""Add a new dream entry to the journal with chosen categories, date, and interpretation."""
		dream_text = input("Enter your dream (press Enter when done):\n")

		# Allow the user to enter the dream text in one line
		dream_lines = [dream_text.strip()]

		# Allow the user to choose or manually enter the dream date
		dream_date = input("Enter the dream date (leave empty for today's date): ").strip()
		if not dream_date:
			dream_date = datetime.date.today().strftime("%Y-%m-%d")

		dream_categories = {}
		for category_name in self.categories.keys():
			chosen_category = self.choose_category(category_name)
			dream_categories[category_name] = chosen_category

		dream_interpretation = input("Would you like to provide an interpretation for this dream? (y/n): ")
		if dream_interpretation.lower() == "y":
			interpretation = input("Enter your dream interpretation: ")
		else:
			interpretation = "No interpretation provided."
		
		# Prompt user to add dream signs
		self.add_dream_sign()

		new_dream_entry = {
			"Date": dream_date,
			"Categories": dream_categories,
			"Dream": dream_text,
			"Interpretation": interpretation
		}

		try:
			# Check if the JSON file exists and is not empty
			existing_dreams = []
			if os.path.exists(self.filename) :
				with open(self.filename, "r") as json_file:
					existing_dreams = json.load(json_file)

			# Append the new dream entry to the existing dreams
			existing_dreams.append(new_dream_entry)

			# Save the updated dreams as a JSON file
			with open(self.filename, "w") as json_file:
				json.dump(existing_dreams, json_file, indent=4)

			print("Dream entry added successfully.")
		except Exception as e:
			print(f"An error occurred: {e}")
	
	def add_dream_sign(self):
			"""Add dream signs to the list of dream signs until the user types 'done'."""
			while True:
				dream_sign = input("Enter a dream sign (type 'done' to finish adding dream signs): ")
		
				if dream_sign.lower() == 'done':
					break

				# Add the dream sign to the list of dream signs
				self.dream_signs.append(dream_sign)

			# Save the dream signs to the JSON file
			self.save_dream_signs()

			print("Dream signs added successfully.")


	def save_dream_signs(self):
		"""Save the dream signs to the JSON file."""
		try:
			# Read existing dreams from the JSON file (if it exists)
			existing_dreams = []
			if os.path.exists(self.filename):
				with open(self.filename, "r") as json_file:
					existing_dreams = json.load(json_file)

			# Check if there are any dream entries to add dream signs to
			if existing_dreams:
				# Add the dream signs to the last dream entry
				last_dream_entry = existing_dreams[-1]
				if "Dream Signs" not in last_dream_entry:
					last_dream_entry["Dream Signs"] = []

				last_dream_entry["Dream Signs"].extend(self.dream_signs)

				# Save the updated dreams (with dream signs) to the JSON file
				with open(self.filename, "w") as json_file:
					json.dump(existing_dreams, json_file, indent=4)

		except Exception as e:
			print(f"An error occurred while saving dream signs: {e}")
			
	def diary(self):
		"""Add a new diary entry for waking life."""
		entry_text = input("Enter your diary entry for waking life (press Enter on an empty line to finish):\n")
		entry_lines = []

		# Allow the user to enter the entry text with line breaks
		while entry_text:
			entry_lines.append(entry_text)
			entry_text = input()

		entry_text = "\n".join(entry_lines)

		# Get the current date and time
		current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		new_entry = {
			"Timestamp": current_datetime,
			"Entry": entry_text
		}

		try:
			# Read existing diary entries from the JSON file (if it exists)
			existing_entries = []
			if os.path.exists(self.diary_filename):
				with open(self.diary_filename, "r") as json_file:
					existing_entries = json.load(json_file)

			# Append the new diary entry to the existing entries
			existing_entries.append(new_entry)

			# Save the updated entries as a JSON file (create it if it doesn't exist)
			with open(self.diary_filename, "w") as json_file:
				json.dump(existing_entries, json_file, indent=4)

			print("Diary entry added successfully.")
		except Exception as e:
			print(f"An error occurred: {e}")
				
	def view_diary(self):
			"""View all entries in the waking life diary."""
			if os.path.exists(self.diary_filename):
				with open(self.diary_filename, "r") as json_file:
					entries = json.load(json_file)

				# Get terminal size
				terminal_columns, _ = shutil.get_terminal_size()

				for entry in entries:
					timestamp = entry["Timestamp"]
					entry_text = entry["Entry"]

					# Split the entry text into lines to fit the terminal width
					entry_lines = entry_text.splitlines()
					formatted_entry = ""
					for line in entry_lines:
						# Wrap lines to fit the terminal width
						formatted_entry += "\n".join(textwrap.wrap(line, width=terminal_columns)) + "\n"

					print(f"Timestamp: {timestamp}")
					print(f"Entry:\n{formatted_entry}\n")
			else:
				print("No entries found in the waking life diary.")

				
	def run_journal(self):
			"""Run the dream journal application."""
			while True:
				print("\nDream Journal Menu:")
				print("1. Exit")
				print("2. Add a Dream Entry")
				print("3. View Dream Entries")
				print("4. View Dream Signs")  
				print("5. Add Dream Sign")
				print("6. Add a Diary Entry")
				print("7. View Diary Entries")

				choice = input("Enter your choice (1/2/3/4): ").strip()

				if choice == "1":
					print("Exiting the Dream Journal. Goodbye!")
					break
				if choice == "2":
					self.add_dream()
				elif choice == "3":
					self.view_dream_entries()
				elif choice == "4":
					self.view_dream_signs()  
				elif choice == "5":
					self.add_dream_sign()
				elif choice == "6":
					self.diary()
				elif choice == "7":
					self.view_diary()
				else:
					print("Invalid choice. Please select a valid option (1/2/3/4).")


if __name__ == "__main__":
    dream_journal = DreamJournal()
    dream_journal.run_journal()

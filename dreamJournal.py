import os
import datetime
import json

class DreamJournal:
	def __init__(self):
		self.filename = "dreams.json"
		# Define dictionaries to store categorized lists
		self.categories = {
			"Emotional Tone": ["None","Happy", "Sad", "Anxious", "Exciting", "Peaceful","Curious","Flirting","a little scared","Frustrated","Vindicated","Dissapointment","Upset","Pride"],
			"Symbols": ["None","Flying", "Water", "Animals", "Stars", "Keys","Levitating","Army uniform","Holding hands","ghost","Super Hero","Confrontational","Court room","Podium","Prisoners","Daily Life","Naked","Sex"],
			"Themes": ["Adventure", "Mystery", "Love", "Success", "Failure","Learning a Skill","Attending Class","Group Setting","Renting a building Floor","Fighting Enemy Forces","Fighting","Disorder","Penis","Team mission"],
			"Time Period": ["None","Childhood", "Recent", "Recurring", "Past", "Future","Imaginary",],
			"Lucidity Level": ["Fully Lucid", "Partially Lucid", "Non-Lucid"],
			"People and Relationships": ["None","Family", "Friends", "Romantic", "Strangers", "Colleagues","Classmate","Teacher and Student","Fictitious Classmate","Fictitious Friends","Fictitious Team","Pet","Authority Figure","Famous People","Supervisor and Subordinate","Father and Son"],
			"Physical Sensations": ["None","Flying Sensation", "Falling Sensation", "Heat/Cold", "Weightlessness", "Pain","Focus Attention"],
			"Dream Setting": ["My mind","Nature", "City", "Historical", "Fantasy", "Outer Space","House","Mansion","University or College","Classroom","Restaurant","Building","The wood","Court room","Farm"]
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

		new_dream_entry = {
			"Date": dream_date,
			"Categories": dream_categories,
			"Dream": dream_text,
			"Interpretation": interpretation
		}

		try:
			# Check if the JSON file exists and is not empty
			existing_dreams = []
			if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
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





	def track_recurring_aspects(self, aspect):
		with open("recurring_aspects.txt", "a") as aspects_file:
			aspects_file.write(aspect + "\n")

		   
	def run_journal(self):
		"""Run the dream journal application."""
		while True:
			print("\nDream Journal Menu:")
			print("1. Exit")
			print("2. Add a Dream Entry")
			print("3. View Dream Entries")
			

			choice = input("Enter your choice (1/2/3/4): ").strip()

			if choice == "1":
				print("Exiting the Dream Journal. Goodbye!")
				break
			if choice == "2":
				self.add_dream()
			else:
				print("Invalid choice. Please select a valid option (1/2/3/4).")




if __name__ == "__main__":
    dream_journal = DreamJournal()
    dream_journal.run_journal()

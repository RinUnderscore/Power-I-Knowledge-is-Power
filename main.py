# Import Packages
import os
import time
import random
import pyfiglet
import json

if __name__ == "__main__":
	# Loading Page
	while True:
		print(pyfiglet.figlet_format("Power I: Knowledge is Power"))
		cmd = input("Would you like to:\n1. Create New Save Slate\n2. Load Slate from String\n")
		if cmd == "1":
			os.system('clear')
			print("Creating Slate...")

			# Create New Save Slate
			userdata = {}

			# Setup New Account
			cmd = input("Create an Username: ")
			userdata["username"] = cmd
			userdata["inventory"] = "sp|"
			
			break
		elif cmd == "2":
			os.system('clear')
			cmd = input("Please enter your save string: ")
			print("Loading Save Slate from string")
			cmd = cmd.replace("'", '"')
			userdata = json.loads(cmd)
			break
		else:
			print("That was not an selection...")
			time.sleep(1)
			os.system('clear')

	# Game Loop
	while True:
		os.system("clear")
		print("Power I: Knowledge is Power")

		# Load Inventory
		inventory = userdata["inventory"].split("|")
		
		cmd = input("Welcome " + str({userdata["username"]}) + ", please select an action to complete.\n1. Mine\n2. Craft\n3. Research\n4. Inventory\n5. Use Machine\n6. Settings\nSelector: ")
		if cmd == "1":
			print("Mining...")
			time.sleep(1)
			if "sp" in str(userdata["inventory"]):
				rng = random.randint(1,3)
				if rng == 1 or rng == 2:
					print("You have recieved [1] Stone")
					userdata["inventory"] += "s|"
					time.sleep(2)
				if rng == 3:
					print("You have recieved [1] Copper Ore")
					userdata["inventory"] += "co|"
					time.sleep(2)
		if cmd == "2":
			cmd = input("Please enter what you would like to craft (ABREVIATIONS FROM MIRO ONLY): ")
			if cmd == "SP2":
				if inventory.count("s") >= 5:
					print("Crafting your Simple Processor... (SP2)")
					time.sleep(3)
					for a in range(4):
						inventory.remove("s")
					inventory.append("sp2")
					# Update Inventory
					userdata["inventory"] = ""
					for b in range(len(inventory)):
						userdata["inventory"] += f"{inventory[b]}|"
					time.sleep(4)
		if cmd == "3":
			print("Here is the link to the progression of items and all of the crafting recipies: https://miro.com/app/board/uXjVPv0KJYc=/")
			time.sleep(5)
		if cmd == "4":
			print("Loading Inventory... This will display your inventory using the code names in the official MIRO with all the items. Please refer to this while checking your inventory: https://miro.com/app/board/uXjVPv0KJYc=/?share_link_id=681750273087")
			try:
				for c in range(len(inventory)):
					inventory.remove("")
			except ValueError:
				inventory = inventory
			print(inventory)
			cmd = input("Press Enter to Continue... ")
		if cmd == "5":
			cmd = input("Select the machine you would like to use: ")
			if cmd in inventory:
				if cmd == "sp2":
					cmd = input("What would you like to create: ")
					if cmd == "n":
						try:
							print("Processing...")
							for d in range(2):
								inventory.remove("s")
							inventory.append("n")
							# Clear and Reset Inventory
							userdata["inventory"] = ""
							for b in range(len(inventory)):
								userdata["inventory"] += f"{inventory[b]}|"
							time.sleep(4)
							print('Completed!')
							time.sleep(1)
						except ValueError:
							print("You do not have enough resources to complete this action.")
							time.sleep(3)
					else:
						print("This machine does not produce this part.")
						time.sleep(3)
			else:
				print("This machine does not exist/is not in your inventory.")
		if cmd == "6":
			cmd = input("Would you like to view: \n1. Export Save String\n2. Credits\n")
			if cmd == "1":
				print("Please make sure to copy this without CTRL+C because this doesn't work on console, use your mouse to copy and paste it. Thank you and make sure you have it on the clipboard before closing out of this page.")
				print(f"\n\nSave String:\n\n{userdata}")
			if cmd == "2":
				print("I'm glad you actually tried to view the credits and give appreciation to me, but unfortunately, I don't have enough braincells to code this. See you!")
			cmd = input("\nPress enter to continue... ")	

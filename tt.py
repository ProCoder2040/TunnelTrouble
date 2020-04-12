import re
from colorama import Fore, Back, Style
from colorama import init
init()



rooms = {
	1: {
		"description":["You are in a cave, there is a tunnel to the north and a door to the south"],
		"exits":{
			"south": {"room_num":2, "transition": "You open the door and cautiously step inside."}, 
			"north": {"room_num":5},
		}
	},
	2: {
		"description":[			
			"It is suprisingly warm in here.",
			"There is a door to the North, and a tunnel to the South and a tunnel to the South East.",
			"Behind the door to the North, there is a bright light.",
			"In the tunnel to the South, there is an intense heat.",
			"In the tunnel to the South East, there is a faint moaning noise.",
		],
		"exits":{
			"south": {"room_num":3}, 
			"north": {"room_num":1}, 
			"south east": {"room_num":4},
		}
	},
	3: {
		"description":["You walk into the room and are almost overwhelmed by the heat. A Lava monster simply plucks you from the ground and swallows you whole. THE END!!"],
		"exits":{
			"restart": {"room_num":1},
		},
	},
	4: {
		"description":["Zombie Room"],
		"exits": {
			"north west":{"room_num":2}
		}
	}
}
current_position=1
while True:
	print ("\n".join(rooms[current_position]["description"]))
	command = input("What do you want to do?")
	if command=="exit":
		break
	if command in rooms[current_position]["exits"]:
		if "transition" in rooms[current_position]["exits"][command]:
			print (rooms[current_position]["exits"][command]["transition"])
		current_position = rooms[current_position]["exits"][command]["room_num"]
	else:		
		print (Fore.RED + "I didn't understand that..."+Style.RESET_ALL)

print (Fore.GREEN + "Thanks for playing Tunnel Trouble!!!"+Style.RESET_ALL)




# name= input("hello, What is your name? ")
# print ("Hello " + name)

# print("""
# You wake up in the middle of a cave! 
# There is a lantern here. 
# You can see a tunnel to the north and a door to the south. 
# Behind the door, you hear flowing liquid.""")

# command = input("What do you want to do? ")
# print("You said "+ command)

# if re.search('north', command, re.IGNORECASE):
# 	print ("You walk north through the tunnel. You come to an intersection.")
# 	print ("There is a tunnel to the North East, a tunnel to the North West and a tunnel to the south.")
# 	print ("It's very dark here.")
# elif re.search('south', command, re.IGNORECASE):
# 	print ("You open the door and cautiously step inside.")
# 	print ("It is suprisingly warm in here.")
# 	print ("There is a door to the North, and a tunnel to the South and a tunnel to the South East")
# 	print ("Behind the door to the North, there is a bright light.")
# 	print ("In the tunnel to the South, there is an intense heat.")
# 	print ("In the tunnel to the South East, there is a faint moaning noise.")
# 	command = input("What do you want to do? ")
# 	if re.search('North', command, re.IGNORECASE):


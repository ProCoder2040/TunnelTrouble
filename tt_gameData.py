from colorama import Fore, Back, Style
from colorama import init

rooms = {
	1: {
		"description":[Fore.BLUE + "You are in a cave, there is a tunnel to the north and a door to the south."],
		"exits":{
			"south": {"room_num":2, "transition": "You open the door and cautiously step inside."}, 
			"north": {"room_num":5},
		}
	},
	2: {
		"description":[			
			Fore.BLUE + "It is suprisingly warm in here.",
			Fore.BLUE + "There is a door to the North, and a tunnel to the South and a tunnel to the South East.",
			Fore.BLUE + "Behind the door to the North, there is a bright light.",
			Fore.BLUE + "In the tunnel to the South, there is an intense heat.",
			Fore.BLUE + "In the tunnel to the South East, there is a faint moaning noise.",
		],
		"exits":{
			"south": {"room_num":3}, 
			"north": {"room_num":1}, 
			"south east": {"room_num":4},
		}
	},
	3: {
		"description":[Fore.RED + "You walk into the room and are almost overwhelmed by the heat.",
		Fore.RED + " A Lava monster simply plucks you from the ground and swallows you whole. THE END!!"],
		"exits":{
			"restart": {"room_num":1},
		},
	},
	4: {
		"description":["Zombie Room"],
		"exits": {
			"north west":{"room_num":2}
		}
	},
	5: {
		"description": [
			Fore.BLUE + "You come across an intersection.", 
			Fore.BLUE + "You can exit from: North West, North East and South.",
			Fore.BLUE + "From the North West you can hear the unmistakable sound of pickaxes mining.",
			Fore.BLUE + "From the South you can see a bright light.",
			Fore.BLUE + "From the North East you can see some stlactites and stalacmites.",
		],
		"exits":{
			"south": {"room_num":1}
		}
	}
}